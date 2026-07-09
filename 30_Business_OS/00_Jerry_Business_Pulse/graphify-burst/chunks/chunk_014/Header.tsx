"use client";

import React, { useState, useEffect } from "react";
import { Phone, ArrowRight } from "lucide-react";
import { Icon } from "./Icon";

export const Header = () => {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header className={`sticky top-0 z-50 transition-all ${scrolled ? "header-blur border-b border-stone-200/70" : ""}`}>
      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12 h-[72px] flex items-center justify-between">
        <a href="#" className="flex items-center gap-2.5 group">
          <span className="w-9 h-9 rounded-xl ring-leaf bg-white flex items-center justify-center">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#064E3B" strokeWidth="1.6">
              <path d="M4 20c2-10 8-16 16-16 0 8-6 14-16 16Z"/>
              <path d="M4 20c4-4 8-7 12-9"/>
            </svg>
          </span>
          <span className="font-display font-extrabold text-[19px] tracking-tight text-emerald-950 leading-none">
            Marina Cleaning<span className="text-lime-600">.</span>
            <span className="block text-[10px] font-medium uppercase tracking-[0.18em] text-stone-500 mt-1">Co. — Hospitality grade</span>
          </span>
        </a>

        <nav className="hidden md:flex items-center gap-8 text-[14px] text-stone-700 font-medium">
          <a href="#packs" className="link-u hover:text-emerald-900">Les Packs</a>
          <a href="#methode" className="link-u hover:text-emerald-900">La Méthode</a>
          <a href="#standards" className="link-u hover:text-emerald-900">Nos Standards</a>
          <a href="#zone" className="link-u hover:text-emerald-900">Zone couverte</a>
        </nav>

        <div className="flex items-center gap-2.5">
          <a href="tel:+18595551212" className="hidden sm:inline-flex btn-ghost rounded-full px-4 h-10 items-center gap-2 text-[13px] font-medium">
            <Icon icon={Phone} size={15} />
            <span className="hidden lg:inline">(859) 555-1212</span>
          </a>
          <a href="#packs" className="btn-cta rounded-full px-5 h-10 inline-flex items-center gap-2 text-[14px] font-semibold font-display">
            Réserver mon Pack
            <Icon icon={ArrowRight} size={16} />
          </a>
        </div>
      </div>
    </header>
  );
};
