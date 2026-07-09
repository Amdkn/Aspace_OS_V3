"use client";

import React from "react";
import { Sparkles, ArrowRight, LayoutGrid, Star, Leaf } from "lucide-react";
import { Icon } from "./Icon";
import { ImageSlot } from "./ImageSlot";

export const Hero = () => {
  return (
    <section className="relative overflow-hidden grain">
      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12 pt-10 lg:pt-16 pb-20 lg:pb-28">
        <div className="grid lg:grid-cols-12 gap-10 lg:gap-14 items-end">
          <div className="lg:col-span-7 animate-fade-up">
            <div className="inline-flex items-center gap-2 seal rounded-full pl-2 pr-3.5 py-1.5 text-[12px] font-medium">
              <span className="w-5 h-5 rounded-full bg-emerald-900 text-lime-300 flex items-center justify-center">
                <Icon icon={Sparkles} size={11} />
              </span>
              Service-as-a-Product · Cincinnati × Florence × N. Kentucky
            </div>

            <h1 className="font-display font-black text-emerald-950 mt-6 text-[44px] leading-[1.02] sm:text-[60px] lg:text-[76px] lg:leading-[0.98] tracking-[-0.035em]">
              Arrêtez de gérer<br/>votre ménage.<br/>
              <span className="font-serif-i font-normal text-emerald-700">Branchez-vous</span> sur notre système.
            </h1>

            <p className="mt-7 text-stone-700 text-[17px] sm:text-[19px] leading-[1.55] max-w-[560px]">
              Des standards de propreté <span className="font-medium text-emerald-900">hôteliers</span>, exécutés chez vous, sans friction. On ne facture pas des heures — on livre un résultat, à la checklist près.
            </p>

            <div className="mt-9 flex flex-wrap items-center gap-3">
              <a href="#packs" className="btn-cta rounded-full pl-6 pr-5 h-14 inline-flex items-center gap-2.5 text-[15px] font-semibold font-display">
                Réserver mon Pack
                <span className="w-7 h-7 rounded-full bg-emerald-950 text-lime-300 flex items-center justify-center">
                  <Icon icon={ArrowRight} size={14} />
                </span>
              </a>
              <a href="#packs" className="btn-ghost rounded-full px-6 h-14 inline-flex items-center gap-2 text-[15px] font-semibold font-display">
                <Icon icon={LayoutGrid} size={16} />
                Découvrir nos Packs
              </a>
            </div>

            <div className="mt-10 flex flex-wrap items-center gap-x-7 gap-y-4 text-[13px] text-stone-600">
              <div className="flex items-center gap-2">
                <div className="flex -space-x-2">
                  {["#84CC16","#064E3B","#A3E635","#047857"].map((c,i)=>(
                    <div key={i} className="w-7 h-7 rounded-full ring-2 ring-stone-50 flex items-center justify-center text-[10px] font-bold text-white" style={{background:c}}>
                      {"MJSL"[i]}
                    </div>
                  ))}
                </div>
                <span><span className="font-semibold text-emerald-950">312 foyers</span> nettoyés ce trimestre</span>
              </div>
              <div className="h-4 w-px bg-stone-300"></div>
              <div className="flex items-center gap-1.5">
                {[0,1,2,3,4].map(i=>(<Icon key={i} icon={Star} size={14} className="text-lime-600" strokeWidth={2}/>))}
                <span className="ml-1"><span className="font-semibold text-emerald-950">4,96/5</span> · 184 avis vérifiés</span>
              </div>
            </div>
          </div>

          <div className="lg:col-span-5 relative animate-fade-up delay-2">
            <div className="relative">
              <div className="relative rounded-[28px] overflow-hidden ring-1 ring-stone-200 bg-white shadow-[0_40px_80px_-30px_rgba(6,78,59,.35)]">
                <ImageSlot id="hero-photo" placeholder="Photo d'intérieur propre & lumineux" />
                
                <div className="absolute top-4 left-4 right-4 flex items-start justify-between pointer-events-none">
                  <span className="seal rounded-full px-3 py-1.5 text-[11px] font-semibold flex items-center gap-1.5">
                    <Icon icon={Leaf} size={11}/> Eco-certified products
                  </span>
                  <span className="bg-white/95 backdrop-blur rounded-full px-3 py-1.5 text-[11px] font-semibold text-emerald-950 ring-1 ring-stone-200 flex items-center gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-lime-500"></span>
                    Tech disponible aujourd'hui
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="marquee-container">
        <div className="marquee-track whitespace-nowrap text-[13px] uppercase tracking-[0.18em] text-stone-500 font-medium">
          {Array(2).fill(0).map((_,r)=>(
            <div key={r} className="flex items-center gap-14 pr-14">
              {[
                ["Leaf","Produits éco-certifiés EU Ecolabel"],
                ["ShieldCheck","Techniciens en CDI · formés sur SOP"],
                ["BadgeDollarSign","Prix fixe — zéro surprise"],
                ["Sparkles","Re-pass garanti sous 48h"],
                ["MapPin","Cincinnati · Florence · N. Kentucky"],
                ["Clock","Créneaux 7j/7 — 7h à 20h"],
              ].map(([ic,t],i)=>(
                <div key={i} className="inline-flex items-center gap-2.5">
                  <span className="text-emerald-700 font-bold">·</span> {t}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
