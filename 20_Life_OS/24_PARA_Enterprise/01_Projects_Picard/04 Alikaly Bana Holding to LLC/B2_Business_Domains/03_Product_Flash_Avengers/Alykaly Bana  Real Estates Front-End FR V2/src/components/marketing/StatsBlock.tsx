"use client";

interface StatProps {
  label: string;
  value: string;
  sub: string;
  borderLeft?: boolean;
  borderTop?: boolean;
  accent?: boolean;
}

export default function Stat({ label, value, sub, borderLeft, borderTop, accent }: StatProps) {
  return (
    <div
      className={`px-5 py-4 ${borderLeft ? "border-l border-slate-800/70" : ""} ${
        borderTop ? "border-t border-slate-800/70" : ""
      }`}
    >
      <div className="text-[10.5px] uppercase tracking-[0.2em] text-slate-500 font-mono">
        {label}
      </div>
      <div
        className={`mt-1 font-display text-[26px] leading-none tracking-tight ${
          accent ? "text-emerald-400" : "text-white"
        }`}
      >
        {value}
      </div>
      <div className="mt-1 text-[10.5px] text-slate-500">{sub}</div>
    </div>
  );
}
