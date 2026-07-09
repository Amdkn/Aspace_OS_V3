"use client";

import React from 'react';
import { MapPin, Phone, Mail } from 'lucide-react';
import { Icon } from './Icon';

export function Footer() {
  return (
    <footer id="contact" className="bg-[#020617]">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 pt-16 pb-10">
        <div className="grid lg:grid-cols-12 gap-12 pb-12 border-b border-slate-800/70">
          <div className="lg:col-span-5">
            <div className="flex items-center gap-3 mb-5">
              <div className="w-10 h-10 border border-slate-700 rounded-sm flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-950">
                <span className="font-display font-bold text-emerald-500 text-lg leading-none">A</span>
              </div>
              <div className="font-display font-semibold tracking-[0.08em] text-white text-[15px] uppercase">Alykaly Holding</div>
            </div>
            <p className="text-[13.5px] text-slate-400 leading-relaxed max-w-md">
              Cabinet d'audit juridique privé dédié à la récupération des fonds excédentaires post-saisie (ORC §2329.44).
            </p>
            <div className="mt-7 space-y-2.5 text-[12.5px] font-mono text-slate-400">
              <div className="flex items-center gap-3"><Icon icon={MapPin} size={13} className="text-emerald-500/80" /><span>312 Walnut St &middot; Cincinnati, OH 45202</span></div>
              <div className="flex items-center gap-3"><Icon icon={Phone} size={13} className="text-emerald-500/80" /><span>+1 (513) 555&middot;0101</span></div>
              <div className="flex items-center gap-3"><Icon icon={Mail} size={13} className="text-emerald-500/80" /><span>audit@alykaly-holding.com</span></div>
            </div>
          </div>

          <div className="lg:col-span-7 grid sm:grid-cols-3 gap-8">
            {["Cabinet", "Expertises", "Juridictions"].map((title, i) => (
              <div key={title}>
                <div className="text-[10.5px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-4">{title}</div>
                <ul className="space-y-2.5 text-[13px] text-slate-400">
                  {i === 0 && ["À propos", "Bilan public", "Presse"].map(l => <li key={l}><a href="#" className="hover:text-white transition-colors">{l}</a></li>)}
                  {i === 1 && ["Foreclosure Surplus", "Tax Lien Overages", "Ghost Probate"].map(l => <li key={l}><a href="#" className="hover:text-white transition-colors">{l}</a></li>)}
                  {i === 2 && ["Hamilton County", "Butler County", "Warren County"].map(l => <li key={l} className="flex justify-between"><span>{l}</span><span className="text-emerald-500 text-[10px]">ACTIF</span></li>)}
                </ul>
              </div>
            ))}
          </div>
        </div>

        <div className="pt-8 flex flex-col md:flex-row md:items-center md:justify-between gap-5 text-[11.5px] text-slate-500 font-mono uppercase tracking-[0.18em]">
          <div>© 2024–2026 Alykaly Holding LLC &middot; OH&middot;BL2024&middot;887401</div>
          <div className="flex items-center gap-5">
            <a href="#" className="hover:text-white transition-colors">Mentions légales</a>
            <a href="#" className="hover:text-white transition-colors">Confidentialité</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
