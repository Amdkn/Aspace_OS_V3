"use client";

import { useEffect, useState } from "react";

export function TopBar() {
  const [time, setTime] = useState("");

  useEffect(() => {
    const tick = () => {
      const d = new Date();
      const hh = String(d.getHours()).padStart(2, "0");
      const mm = String(d.getMinutes()).padStart(2, "0");
      const ss = String(d.getSeconds()).padStart(2, "0");
      setTime(`${hh}:${mm}:${ss} EST`);
    };
    tick();
    const i = setInterval(tick, 1000);
    return () => clearInterval(i);
  }, []);

  return (
    <div className="border-b border-slate-800/70 bg-background/80 backdrop-blur-sm relative z-30">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-2 flex items-center justify-between text-[11px] uppercase tracking-[0.18em] text-slate-500 font-mono">
        <div className="flex items-center gap-4">
          <span className="flex items-center gap-1.5">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 pulse-dot"></span>
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
