"use client";

import React from 'react';
import { ScanLine, FilePen, CircleDollarSign, Check, HandCoins, ArrowRight } from 'lucide-react';
import { Icon } from './Icon';

export function Methode() {
  const steps = [
    { num: "I", title: "Audit & Localisation", sub: "Nous identifions les fonds.", desc: "Croisement de votre dossier avec le Clerk of Courts. Confirmation de l'excédent.", time: "24-48h", icon: ScanLine, tasks: ["Vérification dossier", "Lettre d'éligibilité"] },
    { num: "II", title: "Assemblage Légal", sub: "Mandat avocats locaux.", desc: "Nos avocats plaident à votre place. Vous ne mettez pas un pied au tribunal.", time: "4-8 semaines", icon: FilePen, tasks: ["Motion to disburse", "Audience programmée"] },
    { num: "III", title: "Décaissement", sub: "Le juge libère les fonds.", desc: "Le chèque du Clerk est émis à votre nom. Rémunération au succès.", time: "2-3 semaines", icon: CircleDollarSign, tasks: ["Order signed", "Solde versé"] },
  ];
  return (
    <section id="methode" className="border-b border-slate-800/70 bg-[#040818] relative">
      <div className="absolute inset-0 grid-bg opacity-40 pointer-events-none"></div>
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20 lg:py-28 relative">
        <h2 className="font-display font-medium text-[34px] lg:text-[46px] leading-[1.05] text-white mb-16">Vous signez une fois.<br/><span className="text-slate-500">Nous orchestrons le reste.</span></h2>
        <div className="grid lg:grid-cols-3 gap-px bg-slate-800/70 border border-slate-800/70 rounded-sm overflow-hidden">
          {steps.map((s, i) => (
            <div key={i} className="bg-[#040818] p-8 lg:p-10 group hover:bg-[#06112a] transition-colors">
              <div className="flex items-start justify-between mb-8">
                <div className="font-display text-emerald-500/30 group-hover:text-emerald-500/70 text-[80px] leading-none transition-colors">{s.num}</div>
                <div className="w-11 h-11 border border-slate-800 group-hover:border-emerald-500/50 rounded-sm flex items-center justify-center transition-colors">
                  <Icon icon={s.icon} size={18} className="text-emerald-400" />
                </div>
              </div>
              <h3 className="font-display text-[24px] text-white tracking-tight mb-1">{s.title}</h3>
              <p className="text-[13.5px] text-slate-400 leading-relaxed mb-7">{s.desc}</p>
              <ul className="space-y-2 pt-5 border-t border-slate-800/70">
                {s.tasks.map((t, j) => (
                  <li key={j} className="flex items-center gap-3 text-[12.5px] text-slate-400 font-mono">
                    <Icon icon={Check} size={13} className="text-emerald-500" strokeWidth={2} /><span>{t}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function ClosingCTA() {
  return (
    <section className="border-b border-slate-800/70 ambient-bg relative">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20 lg:py-28 relative">
        <div className="grid lg:grid-cols-12 gap-12 items-center">
          <div className="lg:col-span-7">
            <h2 className="font-display font-medium text-[36px] lg:text-[54px] text-white">Chaque jour qui passe<br/><span className="text-slate-500">rapproche vos fonds</span><br/>de la <span className="text-emerald-400 font-medium">prescription.</span></h2>
          </div>
          <div className="lg:col-span-5">
            <div className="border border-slate-800 bg-slate-950/60 rounded-sm p-7">
              <a href="#hero-widget" className="w-full inline-flex items-center justify-center gap-2 px-5 py-4 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-semibold text-[13px] uppercase tracking-[0.14em] rounded-sm transition-all emerald-glow-strong text-center">
                <span>Vérifier mon éligibilité</span><Icon icon={ArrowRight} size={15} />
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
