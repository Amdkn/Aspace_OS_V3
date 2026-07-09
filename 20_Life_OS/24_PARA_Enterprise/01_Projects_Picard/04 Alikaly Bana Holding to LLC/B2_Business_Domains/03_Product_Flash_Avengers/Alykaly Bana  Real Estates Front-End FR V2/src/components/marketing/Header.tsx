"use client";

import { Phone, ArrowUpRight } from "lucide-react";

export default function Header() {
  return (
    <header className="border-b border-slate-800/70 bg-[#020617]/85 backdrop-blur-md sticky top-0 z-20">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 h-20 flex items-center justify-between">
        {/* Logo */}
        <a href="#" className="flex items-center gap-3 group">
          <div className="relative">
            <div className="w-10 h-10 border border-slate-700 rounded-sm flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-950 group-hover:border-emerald-500/60 transition-colors">
              <span className="font-display font-bold text-emerald-500 text-lg leading-none">A</span>
            </div>
            <div className="absolute -top-1 -right-1 w-2 h-2 bg-emerald-500 rounded-full pulse-dot"></div>
          </div>
          <div className="leading-tight">
            <div className="font-display font-semibold tracking-[0.08em] text-cream text-[15px] uppercase">
              Alykaly Holding
            </div>
            <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 font-mono">
              Real Estate &middot; Legal Audits
            </div>
          </div>
        </a>

        {/* Nav */}
        <nav className="hidden lg:flex items-center gap-9 text-[13px] text-slate-400 font-medium tracking-wide">
          <a href="#expertises" className="hover:text-cream transition-colors">Expertises</a>
          <a href="#methode" className="hover:text-cream transition-colors">La Méthode</a>
          <a href="#promesse" className="hover:text-cream transition-colors">Garanties</a>
          <a href="#contact" className="hover:text-cream transition-colors">Cabinet</a>
        </nav>

        {/* CTA */}
        <div className="flex items-center gap-3">
          <a
            href="tel:+15135550101"
            className="hidden md:flex items-center gap-2 text-[12px] text-slate-400 hover:text-cream font-mono"
          >
            <Phone size={14} />
            <span>+1 (513) 555&middot;0101</span>
          </a>
          <a
            href="#hero-widget"
            className="group relative inline-flex items-center gap-2 px-4 lg:px-5 py-2.5 border border-emerald-500/70 text-emerald-400 hover:text-white hover:bg-emerald-500/10 transition-all text-[12.5px] font-medium uppercase tracking-[0.12em] rounded-sm emerald-glow"
          >
            <span>Vérifier mon éligibilité</span>
            <ArrowUpRight
              size={14}
              className="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform"
            />
          </a>
        </div>
      </div>
    </header>
  );
}
