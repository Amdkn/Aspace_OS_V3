"use client";

import React from "react";
import { Icon } from "@/components/Icons";
import { SectionTag, BtnPrimary, BtnGhost } from "./Base";
import { useSpotlight } from "@/lib/hooks";

export const Marquee = () => {
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

const PillarCard = ({ tag, title, desc, icon: IconC, accent, children, big = false }: any) => {
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
        <React.Fragment key={s.l}>
          <div className="rounded-md border px-2 py-1.5 flex-1 text-center" style={{ borderColor: s.c + '55', background: s.c + '14', color: s.c }}>{s.l}</div>
          {i < a.length - 1 && <Icon.ArrowRight size={10} className="text-slate-600 shrink-0"/>}
        </React.Fragment>
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
      ].map(([l, p, c]: any) => (
        <div key={l}>
          <div className="flex justify-between text-[10.5px] text-slate-400"><span>{l}</span><span className="font-mono text-slate-500">{p}%</span></div>
          <div className="mt-1 h-1 rounded-full bg-white/5 overflow-hidden">
            <div className="h-full rounded-full" style={{ width: `${p}%`, background: c }}/>
          </div>
        </div>
      ))}
    </div>
  </div>
);

export const Piliers = () => (
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
