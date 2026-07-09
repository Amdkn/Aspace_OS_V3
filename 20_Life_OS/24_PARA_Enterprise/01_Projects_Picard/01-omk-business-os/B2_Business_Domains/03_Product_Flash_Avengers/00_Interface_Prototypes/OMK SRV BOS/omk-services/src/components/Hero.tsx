"use client";

import React from "react";
import { Icon } from "@/components/Icons";
import { useSpotlight } from "@/lib/hooks";

export const HeroDashboard = () => {
  const tickerItems = [
    { label: 'Leads qualifiés / mois', value: '128', delta: '+42%', color: '#34D399' },
    { label: 'Heures opérationnelles', value: '−51%', delta: 'vs. T-1', color: '#60A5FA' },
    { label: 'SLA Compliance',         value: '98.4%', delta: '↑ 6.1', color: '#A78BFA' },
    { label: 'Tickets auto-résolus',   value: '74%', delta: 'Nova',  color: '#F472B6' },
    { label: 'Marge opérationnelle',   value: '+18 pts', delta: 'YoY', color: '#FBBF24' },
  ];

  return (
    <div className="relative grad-border rounded-2xl glass p-4 sm:p-5 shadow-[0_40px_80px_-30px_rgba(139,92,246,0.45)]">
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

      <div className="mt-4 grid grid-cols-12 gap-3">
        <div className="col-span-3 hidden md:flex flex-col gap-1.5">
          {[
            ['Pipeline', Icon.Workflow, true],
            ['Documents', Icon.FileSign],
            ['Facturation', Icon.Receipt],
            ['SOP Library', Icon.Book],
            ['Nova', Icon.Bot],
          ].map(([l, I, active]: any) => (
            <div key={l} className={`flex items-center gap-2 rounded-lg px-2.5 py-2 text-[12px] ${active ? 'bg-white/5 text-white' : 'text-slate-400'}`}>
              <I size={14} className={active ? 'text-fuchsia-300' : ''} />
              {l}
            </div>
          ))}
        </div>

        <div className="col-span-12 md:col-span-9 space-y-3">
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

export const Hero = () => {
  return (
    <section className="relative pt-32 pb-20 sm:pt-40 sm:pb-28">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 relative">
        <div className="grid lg:grid-cols-12 gap-12 items-center">
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

          <div className="lg:col-span-5 reveal">
            <div className="relative">
              <HeroDashboard />
              <div className="absolute -inset-6 -z-10 rounded-3xl" style={{ background: 'radial-gradient(circle at 60% 40%, rgba(139,92,246,0.35), transparent 60%)' }}/>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

const Pill = ({ children }: { children: React.ReactNode }) => (
  <span className="inline-flex items-center gap-2 rounded-full glass px-3 py-1.5 text-xs font-medium text-slate-300">
    <span className="relative flex h-1.5 w-1.5">
      <span className="absolute inset-0 rounded-full bg-fuchsia-400 animate-pulseDot" />
      <span className="relative rounded-full bg-fuchsia-400 h-1.5 w-1.5" />
    </span>
    {children}
  </span>
);

const BtnPrimary = ({ children, className = '', href = '#audit' }: { children: React.ReactNode, className?: string, href?: string }) => (
  <a href={href} className={`btn-mesh group inline-flex items-center justify-center gap-2 rounded-full px-5 py-3 text-sm font-semibold text-white transition hover:brightness-110 ${className}`}>
    <span className="relative z-10 flex items-center gap-2">
      {children}
      <Icon.ArrowRight size={16} className="transition group-hover:translate-x-0.5" />
    </span>
  </a>
);

const BtnGhost = ({ children, className = '', href = '#methode' }: { children: React.ReactNode, className?: string, href?: string }) => (
  <a href={href} className={`inline-flex items-center justify-center gap-2 rounded-full glass px-5 py-3 text-sm font-semibold text-slate-200 transition hover:border-white/25 hover:bg-white/10 ${className}`}>
    {children}
  </a>
);
