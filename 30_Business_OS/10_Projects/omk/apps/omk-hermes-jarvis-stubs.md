# Chantier C — Hermes Jarvis Surface (OMK SaaS OS) — Stubs Spec

> **Statut** : SPEC FILE (repo `omk-services/00-omk-saas-os` NOT cloned locally at the time of writing 2026-07-03).
> Quand A0 clone le repo (ou délègue `picard-repo-home`), drop-in ces 2 fichiers aux paths indiqués.
> **Référence stack confirmée** : Next.js 14+ App Router (voir `apps/dashboard/src/app/`), Supabase Cloud project `ndvqwcapwcnpdvknxcjw`.

---

## 1. Contexte canonique

- **App OMK SaaS** : `https://omk-saas-os.vercel.app/`
- **Vercel team** : `omk-services`
- **Repo GitHub** : `omk-services/00-omk-saas-os`
- **Supabase project_id** : `ndvqwcapwcnpdvknxcjw` (= OMK SERVICES CUSTOMERS)
- **Hermes runtime** : `C:\Users\amado\.hermes\` (gateway local + VPS aspace-vps/srv941028)
- **Réf visuelle Enterprise OS** : capture A0 — onglet "Jarvis" + Main agent "Chat" + "Connections" (Telegram Bot + Slack App)

**Bénéfice livraison Chantier C** : la surface Hermes Jarvis permet aux customers OMK SaaS de chatter avec l'agent IA depuis le dashboard, branchable LIVE (env vars) ou MOCK (dev) — sans PII leakage, avec audit log Supabase systématique.

---

## 2. Fichiers à créer dans `00-omk-saas-os/`

| Path dans le repo | Rôle | LOC |
|---|---|---|
| `src/app/api/agent/chat/route.ts` | Endpoint POST Hermes (auth + proxy + audit) | ~95 |
| `src/components/agent/AgentChat.tsx` | Drawer flottant React + Tailwind | ~165 |
| **Total** | | **~260** |

**Naming aligné sur `apps/dashboard/src/`** (App Router, `src/` directory enabled).

---

## 3. Fichier 1 — `src/app/api/agent/chat/route.ts`

```typescript
// src/app/api/agent/chat/route.ts
// Chantier C — Hermes Jarvis surface (OMK SaaS)
// POST /api/agent/chat — Supabase auth + Hermes proxy OR MOCK + audit log
// D1 receipt: POST → 200 {reply, mode: 'live'|'mock', ...}

import { NextRequest, NextResponse } from 'next/server';
import { createServerClient } from '@supabase/ssr';
import { randomUUID } from 'crypto';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

interface ChatBody {
  message: string;
  conversation_id?: string;
}

interface ChatResponse {
  reply: string;
  conversation_id: string;
  model: string;
  latency_ms: number;
  mode: 'live' | 'mock';
}

const HERMES_URL = process.env.HERMES_GATEWAY_URL ?? '';
const HERMES_TOKEN = process.env.HERMES_GATEWAY_TOKEN ?? '';
const MOCK_REPLY =
  '[OMK Jarvis MOCK] Reçu : "' +
  '{message}' +
  '". Branchez HERMES_GATEWAY_URL + HERMES_GATEWAY_TOKEN pour passer en LIVE.';

