"use client";

import React, { useState, useEffect } from 'react';
import { Phone, ArrowUpRight } from 'lucide-react';
import { Icon } from './Icon';

export function TopBar() {
  const [time, setTime] = useState("");
  useEffect(() => {
    const tick = () => {
      const d = new Date();
      setTime(d.toLocaleTimeString('en-US', { hour12: false, timeZone: 'America/New_York' }) + " EST");
    };
    tick();
    const i = setInterval(tick, 1000);
    return () => clearInterval(i);
  }, []);

  return (
    <div className="border-b border-slate-800/70 bg-[#020617]/80 backdrop-blur-sm relative z-30">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-2 flex items-center justify-between text-[11px] uppercase tracking-[0.18em] text-slate-500 font-mono">
        <div className="flex items-center gap-4">
          <span className="flex items-center gap-1.5">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse-dot"></span>
            <span className="text-slate-400">Cabinet ouvert</span>
          </span>
          <span className="hidden sm:inline text-slate-700">|</span>
          <span className="hidden sm:inline">Cincinnati · Hamilton County · OH</span>
        </div>
        <div className="hidden md:flex items-center gap-4">
          <span>Greffe en session</span>
          <span className="text-slate-700">|</span>
          <span className="text-slate-400">{time}</span>
        </div>
      </div>
    </div>
  );
}

export function Header() {
  return (
    <header className="border-b border-slate-800/70 bg-[#020617]/85 backdrop-blur-md sticky top-0 z-20">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 h-20 flex items-center justify-between">
        <a href="#" className="flex items-center gap-3 group">
          <div className="relative">
            <div className="w-10 h-10 border border-slate-700 rounded-sm flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-950 group-hover:border-emerald-500/60 transition-colors">
              <span className="font-display font-bold text-emerald-500 text-lg leading-none">A</span>
            </div>
            <div className="absolute -top-1 -right-1 w-2 h-2 bg-emerald-500 rounded-full animate-pulse-dot"></div>
          </div>
          <div className="leading-tight">
            <div className="font-display font-semibold tracking-[0.08em] text-[#fffaf0] text-[15px] uppercase">Alykaly Holding</div>
            <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 font-mono">Real Estate &middot; Legal Audits</div>
          </div>
        </a>

        <nav className="hidden lg:flex items-center gap-9 text-[13px] text-slate-400 font-medium tracking-wide">
          <a href="#expertises" className="hover:text-[#fffaf0] transition-colors">Expertises</a>
          <a href="#methode" className="hover:text-[#fffaf0] transition-colors">La Méthode</a>
          <a href="#promesse" className="hover:text-[#fffaf0] transition-colors">Garanties</a>
          <a href="#contact" className="hover:text-[#fffaf0] transition-colors">Cabinet</a>
        </nav>

        <div className="flex items-center gap-3">
          <a href="tel:+15135550101" className="hidden md:flex items-center gap-2 text-[12px] text-slate-400 hover:text-[#fffaf0] font-mono transition-colors">
            <Icon icon={Phone} size={14} />
            <span>+1 (513) 555&middot;0101</span>
          </a>
          <a href="#hero-widget" className="group relative inline-flex items-center gap-2 px-4 lg:px-5 py-2.5 border border-emerald-500/70 text-emerald-400 hover:text-white hover:bg-emerald-500/10 transition-all text-[12.5px] font-medium uppercase tracking-[0.12em] rounded-sm emerald-glow">
            <span>Vérifier mon éligibilité</span>
            <Icon icon={ArrowUpRight} size={14} className="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </a>
        </div>
      </div>
    </header>
  );
}
