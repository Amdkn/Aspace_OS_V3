"use client";

export function RecoveryTicker() {
  const items = [
    { case: "A 2401114", amt: "$32,418", county: "Hamilton" },
    { case: "B 2308972", amt: "$87,200", county: "Hamilton" },
    { case: "A 2406302", amt: "$14,750", county: "Hamilton" },
    { case: "C 2305501", amt: "$129,840", county: "Butler" },
    { case: "A 2407108", amt: "$8,920", county: "Hamilton" },
    { case: "A 2402840", amt: "$54,610", county: "Hamilton" },
    { case: "B 2310014", amt: "$22,300", county: "Warren" },
    { case: "A 2406641", amt: "$71,205", county: "Hamilton" },
  ];
  const doubled = [...items, ...items];

  return (
    <div className="border-y border-slate-800/70 bg-[#040a1c] overflow-hidden relative">
      <div className="absolute left-0 top-0 bottom-0 w-24 bg-gradient-to-r from-[#040a1c] to-transparent z-10 pointer-events-none"></div>
      <div className="absolute right-0 top-0 bottom-0 w-24 bg-gradient-to-l from-[#040a1c] to-transparent z-10 pointer-events-none"></div>
      <div className="absolute left-6 lg:left-10 top-1/2 -translate-y-1/2 z-20 flex items-center gap-2 text-[10.5px] uppercase tracking-[0.22em] font-mono text-emerald-400 bg-[#040a1c] pr-4">
        <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full pulse-dot"></span>
        Restitutions récentes
      </div>
      <div className="py-3 marquee-track flex gap-10 whitespace-nowrap pl-[260px]">
        {doubled.map((it, i) => (
          <div key={i} className="flex items-center gap-3 text-[12.5px] text-slate-400 font-mono">
            <span className="text-slate-600">▸</span>
            <span className="text-slate-500">{it.county} County · </span>
            <span className="text-cream tracking-wider">{it.case}</span>
            <span className="text-slate-700">—</span>
            <span className="text-emerald-400 font-semibold">{it.amt}</span>
            <span className="text-slate-600">restitué</span>
          </div>
        ))}
      </div>
    </div>
  );
}
