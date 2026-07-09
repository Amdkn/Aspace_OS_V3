"use client";

import React from "react";
import { ClipboardCheck, Leaf, ShieldCheck, Camera, Star, ArrowUpRight } from "lucide-react";
import { Icon } from "./Icon";

export function Standards() {
  return (
    <section id="standards" className="py-20 lg:py-24">
      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12">
        <div className="grid lg:grid-cols-12 gap-10 items-start">
          <div className="lg:col-span-5">
            <span className="text-[12px] uppercase tracking-[0.22em] font-semibold text-emerald-700 flex items-center gap-2">
              <span className="w-7 h-px bg-emerald-700"></span> Standards hôteliers
            </span>
            <h2 className="font-display font-black text-emerald-950 mt-3 text-[36px] sm:text-[44px] leading-[1.05] tracking-[-0.035em]">
              On ne vend pas des heures.<br/>
              <span className="font-serif-i font-normal text-emerald-700">On livre</span> un résultat.
            </h2>
            <p className="text-stone-700 mt-5 text-[15.5px] leading-relaxed max-w-md">
              Chaque Pack est défini par une <span className="text-emerald-900 font-medium">checklist verrouillée</span> — pas par un chronomètre. Notre équipe coche chaque point dans l'app, prend une photo si nécessaire, et vous recevez le rapport en fin de prestation.
            </p>

            <a href="#packs" className="mt-8 inline-flex items-center gap-2 text-emerald-900 font-semibold text-[14px] link-u">
              Voir les checklists complètes <Icon icon={ArrowUpRight} size={15}/>
            </a>
          </div>

          <div className="lg:col-span-7">
            <div className="grid sm:grid-cols-2 gap-4">
              {[
                { ic: ClipboardCheck, t:"104 checkpoints", d:"par Deep Clean — verrouillés par SOP versionné", k:"v4.2" },
                { ic: Leaf, t:"EU Ecolabel", d:"produits éco-certifiés, sans allergènes agressifs", k:"100%" },
                { ic: ShieldCheck, t:"Techniciens CDI", d:"formés 80h sur nos procédures avant 1er chantier", k:"80h" },
                { ic: Camera, t:"Rapport photo", d:"avant/après livré dans l'app à chaque passage", k:"live" },
              ].map((c,i)=>(
                <div key={i} className="card p-6 flex flex-col">
                  <div className="flex items-center justify-between">
                    <div className="w-11 h-11 rounded-xl bg-stone-100 text-emerald-900 flex items-center justify-center">
                      <Icon icon={c.ic} size={20}/>
                    </div>
                    <span className="font-display font-bold text-[13px] text-lime-600 tracking-wider">{c.k}</span>
                  </div>
                  <div className="font-display font-bold text-[20px] text-emerald-950 mt-5 tracking-tight">{c.t}</div>
                  <p className="text-[13.5px] text-stone-600 mt-1.5 leading-snug">{c.d}</p>
                </div>
              ))}
            </div>

            <div className="card mt-4 p-6 lg:p-7 flex items-start gap-5">
              <div className="w-12 h-12 rounded-full bg-emerald-900 text-lime-300 flex items-center justify-center shrink-0 font-display font-black">
                JS
              </div>
              <div>
                <div className="flex items-center gap-1 mb-2">
                  {[0,1,2,3,4].map(i=>(<Icon key={i} icon={Star} size={13} className="text-lime-600" strokeWidth={2}/>))}
                </div>
                <p className="text-[15px] text-stone-800 leading-relaxed font-serif-i not-italic">
                  « Je suis abonnée au Flash depuis 6 mois — c'est la première fois qu'un service de ménage me donne envie d'éteindre mon téléphone et de partir au boulot l'esprit léger. »
                </p>
                <p className="mt-3 text-[12.5px] text-stone-500">Julie S. — Florence, KY · Pack Flash hebdo</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
