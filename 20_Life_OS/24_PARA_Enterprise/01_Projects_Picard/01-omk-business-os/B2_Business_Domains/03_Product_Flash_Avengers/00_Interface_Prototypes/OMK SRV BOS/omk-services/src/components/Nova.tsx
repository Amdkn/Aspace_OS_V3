"use client";

import React from "react";
import { Icon } from "@/components/Icons";
import { SectionTag, BtnPrimary, BtnGhost } from "./Base";

const Waveform = () => (
  <div className="flex items-center gap-1 h-12">
    {Array.from({ length: 32 }).map((_, i) => (
      <span key={i} className="wave-bar w-1 rounded-full"
        style={{
          height: `${20 + (i % 5) * 14}px`,
          background: `linear-gradient(180deg, #60A5FA, #A78BFA ${50 + (i%3)*10}%, #F472B6)`,
          animationDelay: `${(i * 60) % 800}ms`,
        } as any}/>
    ))}
  </div>
);

const NovaCall = () => (
  <div className="relative grad-border rounded-3xl glass p-6">
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

    <div className="mt-6 rounded-2xl border border-white/5 bg-black/30 p-5">
      <Waveform/>
      <div className="mt-3 flex items-center justify-between text-[10.5px] font-mono text-slate-500">
        <span>00:14</span>
        <span>Sentiment · positif</span>
        <span>02:17</span>
      </div>
    </div>

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

    <div className="mt-5 grid grid-cols-3 gap-2 text-[11px]">
      <div className="rounded-lg border border-emerald-400/20 bg-emerald-400/5 px-2.5 py-2 text-emerald-300 flex items-center gap-1.5"><Icon.Check size={12}/> Lead qualifié</div>
      <div className="rounded-lg border border-blue-400/20 bg-blue-400/5 px-2.5 py-2 text-blue-300 flex items-center gap-1.5"><Icon.Workflow size={12}/> Push CRM</div>
      <div className="rounded-lg border border-fuchsia-400/20 bg-fuchsia-400/5 px-2.5 py-2 text-fuchsia-300 flex items-center gap-1.5"><Icon.Sparkles size={12}/> RDV 14h</div>
    </div>
  </div>
);

const AgentRow = ({ icon: IconC, name, role, accent }: any) => (
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

export const Nova = () => (
  <section id="nova" className="relative py-24 sm:py-32 border-t border-white/5">
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-drift" style={{ width: 720, height: 720, top: 40, right: -240, background: 'radial-gradient(circle, #8B5CF6 0%, transparent 60%)', opacity: 0.28 } as any}/>
      <div className="blob animate-driftSlow" style={{ width: 520, height: 520, bottom: 0, left: -160, background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.22 } as any}/>
    </div>

    <div className="mx-auto max-w-7xl px-6 lg:px-10">
      <div className="grid lg:grid-cols-12 gap-12 items-start">
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

        <div className="lg:col-span-6 reveal lg:sticky lg:top-24">
          <NovaCall/>
        </div>
      </div>
    </div>
  </section>
);

export const FinalCTA = () => (
  <section id="audit" className="relative py-24 sm:py-32 border-t border-white/5">
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-drift"     style={{ width: 700, height: 700, top: -100, left: '20%', background: 'radial-gradient(circle, #3B82F6 0%, transparent 60%)', opacity: 0.25 } as any}/>
      <div className="blob animate-driftSlow" style={{ width: 600, height: 600, bottom: -120, right: '15%', background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.22 } as any}/>
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
      <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
        <BtnPrimary>Réserver un audit stratégique</BtnPrimary>
        <BtnGhost href="#os">Comparer nos offres</BtnGhost>
      </div>
      <div className="mt-6 text-[12px] text-slate-500">Réponse sous 24h · Visio · Aucun deck commercial</div>
    </div>
  </section>
);