export async function POST(req: NextRequest): Promise<NextResponse<ChatResponse | { error: string }>> {
  const t0 = Date.now();

  // 1. Auth Supabase session
  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    { cookies: { getAll: () => req.cookies.getAll() } }
  );
  const { data: { user }, error: authErr } = await supabase.auth.getUser();
  if (authErr || !user) {
    return NextResponse.json({ error: 'unauthorized' }, { status: 401 });
  }

  // 2. Parse body
  let body: ChatBody;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: 'invalid_json' }, { status: 400 });
  }
  const message = (body.message ?? '').trim();
  if (!message) {
    return NextResponse.json({ error: 'empty_message' }, { status: 400 });
  }
  const conversationId = body.conversation_id ?? randomUUID();

  // 3. Branch LIVE (env vars set) OR MOCK fallback
  let reply: string;
  let model: string;
  let mode: 'live' | 'mock';

  if (HERMES_URL && HERMES_TOKEN) {
    try {
      const r = await fetch(`${HERMES_URL.replace(/\/$/, '')}/v1/agent/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${HERMES_TOKEN}`,
        },
        body: JSON.stringify({ message, conversation_id: conversationId, user_id: user.id }),
        signal: AbortSignal.timeout(30_000),
      });
      if (!r.ok) throw new Error(`hermes_${r.status}`);
      const data = (await r.json()) as { reply?: string; model?: string };
      reply = data.reply ?? '[Hermes] empty reply';
      model = data.model ?? 'hermes-unknown';
      mode = 'live';
    } catch (e) {
      // Hermes down → fall back to MOCK (do NOT silently leak error to user)
      reply = `[Hermes unreachable, MOCK fallback] Reçu : "${message}".`;
      model = 'mock-fallback';
      mode = 'mock';
    }
  } else {
    reply = MOCK_REPLY.replace('{message}', message.slice(0, 200));
    model = 'mock-dev';
    mode = 'mock';
  }

  const latency_ms = Date.now() - t0;

  // 4. Audit log (no PII leakage — metadata is structural only)
  await supabase.from('omk_saas.audit_log').insert({
    actor_id: user.id,
    action: 'agent.chat',
    target_id: conversationId,
    metadata: {
      mode,
      model,
      latency_ms,
      message_len: message.length, // length NOT content
      ip: req.headers.get('x-forwarded-for')?.split(',')[0] ?? null,
    },
  });

  return NextResponse.json({ reply, conversation_id: conversationId, model, latency_ms, mode });
}
```

---

## 4. Fichier 2 — `src/components/agent/AgentChat.tsx`

```tsx
// src/components/agent/AgentChat.tsx — Chantier C Hermes Jarvis (OMK SaaS)
// Floating button + right drawer + history from audit_log. Tailwind, dark-aware.

'use client';

import { useEffect, useRef, useState } from 'react';
import { Sparkles, X, Send, Loader2 } from 'lucide-react';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  ts: number;
  mode?: 'live' | 'mock';
}

const MAX_HISTORY = 50;
const DRAWER_WIDTH = 400;

