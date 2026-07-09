"use client";

import React from "react";
import { Icon } from "@/components/Icons";
import { SectionTag } from "./Base";
import { useSpotlight } from "@/lib/hooks";

const ModuleCard = ({ icon: IconC, title, sub, accent, meta }: any) => {
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

const KPIStat = ({ label, value, sub, accent }: any) => (
  <div className="glass rounded-2xl p-6">
    <div className="text-[10px] uppercase tracking-[0.18em] text-slate-500">{label}</div>
    <div className="mt-3 flex items-baseline gap-2">
      <span className="font-display text-4xl sm:text-5xl font-bold text-white">{value}</span>
      <span className="text-xs font-medium" style={{ color: accent }}>{sub}</span>
    </div>
  </div>
);

export const BusinessOS = () => (
  <section id="os" className="relative py-24 sm:py-32 border-t border-white/5">
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <div className="blob animate-driftSlow" style={{ width: 600, height: 600, top: 100, left: -180, background: 'radial-gradient(circle, #3B82F6 0%, transparent 60%)', opacity: 0.18 } as any}/>
      <div className="blob animate-drift"     style={{ width: 500, height: 500, bottom: 80, right: -120, background: 'radial-gradient(circle, #EC4899 0%, transparent 60%)', opacity: 0.18 } as any}/>
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

      <div className="reveal mt-10 grid grid-cols-1 md:grid-cols-3 gap-4">
        <KPIStat label="SLA Compliance" value="98.4%" sub="↑ 6.1 pts" accent="#34D399"/>
        <KPIStat label="Temps de traitement" value="−51%" sub="vs. avant OMK" accent="#A78BFA"/>
        <KPIStat label="Déploiement moyen" value="21j" sub="signature → live" accent="#F472B6"/>
      </div>
    </div>
  </section>
);
