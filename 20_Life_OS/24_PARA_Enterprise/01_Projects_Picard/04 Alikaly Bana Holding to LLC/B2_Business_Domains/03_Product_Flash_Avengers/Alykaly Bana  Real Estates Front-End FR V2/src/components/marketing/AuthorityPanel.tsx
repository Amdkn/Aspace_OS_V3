"use client";

import { Landmark } from "lucide-react";
import Stat from "./StatsBlock";

interface AuthorityPanelProps {}

export default function AuthorityPanel() {
  return (
    <div className="relative border border-slate-800 bg-slate-950/60 backdrop-blur-sm rounded-sm overflow-hidden">
      {/* Header band */}
      <div className="border-b border-slate-800 px-5 py-3 flex items-center justify-between bg-slate-900/40">
        <div className="flex items-center gap-2 text-[10.5px] uppercase tracking-[0.22em] font-mono text-slate-400">
          <Landmark size={13} className="text-emerald-500" />
          <span>Cabinet · Bilan public 2024</span>
        </div>
        <span className="text-[10px] text-emerald-400/80 font-mono uppercase tracking-[0.2em] flex items-center gap-1.5">
          <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full pulse-dot"></span>
          Live
        </span>
      </div>

      {/* Big number */}
      <div className="p-6 border-b border-slate-800/70">
        <div className="text-[11px] uppercase tracking-[0.22em] text-slate-500 font-mono">
          Restitué aux ayants droit
        </div>
        <div className="mt-2 font-display text-[54px] leading-none tracking-tight text-white">
          $4.72<span className="text-emerald-400">M</span>
        </div>
        <div className="mt-2 text-[12px] text-slate-400">
          depuis l&apos;ouverture du cabinet · OH only
        </div>
      </div>

      {/* Mini grid */}
      <div className="grid grid-cols-2">
        <Stat label="Dossiers clos" value="187" sub="+12 ce mois" />
        <Stat label="Taux de succès" value="94%" sub="2022 → 2026" borderLeft />
        <Stat label="Délai moyen" value="11 sem." sub="audit → décaiss." borderTop />
        <Stat label="Frais avancés" value="$0" sub="contingence 100%" borderLeft borderTop accent />
      </div>

      {/* Footer trust strip */}
      <div className="border-t border-slate-800 px-5 py-3.5 bg-slate-900/40">
        <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-2">
          Partenaires Barreau OH
        </div>
        <div className="flex items-center gap-4 flex-wrap text-slate-400 text-[12px] font-display">
          <span className="flex items-center gap-1.5">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="text-emerald-500/70"><Scale size={13} /></svg>
            Reyes &amp; Hall LLP
          </span>
          <span className="text-slate-800">·</span>
          <span className="flex items-center gap-1.5">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="text-emerald-500/70"><Scale size={13} /></svg>
            Whitford Probate
          </span>
          <span className="text-slate-800">·</span>
          <span className="flex items-center gap-1.5">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="text-emerald-500/70"><Scale size={13} /></svg>
            M. Bradbury Esq.
          </span>
        </div>
      </div>
    </div>
  );
}

function Scale({ size = 13 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
      <path d="M12 3v18M3 9l4 4 4-4 4 4 4-4" strokeLinecap="round" strokeLinejoin="round" />
      <path d="M3 15l4-4 4 4 4-4 4 4" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}