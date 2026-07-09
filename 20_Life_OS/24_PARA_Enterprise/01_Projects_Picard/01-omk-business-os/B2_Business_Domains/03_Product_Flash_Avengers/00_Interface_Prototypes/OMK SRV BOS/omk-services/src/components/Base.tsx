import React from "react";
import { Icon } from "@/components/Icons";

export const MeshBackdrop = () => (
  <div aria-hidden="true" className="absolute inset-0 overflow-hidden pointer-events-none">
    <div className="absolute inset-0 grid-bg grid-bg-fade opacity-60" />
    <div className="blob animate-drift"     style={{ width: 620, height: 620, top: -160, left: -120, background: 'radial-gradient(circle at 30% 30%, #3B82F6 0%, transparent 60%)' } as any} />
    <div className="blob animate-driftSlow" style={{ width: 720, height: 720, top: -80,  right: -200, background: 'radial-gradient(circle at 60% 40%, #8B5CF6 0%, transparent 65%)' } as any} />
    <div className="blob animate-drift"     style={{ width: 520, height: 520, top:  260, left: '38%', background: 'radial-gradient(circle at 50% 50%, #EC4899 0%, transparent 65%)', opacity: 0.32 } as any} />
    <div className="absolute inset-x-0 top-[860px] h-[420px] bg-gradient-to-b from-transparent via-ink-950/70 to-ink-950" />
  </div>
);

export const Pill = ({ children, dot = true }: { children: React.ReactNode, dot?: boolean }) => (
  <span className="inline-flex items-center gap-2 rounded-full glass px-3 py-1.5 text-xs font-medium text-slate-300">
    {dot && <span className="relative flex h-1.5 w-1.5">
      <span className="absolute inset-0 rounded-full bg-fuchsia-400 animate-pulseDot" />
      <span className="relative rounded-full bg-fuchsia-400 h-1.5 w-1.5" />
    </span>}
    {children}
  </span>
);

export const BtnPrimary = ({ children, className = '', icon = true, href = '#audit' }: { children: React.ReactNode, className?: string, icon?: boolean, href?: string }) => (
  <a href={href} className={`btn-mesh group inline-flex items-center justify-center gap-2 rounded-full px-5 py-3 text-sm font-semibold text-white transition hover:brightness-110 ${className}`}>
    <span className="relative z-10 flex items-center gap-2">
      {children}
      {icon && <Icon.ArrowRight size={16} className="transition group-hover:translate-x-0.5" />}
    </span>
  </a>
);

export const BtnGhost = ({ children, className = '', href = '#methode' }: { children: React.ReactNode, className?: string, href?: string }) => (
  <a href={href} className={`inline-flex items-center justify-center gap-2 rounded-full glass px-5 py-3 text-sm font-semibold text-slate-200 transition hover:border-white/25 hover:bg-white/10 ${className}`}>
    {children}
  </a>
);

export const SectionTag = ({ children }: { children: React.ReactNode }) => (
  <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] uppercase tracking-[0.18em] text-slate-400">
    <span className="h-1 w-1 rounded-full bg-fuchsia-400" />
    {children}
  </div>
);
