"use client";

import React from "react";
import { Zap, Sparkles, HardHat, Clock, Home, Check, ArrowRight, ShieldCheck, RefreshCcw, ReceiptText } from "lucide-react";
import { Icon } from "./Icon";

const PACKS = [
  {
    id:"flash",
    eyebrow:"01 · Maintien",
    name:"Le Flash",
    tag:"Hebdo / Bi-mensuel",
    icon: Zap,
    price:"89",
    unit:"€",
    cadence:"/ passage",
    sub:"À partir de — abonnement résiliable",
    intro:"Le rituel qui maintient votre maison en état hôtelier, semaine après semaine. Même technicien, même standard.",
    bullets:[
      "Cuisine + sanitaires en mode reset (28 checkpoints)",
      "Sols aspirés & lavés vapeur · multi-surfaces",
      "Surfaces hautes, miroirs, vitres intérieures",
      "Re-pass gratuit sous 48h si insatisfaction",
    ],
    cta:"Démarrer le rituel",
    duration:"≈ 2h",
    rooms:"jusqu'à 80 m²",
  },
  {
    id:"hulk",
    eyebrow:"02 · Reset total",
    name:"Le Hulk",
    tag:"Grand nettoyage / Deep clean",
    icon: Sparkles,
    price:"349",
    unit:"€",
    cadence:"prix fixe",
    sub:"Forfait au m² · devis instantané en ligne",
    intro:"Le grand reset. On démonte, on dégraisse, on détartre, on remet en service comme au premier jour. Idéal 2× / an.",
    bullets:[
      "Intérieur four, frigo, micro-ondes & hotte démontée",
      "Détartrage profond robinetterie + joints brossés",
      "Plinthes, interrupteurs, poignées, radiateurs",
      "Vitres intérieures + encadrements + appuis",
      "104 checkpoints — rapport photo livré",
    ],
    cta:"Réserver le reset",
    badge:"Le plus choisi",
    duration:"≈ 5h",
    rooms:"3 techniciens",
    featured:true,
  },
  {
    id:"stark",
    eyebrow:"03 · Cas extrêmes",
    name:"Le Stark",
    tag:"Post-travaux · Déménagement",
    icon: HardHat,
    price:"sur devis",
    unit:"",
    cadence:"≤ 24h",
    sub:"Visite + chiffrage instantané · sans engagement",
    intro:"Quand la maison sort d'un chantier ou se vide pour de bon. Poussière fine, résidus de plâtre, traces de peinture — tout part.",
    bullets:[
      "Décollage poussière fine (HEPA double passage)",
      "Traces peinture/colle/plâtre · solvants pro",
      "État des lieux conforme bail (caution garantie)",
      "Évacuation déchets + remise des clés",
    ],
    cta:"Demander un devis",
    duration:"½ à 2 jours",
    rooms:"équipe dédiée",
  },
];

