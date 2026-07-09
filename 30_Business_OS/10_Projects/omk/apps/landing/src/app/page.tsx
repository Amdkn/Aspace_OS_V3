"use client";

import React, { useEffect, useRef, useState, Fragment } from "react";
import { Icon } from "@/components/icons";

import { AuditForm } from "@/components/audit-form";

/* ------------------------------------------------------------------ */
/* Building blocks                                                    */
/* ------------------------------------------------------------------ */

const MeshBackdrop = () => (
  <div aria-hidden="true" className="absolute inset-0 overflow-hidden pointer-events-none">
    {/* grid */}
    <div className="absolute inset-0 grid-bg grid-bg-fade opacity-60" />
    {/* mesh blobs */}
    <div className="blob animate-drift"     style={{ width: 620, height: 620, top: -160, left: -120, background: 'radial-gradient(circle at 30% 30%, #3B82F6 0%, transparent 60%)' }} />
    <div className="blob animate-driftSlow" style={{ width: 720, height: 720, top: -80,  right: -200, background: 'radial-gradient(circle at 60% 40%, #8B5CF6 0%, transparent 65%)' }} />
    <div className="blob animate-drift"     style={{ width: 520, height: 520, top:  260, left: '38%', background: 'radial-gradient(circle at 50% 50%, #EC4899 0%, transparent 65%)', opacity: 0.32 }} />
    {/* horizon fade */}
    <div className="absolute inset-x-0 top-[860px] h-[420px] bg-gradient-to-b from-transparent via-ink-950/70 to-ink-950" />
  </div>
);

const Pill = ({ children, dot = true }: { children: React.ReactNode; dot?: boolean }) => (
  <span className="inline-flex items-center gap-2 rounded-full glass px-3 py-1.5 text-xs font-medium text-slate-300">
    {dot && <span className="relative flex h-1.5 w-1.5">
      <span className="absolute inset-0 rounded-full bg-fuchsia-400 animate-pulseDot" />
      <span className="relative rounded-full bg-fuchsia-400 h-1.5 w-1.5" />
    </span>}
    {children}
  </span>
);

const BtnPrimary = ({ children, className = '', icon = true, href = '#audit' }: { children: React.ReactNode; className?: string; icon?: boolean; href?: string }) => (
  <a href={href} className={`btn-mesh group inline-flex items-center justify-center gap-2 rounded-full px-5 py-3 text-sm font-semibold text-white transition hover:brightness-110 ${className}`}>
    <span className="relative z-10 flex items-center gap-2">
      {children}
      {icon && <Icon.ArrowRight size={16} className="transition group-hover:translate-x-0.5" />}
    </span>
  </a>
);

const BtnGhost = ({ children, className = '', href = '#methode' }: { children: React.ReactNode; className?: string; href?: string }) => (
  <a href={href} className={`inline-flex items-center justify-center gap-2 rounded-full glass px-5 py-3 text-sm font-semibold text-slate-200 transition hover:border-white/25 hover:bg-white/10 ${className}`}>
    {children}
  </a>
);

const SectionTag = ({ children }: { children: React.ReactNode }) => (
  <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] uppercase tracking-[0.18em] text-slate-400">
    <span className="h-1 w-1 rounded-full bg-fuchsia-400" />
    {children}
  </div>
);

/* Spotlight effect — adds css vars on hover */
const useSpotlight = () => {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current; if (!el) return;
    const onMove = (e: PointerEvent) => {
      const r = el.getBoundingClientRect();
      el.style.setProperty('--mx', `${e.clientX - r.left}px`);
      el.style.setProperty('--my', `${e.clientY - r.top}px`);
    };
    el.addEventListener('pointermove', onMove);
    return () => el.removeEventListener('pointermove', onMove);
  }, []);
  return ref;
};

/* Reveal on scroll */
const useReveal = () => {
  useEffect(() => {
    const els = document.querySelectorAll('.reveal');
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
    }, { threshold: 0.12 });
    els.forEach(el => io.observe(el));
    return () => io.disconnect();
  }, []);
};

/* ------------------------------------------------------------------ */
/* Header                                                             */
/* ------------------------------------------------------------------ */

