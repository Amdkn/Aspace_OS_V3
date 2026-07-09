"use client";

import React, { useState, useEffect } from "react";
import { Icon } from "./Icons";
import { BtnPrimary } from "./Base";

export const Header = () => {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);
  return (
    <header className={`fixed inset-x-0 top-0 z-50 transition-all ${scrolled ? 'backdrop-blur-xl bg-ink-950/70 border-b border-white/5' : ''}`}>
      <div className="mx-auto max-w-7xl px-6 lg:px-10">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <a href="#" className="flex items-center gap-2.5 group">
            <span className="relative flex h-8 w-8 items-center justify-center rounded-lg" style={{ background: 'linear-gradient(135deg, #3B82F6, #8B5CF6 55%, #EC4899)' }}>
              <span className="absolute inset-[1px] rounded-[7px] bg-ink-950 flex items-center justify-center">
                <span className="font-display text-[15px] font-bold text-mesh">O</span>
              </span>
            </span>
            <div className="leading-none">
              <div className="font-display text-[15px] font-bold tracking-tight text-white">OMK <span className="text-slate-400 font-medium">SERVICES</span></div>
              <div className="mt-0.5 text-[9px] uppercase tracking-[0.22em] text-slate-500">Operational Engineering</div>
            </div>
          </a>

          {/* Nav */}
          <nav className="hidden md:flex items-center gap-1 rounded-full glass px-1.5 py-1.5">
            {[
              ['Notre Méthode', '#methode'],
              ['Business OS', '#os'],
              ['Nova (IA)', '#nova'],
            ].map(([l, h]) => (
              <a key={l} href={h} className="rounded-full px-3.5 py-1.5 text-[13px] font-medium text-slate-300 transition hover:text-white hover:bg-white/5">{l}</a>
            ))}
          </nav>

          {/* CTA */}
          <div className="hidden md:flex items-center gap-2">
            <BtnPrimary href="#audit" className="!py-2 !px-4 !text-[13px]">Réserver un audit</BtnPrimary>
          </div>

          {/* Mobile toggle */}
          <button onClick={() => setOpen(v => !v)} className="md:hidden glass rounded-full p-2.5">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><path d={open ? "M6 6l12 12M6 18L18 6" : "M4 7h16M4 12h16M4 17h16"} /></svg>
          </button>
        </div>

        {/* Mobile nav */}
        {open && (
          <div className="md:hidden pb-4">
            <div className="glass rounded-2xl p-3 space-y-1">
              {[['Notre Méthode', '#methode'], ['Business OS', '#os'], ['Nova (IA)', '#nova']].map(([l, h]) => (
                <a key={l} href={h} onClick={() => setOpen(false)} className="block rounded-xl px-3 py-2 text-sm font-medium text-slate-200 hover:bg-white/5">{l}</a>
              ))}
              <BtnPrimary href="#audit" className="w-full mt-2">Réserver un audit stratégique</BtnPrimary>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};