export function AgentChat(): JSX.Element {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [sending, setSending] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open || messages.length > 0) return;
    void (async () => {
      try {
        const r = await fetch('/api/agent/history', { credentials: 'include' });
        if (!r.ok) return;
        const data = (await r.json()) as { messages: Message[] };
        setMessages(data.messages.slice(-MAX_HISTORY));
      } catch {}
    })();
  }, [open, messages.length]);

  useEffect(() => {
    if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [messages]);

  async function send(): Promise<void> {
    const trimmed = input.trim();
    if (!trimmed || sending) return;
    setSending(true);
    const userMsg: Message = { id: crypto.randomUUID(), role: 'user', content: trimmed, ts: Date.now() };
    setMessages((m) => [...m, userMsg].slice(-MAX_HISTORY));
    setInput('');
    try {
      const r = await fetch('/api/agent/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ message: trimmed, conversation_id: conversationId }),
      });
      if (!r.ok) throw new Error(`http_${r.status}`);
      const data = (await r.json()) as { reply: string; conversation_id: string; mode: 'live' | 'mock' };
      setConversationId(data.conversation_id);
      setMessages((m) =>
        [...m, { id: crypto.randomUUID(), role: 'assistant', content: data.reply, ts: Date.now(), mode: data.mode }].slice(-MAX_HISTORY)
      );
    } catch {
      setMessages((m) =>
        [...m, { id: crypto.randomUUID(), role: 'assistant', content: '[erreur réseau — réessaie]', ts: Date.now() }].slice(-MAX_HISTORY)
      );
    } finally {
      setSending(false);
    }
  }

  const btnCls = 'fixed bottom-6 right-6 z-40 flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 text-white shadow-lg shadow-indigo-500/30 transition hover:scale-105 hover:shadow-xl';
  const drawerCls = 'fixed bottom-0 right-0 top-0 z-50 flex flex-col border-l border-white/10 bg-slate-900/85 backdrop-blur-xl text-slate-100 shadow-2xl';

  return (
    <>
      <button type="button" onClick={() => setOpen(true)} aria-label="Ouvrir Jarvis" className={open ? 'hidden' : btnCls}>
        <Sparkles className="h-6 w-6" />
      </button>

      {open && (
        <aside role="dialog" aria-label="Jarvis chat" className={drawerCls} style={{ width: DRAWER_WIDTH }}>
          <header className="flex items-center justify-between border-b border-white/10 px-4 py-3">
            <div className="flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-indigo-400" />
              <h2 className="font-semibold">Jarvis</h2>
              <span className="rounded-full bg-emerald-500/20 px-2 py-0.5 text-xs text-emerald-300">Hermes</span>
            </div>
            <button type="button" onClick={() => setOpen(false)} aria-label="Fermer" className="rounded p-1 hover:bg-white/10">
              <X className="h-5 w-5" />
            </button>
          </header>

          <div ref={scrollRef} className="flex-1 overflow-y-auto px-4 py-3 space-y-3">
            {messages.length === 0 && (
              <p className="text-sm text-slate-400 text-center mt-8">Bonjour. Pose ta question — Hermes répond (MOCK en dev, LIVE en prod).</p>
            )}
            {messages.map((m) => (
              <div key={m.id} className={'flex ' + (m.role === 'user' ? 'justify-end' : 'justify-start')}>
                <div className={'max-w-[85%] rounded-2xl px-3 py-2 text-sm ' + (m.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-white/10 text-slate-100')}>
                  {m.content}
                  {m.mode === 'mock' && <span className="ml-2 text-[10px] uppercase tracking-wide text-amber-300/80">mock</span>}
                </div>
              </div>
            ))}
          </div>

          <form onSubmit={(e) => { e.preventDefault(); void send(); }} className="flex gap-2 border-t border-white/10 p-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Demande à Jarvis..."
              disabled={sending}
              className="flex-1 rounded-lg bg-white/5 px-3 py-2 text-sm placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 disabled:opacity-50"
            />
            <button type="submit" disabled={sending || !input.trim()} aria-label="Envoyer" className="flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-600 text-white transition hover:bg-indigo-500 disabled:opacity-50">
              {sending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
            </button>
          </form>
        </aside>
      )}
    </>
  );
}
```

---

## 5. Branchement Hermes — MOCK → LIVE (env vars)

### MOCK (dev par défaut, ZERO config)
- `HERMES_GATEWAY_URL` absent **ou** `HERMES_GATEWAY_TOKEN` absent → réponse MOCK
- Pas d'appel réseau sortant, pas de dépendance runtime
- Le badge `mock` apparaît dans le drawer pour transparency

### LIVE (prod Vercel)
```bash
# Sur Vercel team omk-services, projet 00-omk-saas-os :
vercel env add HERMES_GATEWAY_URL production
# Valeur recommandée : https://hermes.<vps-domain>.sslip.io
# (sslip.io = wildcard DNS gratuit pour VPS Hostinger)
# OU http://localhost:8080 (si tunnel SSH)

vercel env add HERMES_GATEWAY_TOKEN production
# Valeur : token Bearer long-lived généré par `hermes config set token-gen`

# Restart le deploy Vercel pour prendre en compte les nouvelles env vars
vercel --prod
```

### Endpoint Hermes attendu côté VPS
```
POST {HERMES_GATEWAY_URL}/v1/agent/chat
Authorization: Bearer {HERMES_GATEWAY_TOKEN}
Content-Type: application/json
Body: { message: string, conversation_id: string, user_id: string }
Response: { reply: string, model: string }
```

### Check de santé post-deploy
```bash
curl -X POST https://omk-saas-os.vercel.app/api/agent/chat \
  -H 'Content-Type: application/json' \
  -b 'sb-access-token=...' \
  -d '{"message":"ping"}'
# Attendu : {"reply":"...","mode":"live","model":"hermes-minimax-m3","latency_ms":<N>}
```

---

## 6. Endpoint history (TODO Chantier C.1 — non livré ici)

Pour l'UI `loadHistory()` ci-dessus, il manque la route `GET /api/agent/history` qui lit `omk_saas.audit_log` WHERE actor_id=current_user AND action='agent.chat' ORDER BY created_at DESC LIMIT 50.

**Spec rapide** (≤30 lignes) :
```typescript
// src/app/api/agent/history/route.ts
export async function GET(req: NextRequest) {
  const supabase = createServerClient(/* ... */);
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: 'unauthorized' }, { status: 401 });
  const { data } = await supabase
    .from('omk_saas.audit_log')
    .select('id, created_at, metadata, target_id')
    .eq('actor_id', user.id)
    .eq('action', 'agent.chat')
    .order('created_at', { ascending: false })
    .limit(50);
  return NextResponse.json({
    messages: (data ?? []).flatMap((r) => [
      { id: r.id + '-u', role: 'user', ts: new Date(r.created_at).getTime(), content: '[user msg]', conversation_id: r.target_id },
      { id: r.id + '-a', role: 'assistant', ts: new Date(r.created_at).getTime() + 100, content: '[reply]', mode: r.metadata?.mode },
    ]),
  });
}
```
> ⚠️ Le contenu exact user/assistant n'est pas stocké dans audit_log (metadata = length uniquement, anti-PII-leakage). Si A0 veut history lisible, créer table dédiée `omk_saas.agent_messages` (Chantier C.1 future).

---

## 7. Anti-patterns doc

- ❌ **Pas d'auth bypass** : `supabase.auth.getUser()` obligatoire, sinon `401`. Mock ne peut pas être atteint sans auth.
- ❌ **Pas de PII dans metadata** : `audit_log.metadata` stocke UNIQUEMENT `mode`, `model`, `latency_ms`, `message_len`, `ip`. PAS de `message` ni `reply`.
- ❌ **Pas de streaming SSE sans backpressure** : on attend la réponse complète (`fetch` sync). Streaming = Chantier C.2 si demandé (read-backpressure avec ReadableStream + AbortController).
- ❌ **Pas de hardcode du endpoint Hermes** : env var `HERMES_GATEWAY_URL` OBLIGATOIRE. Aucune URL en dur dans le code.
- ❌ **Pas de secret en clair** : `HERMES_GATEWAY_TOKEN` lu depuis env var (User scope), jamais loggé.
- ❌ **Pas de POST /api/agent/chat sans CSRF** : Supabase auth = cookie HttpOnly SameSite=Lax → protection CSRF native. Pas besoin de token supplémentaire.

---

## 8. D1 receipts (CHANTIER C : PARTIAL — spec livrée, code à drop-in)

- **Spec file** : `C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/omk-hermes-jarvis-stubs.md`
- **File 1 (route.ts)** : 95 lignes, in spec §3
- **File 2 (AgentChat.tsx)** : 165 lignes, in spec §4
- **Endpoint history** : spec §6 (Chantier C.1 future, ≤30 lignes)
- **Handoff canonique** : `wiki/hand_offs/handoff_hermes_jarvis_omk_2026-07-03.md`
- **Log MD** : `wiki/log.md` (entry appended 2026-07-03)

---

## 9. Status final

**CHANTIER C : PARTIAL (spec livrée) → DONE quand repo cloné + 2 fichiers drop-in + 1 deploy Vercel.**

**Bénéfice Chantier C.0** : la spec permet à A0 (ou un sub-agent `b3-6-cyborg-it`) de drop-in le code dès que `omk-services/00-omk-saas-os` est cloné localement. Aucun risque de désync entre les 2 fichiers (ils sont dans le même doc).

**Prochaine étape recommandée (Chantier C.1)** : ajouter table `omk_saas.agent_messages` (id, conversation_id, actor_id, role, content, created_at) + endpoint `GET /api/agent/history` qui lit CETTE table (pas audit_log) → history lisible user/assistant full-fidelity.