function PackCard({ p }: any) {
  const featured = p.featured;
  return (
    <div className={(featured ? "card-featured" : "card") + " relative p-7 lg:p-8 flex flex-col h-full"}>
      {p.badge && (
        <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-lime-400 text-emerald-950 text-[11px] uppercase tracking-[0.18em] font-bold font-display px-3 py-1.5 rounded-full ring-2 ring-emerald-950">
          {p.badge}
        </div>
      )}

      <div className="flex items-center justify-between">
        <span className={"text-[11px] uppercase tracking-[0.2em] font-semibold " + (featured ? "text-lime-300" : "text-stone-500")}>
          {p.eyebrow}
        </span>
        <div className={"w-11 h-11 rounded-xl flex items-center justify-center " + (featured ? "bg-lime-400 text-emerald-950" : "bg-stone-100 text-emerald-900")}>
          <Icon icon={p.icon} size={20} strokeWidth={2}/>
        </div>
      </div>

      <h3 className={"font-display font-black text-[40px] leading-none mt-4 tracking-[-0.035em] " + (featured ? "text-white" : "text-emerald-950")}>
        {p.name}
      </h3>
      <p className={"mt-1 text-[14px] " + (featured ? "text-stone-300" : "text-stone-500")}>{p.tag}</p>

      <p className={"mt-5 text-[14px] leading-relaxed " + (featured ? "text-stone-200" : "text-stone-700")}>
        {p.intro}
      </p>

      <div className={"mt-6 flex items-baseline gap-1.5 " + (featured ? "text-white" : "text-emerald-950")}>
        <span className="font-display font-black text-[44px] tracking-[-0.035em] leading-none">
          {p.price}{p.unit && <span className="text-[28px] font-bold">{p.unit}</span>}
        </span>
        <span className={"text-[13px] font-medium " + (featured ? "text-lime-300" : "text-stone-500")}>{p.cadence}</span>
      </div>
      <p className={"text-[12.5px] mt-1 " + (featured ? "text-stone-400" : "text-stone-500")}>{p.sub}</p>

      <div className={"mt-5 flex flex-wrap gap-2"}>
        <span className={"inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11.5px] font-medium " + (featured ? "bg-white/10 text-stone-200" : "bg-stone-100 text-stone-700")}>
          <Icon icon={Clock} size={12}/> {p.duration}
        </span>
        <span className={"inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11.5px] font-medium " + (featured ? "bg-white/10 text-stone-200" : "bg-stone-100 text-stone-700")}>
          <Icon icon={Home} size={12}/> {p.rooms}
        </span>
      </div>

      <div className={"my-6 h-px " + (featured ? "bg-white/15" : "bg-stone-200")}></div>
      <div className="space-y-3">
        <div className={"text-[11px] uppercase tracking-[0.2em] font-semibold " + (featured ? "text-lime-300" : "text-emerald-700")}>
          Périmètre — checklist standardisée
        </div>
        {p.bullets.map((b: string, i: number)=>(
          <div key={i} className="flex items-start gap-3 text-[13.5px] leading-snug">
            <span className={(featured ? "chk chk-dark mt-0.5" : "chk mt-0.5")}>
              <Icon icon={Check} size={12} strokeWidth={2.5}/>
            </span>
            <span className={featured ? "text-stone-100" : "text-stone-800"}>{b}</span>
          </div>
        ))}
      </div>

      <div className="mt-auto pt-7">
        <a href="#" className={featured ? "btn-cta rounded-full h-12 px-5 inline-flex items-center justify-center gap-2 text-[14px] font-semibold font-display w-full" : "btn-dark rounded-full h-12 px-5 inline-flex items-center justify-center gap-2 text-[14px] font-semibold font-display w-full"}>
          {p.cta}
          <Icon icon={ArrowRight} size={15}/>
        </a>
        <p className={"text-center text-[11.5px] mt-3 " + (featured ? "text-stone-400" : "text-stone-500")}>
          Paiement à la livraison · satisfait ou re-passé
        </p>
      </div>
    </div>
  );
}

export function Packs() {
  return (
    <section id="packs" className="relative py-24 lg:py-32">
      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6 mb-14">
          <div className="max-w-2xl">
            <span className="text-[12px] uppercase tracking-[0.22em] font-semibold text-emerald-700 flex items-center gap-2">
              <span className="w-7 h-px bg-emerald-700"></span> Les Packs
            </span>
            <h2 className="font-display font-black text-emerald-950 mt-3 text-[40px] sm:text-[52px] leading-[1.02] tracking-[-0.035em]">
              Trois produits.<br/>
              <span className="font-serif-i font-normal text-emerald-700">Zéro</span> heure facturée.
            </h2>
          </div>
          <p className="text-stone-600 text-[15px] leading-relaxed max-w-md">
            Chaque pack est un <span className="font-medium text-emerald-900">livrable mesurable</span> avec un périmètre verrouillé et un prix transparent. Vous savez exactement ce qui sera fait — et vérifié — avant que l'équipe sonne.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-7 items-stretch">
          {PACKS.map((p) => (
            <div key={p.id} className={p.featured ? "lg:-mt-6" : ""}>
              <PackCard p={p}/>
            </div>
          ))}
        </div>

        <div className="mt-10 flex flex-wrap items-center justify-center gap-4 text-[13px] text-stone-600">
          <span className="inline-flex items-center gap-2"><Icon icon={ShieldCheck} size={15} className="text-emerald-700"/> Caution garantie pour les baux locatifs</span>
          <span className="hidden sm:inline w-1 h-1 rounded-full bg-stone-300"></span>
          <span className="inline-flex items-center gap-2"><Icon icon={RefreshCcw} size={15} className="text-emerald-700"/> Annulation gratuite jusqu'à H-12</span>
          <span className="hidden sm:inline w-1 h-1 rounded-full bg-stone-300"></span>
          <span className="inline-flex items-center gap-2"><Icon icon={ReceiptText} size={15} className="text-emerald-700"/> Facturation entreprise possible</span>
        </div>
      </div>
    </section>
  );
}
