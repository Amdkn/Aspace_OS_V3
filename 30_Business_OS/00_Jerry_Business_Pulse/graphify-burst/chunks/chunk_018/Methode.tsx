"use client";

import React from "react";
import { MousePointerClick, ClipboardCheck, Home, ArrowRight, Sparkles } from "lucide-react";
import { Icon } from "./Icon";

const STEPS = [
  {
    n:"01",
    icon: MousePointerClick,
    title:"Réservation en 60 secondes",
    desc:"Vous choisissez votre Pack, votre créneau, votre adresse. Le prix est confirmé à l'écran — aucun appel, aucun devis manuel.",
    bullets:["Devis instantané","Paiement sécurisé","Confirmation SMS"],
  },
  {
    n:"02",
    icon: ClipboardCheck,
    title:"Intervention sur SOP",
    desc:"Nos techniciens en CDI arrivent avec la checklist du Pack. Ils cochent chaque point dans l'app — vous recevez le rapport photo en direct.",
    bullets:["Équipe formée 80h","37 checkpoints/h","Rapport photo live"],
  },
  {
    n:"03",
    icon: Home,
    title:"Une maison parfaite",
    desc:"Vous rentrez. Tout est à sa place, vérifié, certifié. Si un détail cloche, on re-passe sous 48h — sans discussion, sans surcoût.",
    bullets:["Satisfait ou re-passé","Suivi mensuel optionnel","Note technicien"],
  },
];

export function Methode() {
  return (
    <section id="methode" className="relative py-24 lg:py-32 bg-emerald-950 text-white overflow-hidden">
      <svg className="absolute -top-20 -right-20 opacity-[0.08]" width="500" height="500" viewBox="0 0 200 200" fill="none">
        <path d="M20 180c10-80 80-150 160-160 0 80-70 150-160 160Z" stroke="#BEF264" strokeWidth="1"/>
        <path d="M40 175c20-30 50-60 100-90" stroke="#BEF264" strokeWidth="1"/>
      </svg>

      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12 relative">
        <div className="max-w-3xl">
          <span className="text-[12px] uppercase tracking-[0.22em] font-semibold text-lime-300 flex items-center gap-2">
            <span className="w-7 h-px bg-lime-300"></span> La Méthode
          </span>
          <h2 className="font-display font-black mt-3 text-[40px] sm:text-[56px] leading-[1.02] tracking-[-0.035em]">
            Trois étapes.<br/>
            <span className="font-serif-i font-normal text-lime-300">Zéro</span> friction.
          </h2>
          <p className="text-stone-300 text-[16px] mt-5 leading-relaxed max-w-xl">
            On a industrialisé chaque geste pour que vous, vous n&apos;ayez plus rien à faire — sauf rentrer.
          </p>
        </div>

        <div className="mt-16 grid md:grid-cols-3 gap-8 lg:gap-10 relative">
          <div className="hidden md:block absolute top-12 left-[16.66%] right-[16.66%] h-px dotted opacity-60"></div>

          {STEPS.map((s)=>(
            <div key={s.n} className="relative">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-2xl bg-lime-400 text-emerald-950 flex items-center justify-center relative z-10">
                  <Icon icon={s.icon} size={22} strokeWidth={2}/>
                </div>
                <span className="font-display font-black text-[15px] tracking-[0.16em] text-lime-300">{s.n}</span>
              </div>

              <h3 className="font-display font-bold text-[24px] leading-tight mt-5 text-white">
                {s.title}
              </h3>
              <p className="text-stone-300 text-[14.5px] leading-relaxed mt-3 max-w-sm">
                {s.desc}
              </p>

              <ul className="mt-5 space-y-2">
                {s.bullets.map((b,j)=>(
                  <li key={j} className="flex items-center gap-2.5 text-[13px] text-stone-200">
                    <span className="w-1.5 h-1.5 rounded-full bg-lime-400"></span> {b}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-20 lg:mt-24 rounded-3xl border border-white/10 bg-white/[0.04] p-6 lg:p-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div>
            <div className="flex items-center gap-2 text-[12px] uppercase tracking-[0.18em] text-lime-300 font-semibold">
              <Icon icon={Sparkles} size={13}/> Garantie hôtelière
            </div>
            <h3 className="font-display font-bold text-[24px] sm:text-[28px] mt-2 leading-tight">
              Pas satisfait·e ? On re-passe sous 48h.<br className="hidden sm:block"/>
              <span className="text-stone-300 font-medium">Aucun débat, aucun frais.</span>
            </h3>
          </div>
          <a href="#packs" className="btn-cta rounded-full h-14 px-7 inline-flex items-center justify-center gap-2 text-[15px] font-semibold font-display shrink-0">
            Réserver maintenant <Icon icon={ArrowRight} size={16}/>
          </a>
        </div>
      </div>
    </section>
  );
}
