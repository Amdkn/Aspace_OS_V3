import { Shield, Scale, Lock } from "lucide-react";

export function PromiseBar() {
  const items = [
    { icon: Shield, title: "Zéro Risque Financier", sub: "Pas de fonds récupérés, pas d'honoraires. Garantie écrite." },
    { icon: Scale, title: "Frais d'Avocats Inclus", sub: "Nous mandatons et payons les avocats du Barreau de l'Ohio." },
    { icon: Lock, title: "Confidentialité Absolue", sub: "Données scellées. Procédure menée discrètement, hors audience publique." },
  ];
  return (
    <section id="promesse" className="border-b border-slate-800/70 bg-background">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 grid md:grid-cols-3">
        {items.map((it, i) => (
          <div key={i} className={`flex items-start gap-5 py-10 lg:py-14 px-2 lg:px-8 ${i > 0 ? "md:border-l border-slate-800/70" : ""}`}>
            <div className="flex-shrink-0 w-12 h-12 border border-emerald-500/40 rounded-sm flex items-center justify-center bg-emerald-500/[0.04]">
              <it.icon size={22} className="text-emerald-400" strokeWidth={1.4} />
            </div>
            <div>
              <div className="font-display text-[18px] text-white tracking-tight">{it.title}</div>
              <div className="mt-1.5 text-[13.5px] text-slate-400 leading-relaxed">{it.sub}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
