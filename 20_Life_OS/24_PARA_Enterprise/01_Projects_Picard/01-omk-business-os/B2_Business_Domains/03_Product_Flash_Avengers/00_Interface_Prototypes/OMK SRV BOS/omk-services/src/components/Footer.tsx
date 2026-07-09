"use client";

import React from "react";
import { Icon } from "@/components/Icons";

export const Footer = () => (
  <footer className="relative border-t border-white/5 bg-ink-950/80">
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-14">
      <div className="grid grid-cols-2 md:grid-cols-5 gap-10">
        <div className="col-span-2">
          <a href="#" className="flex items-center gap-2.5">
            <span className="relative flex h-8 w-8 items-center justify-center rounded-lg" style={{ background: 'linear-gradient(135deg, #3B82F6, #8B5CF6 55%, #EC4899)' }}>
              <span className="absolute inset-[1px] rounded-[7px] bg-ink-950 flex items-center justify-center">
                <span className="font-display text-[15px] font-bold text-mesh">O</span>
              </span>
            </span>
            <div className="font-display text-[15px] font-bold tracking-tight text-white">OMK SERVICES</div>
          </a>
          <p className="mt-4 text-[13px] text-slate-400 max-w-sm leading-relaxed">
            Ingénierie opérationnelle pour Small Business Owners. Nous transformons les entreprises manuelles en Self-Operating Businesses.
          </p>
          <div className="mt-6 flex items-center gap-2">
            <a href="#" aria-label="LinkedIn" className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Linkedin size={15}/></a>
            <a href="#" aria-label="Twitter"  className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Twitter size={15}/></a>
            <a href="#" aria-label="Github"   className="glass rounded-full p-2.5 hover:border-white/25 transition"><Icon.Github size={15}/></a>
          </div>
        </div>

        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Produit</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#os" className="hover:text-white">Business OS</a></li>
            <li><a href="#nova" className="hover:text-white">Nova IA</a></li>
            <li><a href="#methode" className="hover:text-white">Méthode</a></li>
            <li><a href="#" className="hover:text-white">Tarifs</a></li>
          </ul>
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Société</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#" className="hover:text-white">À propos</a></li>
            <li><a href="#" className="hover:text-white">Cas clients</a></li>
            <li><a href="#" className="hover:text-white">Carrières</a></li>
            <li><a href="#" className="hover:text-white">Contact</a></li>
          </ul>
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 mb-4">Légal</div>
          <ul className="space-y-2.5 text-[13px] text-slate-300">
            <li><a href="#" className="hover:text-white">Confidentialité</a></li>
            <li><a href="#" className="hover:text-white">CGU / CGV</a></li>
            <li><a href="#" className="hover:text-white">Sécurité</a></li>
            <li><a href="#" className="hover:text-white">RGPD</a></li>
          </ul>
        </div>
      </div>

      <div className="mt-12 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-t border-white/5 pt-6">
        <div className="text-[12px] text-slate-500">
          © 2026 OMK SERVICES — Empowering Small Business Owners.
        </div>
        <div className="flex items-center gap-2 text-[11px] text-slate-500">
          <Icon.Globe size={13}/> Paris · Casablanca · Remote
        </div>
      </div>
    </div>
  </footer>
);