const Header = () => {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);
  return (
    <header className={`fixed inset-x-0 top-0 z-50 transition-all ${scrolled ? 'backdrop-blur-xl bg-ink-950/70 border-b border-white/5' : ''}`}>
      <div className="mx-auto max-w-7xl px-6 lg:px-10">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <a href="#" className="flex items-center gap-2.5 group">
            <span className="relative flex h-8 w-8 items-center justify-center rounded-lg" style={{ background: 'linear-gradient(135deg, #3B82F6, #8B5CF6 55%, #EC4899)' }}>
              <span className="absolute inset-[1px] rounded-[7px] bg-ink-950 flex items-center justify-center">
                <span className="font-display text-[15px] font-bold text-mesh">O</span>
              </span>
            </span>
            <div className="leading-none">
              <div className="font-display text-[15px] font-bold tracking-tight text-white">OMK <span className="text-slate-400 font-medium">SERVICES</span></div>
              <div className="mt-0.5 text-[9px] uppercase tracking-[0.22em] text-slate-500">Operational Engineering</div>
            </div>
          </a>

          {/* Nav */}
          <nav className="hidden md:flex items-center gap-1 rounded-full glass px-1.5 py-1.5">
            {[
              ['Notre Méthode', '#methode'],
              ['Business OS', '#os'],
              ['Nova (IA)', '#nova'],
            ].map(([l, h]) => (
              <a key={l} href={h} className="rounded-full px-3.5 py-1.5 text-[13px] font-medium text-slate-300 transition hover:text-white hover:bg-white/5">{l}</a>
            ))}
          </nav>

          {/* CTA */}
          <div className="hidden md:flex items-center gap-2">
            <BtnPrimary href="#audit" className="!py-2 !px-4 !text-[13px]">Réserver un audit</BtnPrimary>
          </div>

          {/* Mobile toggle */}
          <button onClick={() => setOpen(v => !v)} className="md:hidden glass rounded-full p-2.5">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><path d={open ? "M6 6l12 12M6 18L18 6" : "M4 7h16M4 12h16M4 17h16"} /></svg>
          </button>
        </div>

        {/* Mobile nav */}
        {open && (
          <div className="md:hidden pb-4">
            <div className="glass rounded-2xl p-3 space-y-1">
              {[['Notre Méthode', '#methode'], ['Business OS', '#os'], ['Nova (IA)', '#nova']].map(([l, h]) => (
                <a key={l} href={h} onClick={() => setOpen(false)} className="block rounded-xl px-3 py-2 text-sm font-medium text-slate-200 hover:bg-white/5">{l}</a>
              ))}
              <BtnPrimary href="#audit" className="w-full mt-2">Réserver un audit stratégique</BtnPrimary>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

/* ------------------------------------------------------------------ */
/* Hero                                                               */
/* ------------------------------------------------------------------ */

const HeroDashboard = () => {
  // KPI ticker values
  const tickerItems = [
    { label: 'Leads qualifiés / mois', value: '128', delta: '+42%', color: '#34D399' },
    { label: 'Heures opérationnelles', value: '−51%', delta: 'vs. T-1', color: '#60A5FA' },
    { label: 'SLA Compliance',         value: '98.4%', delta: '↑ 6.1', color: '#A78BFA' },
    { label: 'Tickets auto-résolus',   value: '74%', delta: 'Nova',  color: '#F472B6' },
    { label: 'Marge opérationnelle',   value: '+18 pts', delta: 'YoY', color: '#FBBF24' },
  ];

  return (
    <div className="relative grad-border rounded-2xl glass p-4 sm:p-5 shadow-[0_40px_80px_-30px_rgba(139,92,246,0.45)]">
      {/* window chrome */}
      <div className="flex items-center justify-between border-b border-white/5 pb-3">
        <div className="flex items-center gap-2">
          <span className="h-2.5 w-2.5 rounded-full bg-rose-500/70" />
          <span className="h-2.5 w-2.5 rounded-full bg-amber-400/70" />
          <span className="h-2.5 w-2.5 rounded-full bg-emerald-400/70" />
          <span className="ml-3 font-mono text-[11px] text-slate-500">business-os / overview</span>
        </div>
        <div className="hidden sm:flex items-center gap-2 text-[10px] text-slate-500">
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulseDot" />
          LIVE · synced 2s ago
        </div>
      </div>

      {/* Body */}
      <div className="mt-4 grid grid-cols-12 gap-3">
        {/* Side rail */}
        <div className="col-span-3 hidden md:flex flex-col gap-1.5">
          {[
            { label: 'Pipeline', IconComp: Icon.Workflow, active: true },
            { label: 'Documents', IconComp: Icon.FileSign, active: false },
            { label: 'Facturation', IconComp: Icon.Receipt, active: false },
            { label: 'SOP Library', IconComp: Icon.Book, active: false },
            { label: 'Nova', IconComp: Icon.Bot, active: false },
          ].map(({ label, IconComp, active }) => (
            <div key={label} className={`flex items-center gap-2 rounded-lg px-2.5 py-2 text-[12px] ${active ? 'bg-white/5 text-white' : 'text-slate-400'}`}>
              <IconComp size={14} className={active ? 'text-fuchsia-300' : ''} />
              {label}
            </div>
          ))}
        </div>

        {/* Main */}
        <div className="col-span-12 md:col-span-9 space-y-3">
          {/* KPI ticker */}
          <div className="grid grid-cols-3 gap-2.5">
            <div className="col-span-2 rounded-xl border border-white/5 bg-white/[0.03] p-3.5 overflow-hidden">
              <div className="text-[10px] uppercase tracking-wider text-slate-500">KPI temps réel</div>
              <div className="mt-1 h-[44px] overflow-hidden">
                <div className="animate-ticker">
                  {tickerItems.concat(tickerItems[0]).map((k, i) => (
                    <div key={i} className="h-[44px] flex items-baseline gap-2">
                      <span className="font-display text-2xl font-bold text-white">{k.value}</span>
                      <span className="text-[11px] font-medium" style={{ color: k.color }}>{k.delta}</span>
                      <span className="ml-auto text-[11px] text-slate-500">{k.label}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
            <div className="rounded-xl border border-white/5 bg-white/[0.03] p-3.5">
              <div className="text-[10px] uppercase tracking-wider text-slate-500">Charge mentale</div>
              <div className="mt-2 flex items-baseline gap-1">
                <span className="font-display text-2xl font-bold text-white">−68%</span>
              </div>
              <div className="mt-1.5 h-1.5 rounded-full bg-white/5 overflow-hidden">
                <div className="h-full w-[32%]" style={{ background: 'linear-gradient(90deg, #3B82F6, #EC4899)' }} />
              </div>
            </div>
          </div>

          {/* Pipeline preview */}
          <div className="rounded-xl border border-white/5 bg-white/[0.03] p-3.5">
            <div className="flex items-center justify-between">
              <div className="text-[11px] uppercase tracking-wider text-slate-500">Pipeline clients · semaine 21</div>
              <div className="text-[10px] text-slate-500">62 fiches actives</div>
            </div>
            <div className="mt-3 grid grid-cols-4 gap-2">
              {[
                { l: 'Nova lead',  n: 24, c: '#F472B6' },
                { l: 'Qualifié',   n: 18, c: '#A78BFA' },
                { l: 'Proposition',n: 12, c: '#60A5FA' },
                { l: 'Signé',      n: 8,  c: '#34D399' },
              ].map((s) => (
                <div key={s.l} className="rounded-lg bg-black/30 border border-white/5 p-2.5">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] text-slate-400">{s.l}</span>
                    <span className="font-mono text-[10px] text-slate-500">{s.n}</span>
                  </div>
                  <div className="mt-2 flex gap-1">
                    {Array.from({ length: Math.min(s.n, 8) }).map((_, i) => (
                      <span key={i} className="h-5 flex-1 rounded-sm" style={{ background: `linear-gradient(180deg, ${s.c}55, ${s.c}22)`, border: `1px solid ${s.c}55` }} />
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Mini chart */}
          <div className="rounded-xl border border-white/5 bg-white/[0.03] p-3.5">
            <div className="flex items-center justify-between">
              <div className="text-[11px] uppercase tracking-wider text-slate-500">Tâches automatisées (30j)</div>
              <div className="flex items-center gap-1.5 text-[10px] text-emerald-300"><Icon.Activity size={12}/>+312%</div>
            </div>
            <svg viewBox="0 0 320 70" className="mt-2 w-full h-[70px]">
              <defs>
                <linearGradient id="lg" x1="0" x2="0" y1="0" y2="1">
                  <stop offset="0%" stopColor="#A78BFA" stopOpacity="0.55"/>
                  <stop offset="100%" stopColor="#A78BFA" stopOpacity="0"/>
                </linearGradient>
                <linearGradient id="ls" x1="0" x2="1" y1="0" y2="0">
                  <stop offset="0%" stopColor="#3B82F6"/>
                  <stop offset="60%" stopColor="#8B5CF6"/>
                  <stop offset="100%" stopColor="#EC4899"/>
                </linearGradient>
              </defs>
              <path d="M0,55 L20,52 L40,48 L60,50 L80,42 L100,38 L120,40 L140,30 L160,32 L180,22 L200,24 L220,16 L240,18 L260,10 L280,12 L300,6 L320,4 L320,70 L0,70 Z" fill="url(#lg)"/>
              <path d="M0,55 L20,52 L40,48 L60,50 L80,42 L100,38 L120,40 L140,30 L160,32 L180,22 L200,24 L220,16 L240,18 L260,10 L280,12 L300,6 L320,4" fill="none" stroke="url(#ls)" strokeWidth="1.6"/>
            </svg>
          </div>
        </div>
      </div>

      {/* Floating badge */}
      <div className="absolute -bottom-4 -left-3 md:left-6 glass rounded-xl px-3 py-2 flex items-center gap-2 shadow-xl">
        <Icon.Bot size={16} className="text-fuchsia-300"/>
        <div className="text-[11px] leading-tight">
          <div className="text-white font-semibold">Nova · appel terminé</div>
          <div className="text-slate-400">Lead qualifié → CRM</div>
        </div>
        <span className="ml-2 text-[10px] rounded-full bg-emerald-400/15 text-emerald-300 px-1.5 py-0.5">+1</span>
      </div>
    </div>
  );
};

const Hero = () => {
  return (
    <section className="relative pt-32 pb-20 sm:pt-40 sm:pb-28">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 relative">
        <div className="grid lg:grid-cols-12 gap-12 items-center">
          {/* Copy */}
          <div className="lg:col-span-7">
            <div className="reveal">
              <Pill>Business OS · Built for Small Business Owners</Pill>
            </div>
            <h1 className="reveal mt-6 font-display text-[44px] sm:text-6xl lg:text-[72px] leading-[1.02] font-bold tracking-tight text-white" style={{ textWrap: 'balance' }}>
              Arrêtez de travailler <span className="text-slate-400">DANS</span><br/>
              votre entreprise.<br/>
              <span className="text-mesh">Travaillez SUR elle.</span>
            </h1>
            <p className="reveal mt-6 max-w-xl text-[17px] leading-relaxed text-slate-400">
              Nous structurons et automatisons les opérations des Small Business Owners.
              Déployez votre propre <span className="text-slate-200 font-medium">Business OS</span> et libérez-vous des tâches manuelles, des oublis et de la charge mentale.
            </p>

            <div className="reveal mt-8 flex flex-col sm:flex-row gap-3">
              <BtnPrimary href="#audit">Lancer l'automatisation</BtnPrimary>
              <BtnGhost href="#os">Découvrir nos solutions</BtnGhost>
            </div>

            {/* Trust strip */}
            <div className="reveal mt-10 flex flex-wrap items-center gap-x-8 gap-y-3">
              <div className="flex items-center gap-2 text-slate-400 text-[12px]">
                <Icon.Shield size={14} className="text-emerald-400"/>
                Conforme RGPD · données européennes
              </div>
              <div className="flex items-center gap-2 text-slate-400 text-[12px]">
                <Icon.Zap size={14} className="text-amber-300"/>
                Déploiement sous 21 jours
              </div>
              <div className="flex items-center gap-2 text-slate-400 text-[12px]">
                <Icon.Check size={14} className="text-fuchsia-300"/>
                ROI moyen 4.2× en 6 mois
              </div>
            </div>
          </div>

          {/* Dashboard mock */}
          <div className="lg:col-span-5 reveal">
            <div className="relative">
              <HeroDashboard />
              {/* glow */}
              <div className="absolute -inset-6 -z-10 rounded-3xl" style={{ background: 'radial-gradient(circle at 60% 40%, rgba(139,92,246,0.35), transparent 60%)' }}/>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

/* ------------------------------------------------------------------ */
/* Stack marquee                                                      */
/* ------------------------------------------------------------------ */

const Marquee = () => {
  const tools = ['Notion', 'Airtable', 'Make.com', 'n8n', 'Slack', 'Stripe', 'HubSpot', 'Pennylane', 'Webflow', 'OpenAI', 'Twilio', 'Calendly', 'Pipedrive', 'Zapier'];
  return (
    <section aria-label="Stack technique" className="border-y border-white/5 bg-ink-950/60">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 py-7">
        <div className="flex items-center gap-6">
          <div className="hidden sm:block text-[11px] uppercase tracking-[0.18em] text-slate-500 shrink-0">
            Stack opérationnelle · orchestrée
          </div>
          <div className="marquee flex-1 overflow-hidden">
            <div className="marquee-track flex w-max gap-10 text-slate-400">
              {[...tools, ...tools].map((t, i) => (
                <span key={i} className="font-display text-lg font-medium whitespace-nowrap">{t}</span>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

/* ------------------------------------------------------------------ */
/* 3 Piliers (Bento)                                                  */
/* ------------------------------------------------------------------ */

const PillarCard = ({ tag, title, desc, icon: IconC, accent, children, big = false }: { tag: string; title: string; desc: string; icon: any; accent: string; children?: React.ReactNode; big?: boolean }) => {
  const ref = useSpotlight();
  return (
    <div ref={ref} className={`spot glass glass-hover rounded-3xl p-7 sm:p-8 flex flex-col ${big ? 'lg:row-span-2' : ''}`}>
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl border border-white/10" style={{ background: `linear-gradient(135deg, ${accent}33, ${accent}11)` }}>
          <IconC size={18} style={{ color: accent }}/>
        </div>
        <span className="text-[10px] uppercase tracking-[0.22em] text-slate-500">{tag}</span>
      </div>
      <h3 className="mt-5 font-display text-2xl sm:text-[26px] font-semibold text-white" style={{ textWrap: 'balance' }}>{title}</h3>
      <p className="mt-3 text-[14.5px] leading-relaxed text-slate-400">{desc}</p>
      {children && <div className="mt-6">{children}</div>}
    </div>
  );
};

const NoCodeVisual = () => (
  <div className="rounded-xl border border-white/5 bg-black/30 p-4 font-mono text-[11px] text-slate-400 space-y-1.5">
    <div className="flex items-center gap-2 text-slate-500"><Icon.Database size={12}/> clients.db</div>
    <div className="grid grid-cols-3 gap-1.5 text-[10px]">
      {[
        ['Acme Inc.',  'Signé',     '#34D399'],
        ['Belluci',    'Proposition','#A78BFA'],
        ['Cortez SAS', 'Lead',      '#60A5FA'],
        ['Dupont &Co', 'Signé',     '#34D399'],
        ['Eden Café',  'Lead',      '#60A5FA'],
        ['Floralis',   'Proposition','#A78BFA'],
      ].map(([n, s, c], i) => (
        <div key={i} className="rounded bg-white/5 px-2 py-1.5">
          <div className="text-slate-200 truncate">{n}</div>
          <div className="flex items-center gap-1 mt-0.5"><span className="h-1 w-1 rounded-full" style={{ background: c }}/><span className="text-slate-500">{s}</span></div>
        </div>
      ))}
    </div>
  </div>
);

const WorkflowVisual = () => (
  <div className="rounded-xl border border-white/5 bg-black/30 p-4">
    <div className="flex items-center justify-between text-[10px] uppercase tracking-wider text-slate-500">
      <span>Workflow · onboarding client</span>
      <span className="text-emerald-300">● actif</span>
    </div>
    <div className="mt-3 flex items-center gap-1.5 text-[10px]">
      {[
        { l: 'Form', c: '#60A5FA' },
        { l: 'CRM',  c: '#A78BFA' },
        { l: 'Mail', c: '#F472B6' },
        { l: 'Sign', c: '#FBBF24' },
        { l: 'OS',   c: '#34D399' },
      ].map((s, i, a) => (
        <Fragment key={s.l}>
          <div className="rounded-md border px-2 py-1.5 flex-1 text-center" style={{ borderColor: s.c + '55', background: s.c + '14', color: s.c }}>{s.l}</div>
          {i < a.length - 1 && <Icon.ArrowRight size={10} className="text-slate-600 shrink-0"/>}
        </Fragment>
      ))}
    </div>
    <div className="mt-3 grid grid-cols-3 gap-1.5 text-[10px] text-slate-500">
      <div className="rounded bg-white/5 px-1.5 py-1">12 runs/j</div>
      <div className="rounded bg-white/5 px-1.5 py-1">0 erreur</div>
      <div className="rounded bg-white/5 px-1.5 py-1">~4.2s</div>
    </div>
  </div>
);

const FrameworkVisual = () => (
  <div className="rounded-xl border border-white/5 bg-black/30 p-4">
    <div className="text-[10px] uppercase tracking-wider text-slate-500">Framework · 90 jours</div>
    <div className="mt-3 space-y-1.5">
      {[
        ['Diagnostic', 100, '#60A5FA'],
        ['Architecture OS', 76, '#A78BFA'],
        ['Déploiement Nova', 48, '#F472B6'],
        ['Optimisation continue', 22, '#FBBF24'],
      ].map(([l, p, c]) => (
        <div key={l as string}>
          <div className="flex justify-between text-[10.5px] text-slate-400"><span>{l as string}</span><span className="font-mono text-slate-500">{p as number}%</span></div>
          <div className="mt-1 h-1 rounded-full bg-white/5 overflow-hidden">
            <div className="h-full rounded-full" style={{ width: `${p as number}%`, background: c as string }}/>
          </div>
        </div>
      ))}
    </div>
  </div>
);

const Piliers = () => (
  <section id="methode" className="relative py-24 sm:py-32">
    <div className="mx-auto max-w-7xl px-6 lg:px-10">
      <div className="max-w-3xl reveal">
        <SectionTag>La Méthode OMK</SectionTag>
        <h2 className="mt-5 font-display text-4xl sm:text-5xl lg:text-[56px] font-bold leading-[1.05] text-white" style={{ textWrap: 'balance' }}>
          Trois piliers. Un seul objectif :<br/>
          <span className="text-mesh">une entreprise qui tourne sans vous.</span>
        </h2>
        <p className="mt-5 max-w-xl text-slate-400 text-[15.5px]">
          Pas de slides, pas de PDF de recommandations. Nous livrons des systèmes, déployés, branchés, mesurés.
        </p>
      </div>

      <div className="reveal mt-14 grid lg:grid-cols-3 gap-5">
        <PillarCard tag="01 · Foundation" title="Templates No-Code sur mesure"
          desc="Bases de données, CRM, dashboards et portails clients. Tout ce qui devrait vivre dans Excel ou dans votre tête, modélisé, connecté, accessible."
          icon={Icon.Database} accent="#60A5FA">
          <NoCodeVisual/>
        </PillarCard>
        <PillarCard tag="02 · Engine" title="Workflows d'automatisation"
          desc="Élimination chirurgicale des processus chronophages. Devis, relances, onboarding, facturation, support : tout s'exécute sans vous."
          icon={Icon.Workflow} accent="#A78BFA">
          <WorkflowVisual/>
        </PillarCard>
        <PillarCard tag="03 · Compass" title="Frameworks stratégiques"
          desc="Méthodologies agiles pour scaler sans friction. Cadences, OKR, SOP et indicateurs de pilotage installés dans votre OS."
          icon={Icon.Layers} accent="#F472B6">
          <FrameworkVisual/>
        </PillarCard>
      </div>
    </div>
  </section>
);

/* ------------------------------------------------------------------ */
/* Business OS                                                        */
/* ------------------------------------------------------------------ */

const ModuleCard = ({ icon: IconC, title, sub, accent, meta }: { icon: any; title: string; sub: string; accent: string; meta: [string, string] }) => {
  const ref = useSpotlight();
  return (
    <div ref={ref} className="spot glass glass-hover rounded-2xl p-5 group">
      <div className="flex items-start justify-between">
        <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10" style={{ background: `linear-gradient(135deg, ${accent}38, transparent)` }}>
          <IconC size={16} style={{ color: accent }}/>
        </div>
        <Icon.ArrowUpRight size={14} className="text-slate-500 transition group-hover:text-white group-hover:-translate-y-0.5 group-hover:translate-x-0.5"/>
      </div>
      <div className="mt-4">
        <div className="font-display text-[17px] font-semibold text-white">{title}</div>
        <div className="mt-1 text-[12.5px] text-slate-400 leading-relaxed">{sub}</div>
      </div>
      <div className="mt-5 flex items-center justify-between border-t border-white/5 pt-3 text-[10.5px]">
        <span className="text-slate-500">{meta[0]}</span>
        <span className="font-mono" style={{ color: accent }}>{meta[1]}</span>
      </div>
    </div>
  );
};

const KPIStat = ({ label, value, sub, accent }: { label: string; value: string; sub: string; accent: string }) => (
  <div className="glass rounded-2xl p-6">
    <div className="text-[10px] uppercase tracking-[0.18em] text-slate-500">{label}</div>
    <div className="mt-3 flex items-baseline gap-2">
      <span className="font-display text-4xl sm:text-5xl font-bold text-white">{value}</span>
      <span className="text-xs font-medium" style={{ color: accent }}>{sub}</span>
    </div>
  </div>
);

const BusinessOS = () => (
  <section id="os" className="relative py-24 sm:py-32 border-t border-white/5">
    {/* ambient */}
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-driftSlow" style={{ width: 600, height: 600, top: 100, left: -180, background: 'radial-gradient(circle, #3B82F6 0%, transparent 60%)', opacity: 0.18 }}/>
      <div className="blob animate-drift"     style={{ width: 500, height: 500, bottom: 80, right: -120, background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.18 }}/>
    </div>

    <div className="mx-auto max-w-7xl px-6 lg:px-10">
      <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8">
        <div className="max-w-2xl reveal">
          <SectionTag>Le cœur du réacteur</SectionTag>
          <h2 className="mt-5 font-display text-4xl sm:text-5xl lg:text-[56px] font-bold leading-[1.05] text-white" style={{ textWrap: 'balance' }}>
            Le <span className="text-mesh">Business OS</span>.<br/>Votre suite logicielle, livrée clé en main.
          </h2>
        </div>
        <p className="max-w-md text-slate-400 text-[15px] reveal">
          Une interface unifiée pour piloter clients, documents, finance et savoir-faire.
          Conçue sur des outils no-code que <em>vos équipes savent déjà utiliser</em>.
        </p>
      </div>

      {/* Modules grid */}
      <div className="reveal mt-14 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <ModuleCard icon={Icon.Workflow} title="Clients Pipeline"
          sub="CRM no-code, scoring, relances automatisées et synchro avec Nova."
          accent="#60A5FA" meta={['Module', 'v3.1']}/>
        <ModuleCard icon={Icon.FileSign} title="Gestion documentaire & e-signature"
          sub="Génération, envoi, signature et archivage. Contrats prêts en 4 minutes."
          accent="#A78BFA" meta={['Module', 'v2.4']}/>
        <ModuleCard icon={Icon.Receipt} title="Facturation automatisée"
          sub="Devis → facture → relance → encaissement. Rapprochement bancaire inclus."
          accent="#F472B6" meta={['Module', 'v2.0']}/>
        <ModuleCard icon={Icon.Book} title="SOP Library"
          sub="Toute la mémoire opérationnelle de l'entreprise. Vidéos, checklists, garde-fous."
          accent="#FBBF24" meta={['Module', 'v1.7']}/>
      </div>

      {/* KPI band */}
      <div className="reveal mt-10 grid grid-cols-1 md:grid-cols-3 gap-4">
        <KPIStat label="SLA Compliance" value="98.4%" sub="↑ 6.1 pts" accent="#34D399"/>
        <KPIStat label="Temps de traitement" value="−51%" sub="vs. avant OMK" accent="#A78BFA"/>
        <KPIStat label="Déploiement moyen" value="21j" sub="signature → live" accent="#F472B6"/>
      </div>
    </div>
  </section>
);

/* ------------------------------------------------------------------ */
/* Nova                                                               */
/* ------------------------------------------------------------------ */

const Waveform = () => (
  <div className="flex items-center gap-1 h-12">
    {Array.from({ length: 32 }).map((_, i) => (
      <span key={i} className="wave-bar w-1 rounded-full"
        style={{
          height: `${20 + (i % 5) * 14}px`,
          background: `linear-gradient(180deg, #60A5FA, #A78BFA ${50 + (i%3)*10}%, #F472B6)`,
          animationDelay: `${(i * 60) % 800}ms`,
        }}/>
    ))}
  </div>
);

const NovaCall = () => (
  <div className="relative grad-border rounded-3xl glass p-6">
    {/* Header */}
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-3">
        <div className="relative flex h-10 w-10 items-center justify-center rounded-full" style={{ background: 'linear-gradient(135deg, #8B5CF6, #EC4899)' }}>
          <Icon.Bot size={18} className="text-white"/>
          <span className="absolute -bottom-0.5 -right-0.5 h-3 w-3 rounded-full bg-emerald-400 ring-2 ring-ink-900"/>
        </div>
        <div>
          <div className="font-display font-semibold text-white text-[15px]">Nova</div>
          <div className="text-[11px] text-slate-400">Appel entrant · 02:17</div>
        </div>
      </div>
      <div className="flex items-center gap-2 text-[10px] text-slate-400 rounded-full glass px-2.5 py-1">
        <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulseDot"/>
        En ligne
      </div>
    </div>

    {/* Waveform */}
    <div className="mt-6 rounded-2xl border border-white/5 bg-black/30 p-5">
      <Waveform/>
      <div className="mt-3 flex items-center justify-between text-[10.5px] font-mono text-slate-500">
        <span>00:14</span>
        <span>Sentiment · positif</span>
        <span>02:17</span>
      </div>
    </div>

    {/* Transcript */}
    <div className="mt-4 space-y-2.5">
      <div className="flex gap-2">
        <span className="text-[10px] font-mono text-fuchsia-300/80 mt-0.5">NOVA</span>
        <p className="text-[13px] text-slate-200 leading-relaxed flex-1">
          « Bonjour Madame Léger, je suis Nova, l'assistante d'OMK. Vous cherchez à structurer la facturation de votre cabinet ? »
        </p>
      </div>
      <div className="flex gap-2">
        <span className="text-[10px] font-mono text-slate-500 mt-0.5">CLIENT</span>
        <p className="text-[13px] text-slate-400 leading-relaxed flex-1">
          « Oui, on perd environ deux jours par semaine sur les relances et les devis. »
        </p>
      </div>
      <div className="flex gap-2">
        <span className="text-[10px] font-mono text-fuchsia-300/80 mt-0.5">NOVA</span>
        <p className="text-[13px] text-slate-200 leading-relaxed flex-1">
          « Compris. Je bloque un audit stratégique avec Omar mardi 14h ? Vous recevrez le brief Notion juste après. »
        </p>
      </div>
    </div>

    {/* Action chips */}
    <div className="mt-5 grid grid-cols-3 gap-2 text-[11px]">
      <div className="rounded-lg border border-emerald-400/20 bg-emerald-400/5 px-2.5 py-2 text-emerald-300 flex items-center gap-1.5"><Icon.Check size={12}/> Lead qualifié</div>
      <div className="rounded-lg border border-blue-400/20 bg-blue-400/5 px-2.5 py-2 text-blue-300 flex items-center gap-1.5"><Icon.Workflow size={12}/> Push CRM</div>
      <div className="rounded-lg border border-fuchsia-400/20 bg-fuchsia-400/5 px-2.5 py-2 text-fuchsia-300 flex items-center gap-1.5"><Icon.Sparkles size={12}/> RDV 14h</div>
    </div>
  </div>
);

const AgentRow = ({ icon: IconC, name, role, accent }: { icon: any; name: string; role: string; accent: string }) => (
  <div className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/[0.025] hover:bg-white/[0.05] transition p-3">
    <div className="flex h-9 w-9 items-center justify-center rounded-lg" style={{ background: `${accent}22`, color: accent }}>
      <IconC size={15}/>
    </div>
    <div className="min-w-0 flex-1">
      <div className="text-[13px] font-semibold text-white">{name}</div>
      <div className="text-[11.5px] text-slate-400">{role}</div>
    </div>
    <span className="text-[10px] font-mono text-slate-500">ONLINE</span>
  </div>
);

const Nova = () => (
  <section id="nova" className="relative py-24 sm:py-32 border-t border-white/5">
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-drift" style={{ width: 720, height: 720, top: 40, right: -240, background: 'radial-gradient(circle, #8B5CF6 0%, transparent 60%)', opacity: 0.28 }}/>
      <div className="blob animate-driftSlow" style={{ width: 520, height: 520, bottom: 0, left: -160, background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.22 }}/>
    </div>

    <div className="mx-auto max-w-7xl px-6 lg:px-10">
      <div className="grid lg:grid-cols-12 gap-12 items-start">
        {/* Copy */}
        <div className="lg:col-span-6 reveal">
          <SectionTag>L'avant-garde · Flotte IA</SectionTag>
          <h2 className="mt-5 font-display text-4xl sm:text-5xl lg:text-[56px] font-bold leading-[1.05] text-white" style={{ textWrap: 'balance' }}>
            Rencontrez <span className="text-mesh">Nova</span>.<br/>
            Votre agent de qualification <span className="text-slate-400">24/7</span>.
          </h2>
          <p className="mt-6 text-[16px] leading-relaxed text-slate-400 max-w-xl">
            Nova décroche, qualifie, répond aux objections et synchronise chaque appel avec votre CRM.
            Pas de script rigide : un agent vocal entraîné sur <em>votre</em> méthode commerciale et votre <em>SOP Library</em>.
          </p>

          <div className="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-3 max-w-xl">
            {[
              ['24/7', 'disponibilité'],
              ['<400ms', 'latence vocale'],
              ['7 langues', 'natives'],
            ].map(([v, l]) => (
              <div key={l} className="rounded-xl border border-white/8 bg-white/[0.03] p-3">
                <div className="font-display text-xl font-bold text-white">{v}</div>
                <div className="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">{l}</div>
              </div>
            ))}
          </div>

          {/* Agents back-office */}
          <div className="mt-10">
            <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-3">+ Flotte back-office</div>
            <div className="grid sm:grid-cols-2 gap-2.5">
              <AgentRow icon={Icon.Inbox}      name="Intake-Agent"     role="Trie les emails et tickets entrants"        accent="#60A5FA"/>
              <AgentRow icon={Icon.Languages}  name="Translator-Agent" role="Traduit contrats et supports en temps réel" accent="#A78BFA"/>
              <AgentRow icon={Icon.FileSign}   name="DocuFlow-Agent"   role="Génère devis, contrats, relances signées"    accent="#F472B6"/>
              <AgentRow icon={Icon.Wallet}     name="Finance-Flow"     role="Réconcilie factures, banque et compta"       accent="#FBBF24"/>
            </div>
          </div>

          <div className="mt-10 flex gap-3">
            <BtnPrimary href="#audit">Écouter une démo Nova</BtnPrimary>
            <BtnGhost href="#os">Voir l'architecture</BtnGhost>
          </div>
        </div>

        {/* Call mock */}
        <div className="lg:col-span-6 reveal lg:sticky lg:top-24">
          <NovaCall/>
        </div>
      </div>
    </div>
  </section>
);

/* ------------------------------------------------------------------ */
/* CTA + Footer                                                       */
/* ------------------------------------------------------------------ */

const FinalCTA = () => (
  <section id="audit" className="relative py-24 sm:py-32 border-t border-white/5">
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-drift"     style={{ width: 700, height: 700, top: -100, left: '20%', background: 'radial-gradient(circle, #3B82F6 0%, transparent 60%)', opacity: 0.25 }}/>
      <div className="blob animate-driftSlow" style={{ width: 600, height: 600, bottom: -120, right: '15%', background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.22 }}/>
    </div>

    <div className="mx-auto max-w-5xl px-6 lg:px-10 text-center reveal">
      <SectionTag>Prêt à reprendre le contrôle ?</SectionTag>
      <h2 className="mt-6 font-display text-4xl sm:text-5xl lg:text-[64px] font-bold leading-[1.04] text-white" style={{ textWrap: 'balance' }}>
        Un diagnostic de 45 minutes.<br/>
        <span className="text-mesh">Une roadmap exploitable.</span>
      </h2>
      <p className="mt-5 text-slate-400 max-w-xl mx-auto text-[15.5px]">
        Nous identifions les 3 plus grosses fuites opérationnelles de votre business et chiffrons l'impact d'un Business OS. Sans engagement.
      </p>
      
      <AuditForm />
      
      <div className="mt-6 text-[12px] text-slate-500">Réponse sous 24h · Visio · Aucun deck commercial</div>
    </div>
  </section>
);

const Footer = () => (
  <footer className="relative border-t border-white/5 bg-ink-950/80">
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-14">
      <div className="grid grid-cols-2 md:grid-cols-5 gap-10">
        <div className="col-span-2">
          <a href="#" className="flex items-center gap-2.5">
            <span className="relative flex h-8 w-8 items-center justify-center rounded-lg" style={{ background: 'linear-gradient(135deg, #3B82F6, #8B5CF6 55%, #EC4899)' }}>
              <span className="absolute inset-[1px] rounded-[7px] bg-ink-950 flex items-center justify-center">
                <span className="font-display text-[15px] font-bold text-mesh">O</span>
              </span>
            </span>
            <div className="font-display text-[15px] font-bold tracking-tight text-white">OMK SERVICES</div>
          </a>
          <p className="mt-4 text-[13px] text-slate-400 max-w-sm leading-relaxed">
            Ingénierie opérationnelle pour Small Business Owners. Nous transformons les entreprises manuelles en Self-Operating Businesses.
          </p>
          <div className="mt-6 flex items-center gap-2">
            <a href="#" aria-label="LinkedIn" className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Linkedin size={15}/></a>
            <a href="#" aria-label="Twitter"  className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Twitter size={15}/></a>
            <a href="#" aria-label="Github"   className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Github size={15}/></a>
          </div>
        </div>

        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Produit</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#os" className="hover:text-white">Business OS</a></li>
            <li><a href="#nova" className="hover:text-white">Nova IA</a></li>
            <li><a href="#methode" className="hover:text-white">Méthode</a></li>
            <li><a href="#" className="hover:text-white">Tarifs</a></li>
          </ul>
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Société</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#" className="hover:text-white">À propos</a></li>
            <li><a href="#" className="hover:text-white">Cas clients</a></li>
            <li><a href="#" className="hover:text-white">Carrières</a></li>
            <li><a href="#" className="hover:text-white">Contact</a></li>
          </ul>
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Légal</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#" className="hover:text-white">Confidentialité</a></li>
            <li><a href="#" className="hover:text-white">CGU / CGV</a></li>
            <li><a href="#" className="hover:text-white">Sécurité</a></li>
            <li><a href="#" className="hover:text-white">RGPD</a></li>
          </ul>
        </div>
      </div>

      <div className="mt-12 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-t border-white/5 pt-6">
        <div className="text-[12px] text-slate-500">
          © 2026 OMK SERVICES — Empowering Small Business Owners.
        </div>
        <div className="flex items-center gap-2 text-[11px] text-slate-500">
          <Icon.Globe size={13}/> Paris · Casablanca · Remote
        </div>
      </div>
    </div>
  </footer>
);

/* ------------------------------------------------------------------ */
/* App                                                                */
/* ------------------------------------------------------------------ */

export default function Home() {
  useReveal();
  return (
    <div className="relative">
      <MeshBackdrop/>
      <Header/>
      <main className="relative">
        <Hero/>
        <Marquee/>
        <Piliers/>
        <BusinessOS/>
        <Nova/>
        <FinalCTA/>
      </main>
      <Footer/>
    </div>
  );
}
