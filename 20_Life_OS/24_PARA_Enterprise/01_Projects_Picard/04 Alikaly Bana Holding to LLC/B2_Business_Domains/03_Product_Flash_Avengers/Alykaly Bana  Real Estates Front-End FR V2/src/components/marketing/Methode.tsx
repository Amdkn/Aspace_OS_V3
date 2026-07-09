"use client";

import { ScanLine, FilePen, CircleDollarSign, Check, HandCoins, ArrowRight } from "lucide-react";

export default function Methode() {
  const steps = [
    {
      num: "I",
      title: "Audit & Localisation",
      sub: "Nous identifions les fonds.",
      desc: "Croisement de votre numéro de dossier avec les bases du Clerk of Courts et du Treasurer. Confirmation écrite de l'excédent et de votre éligibilité légale.",
      time: "24-48h",
      icon: ScanLine,
      tasks: ["Vérification dossier", "Confirmation excédent", "Lettre d'éligibilité"],
    },
    {
      num: "II",
      title: "Assemblage Légal",
      sub: "Nous mandatons et payons les avocats locaux.",
      desc: "Nos avocats du Barreau de l'Ohio préparent le Motion to Disburse, gèrent les notifications légales et plaident à votre place. Vous ne mettez pas un pied au tribunal.",
      time: "4-8 semaines",
      icon: FilePen,
      tasks: ["Motion to disburse", "Notifications créanciers", "Audience programmée"],
    },
    {
      num: "III",
      title: "Décaissement",
      sub: "Le juge libère les fonds directement vers vous.",
      desc: "Une fois la motion accordée, le chèque du Clerk est émis à votre nom. Nous prélevons notre commission de succès. Aucune avance n'a jamais quitté votre poche.",
      time: "2-3 semaines",
      icon: CircleDollarSign,
      tasks: ["Order signed", "Chèque émis", "Solde versé"],
    },
  ];

  return (
    <section id="methode" className="border-b border-slate-800/70 bg-[#040818] relative">
      <div className="absolute inset-0 grid-bg opacity-40 pointer-events-none" />
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20 lg:py-28 relative">
        <div className="flex items-center gap-3 mb-5">
          <span className="h-px w-10 bg-emerald-500/70" />
          <span className="text-[11px] uppercase tracking-[0.28em] text-emerald-400 font-mono">
            Processus Asynchrone
          </span>
        </div>
        <h2 className="font-display font-medium text-[34px] lg:text-[46px] leading-[1.05] tracking-[-0.03em] text-white max-w-3xl mb-16">
          Vous signez une fois.
          <br />
          <span className="text-slate-500">Nous orchestrons le reste.</span>
        </h2>

        <div className="relative grid lg:grid-cols-3 gap-px bg-slate-800/70 border border-slate-800/70 rounded-sm overflow-hidden">
          {steps.map((s, i) => (
            <div
              key={i}
              className="relative bg-[#040818] p-8 lg:p-10 group hover:bg-[#06112a] transition-colors"
            >
              {/* Roman number */}
              <div className="flex items-start justify-between mb-8">
                <div className="font-display text-emerald-500/30 group-hover:text-emerald-500/70 text-[80px] leading-none transition-colors">
                  {s.num}
                </div>
                <div className="flex flex-col items-end gap-2">
                  <div className="w-11 h-11 border border-slate-800 group-hover:border-emerald-500/50 rounded-sm flex items-center justify-center transition-colors">
                    <s.icon size={18} className="text-emerald-400" strokeWidth={1.4} />
                  </div>
                  <span className="text-[10px] uppercase tracking-[0.2em] font-mono text-slate-500">
                    {s.time}
                  </span>
                </div>
              </div>

              <h3 className="font-display text-[24px] text-white tracking-tight mb-1">{s.title}</h3>
              <p className="text-[13px] text-emerald-400/90 mb-5 italic">{s.sub}</p>
              <p className="text-[13.5px] text-slate-400 leading-relaxed mb-7">{s.desc}</p>

              <ul className="space-y-2 pt-5 border-t border-slate-800/70">
                {s.tasks.map((t, j) => (
                  <li key={j} className="flex items-center gap-3 text-[12.5px] text-slate-400 font-mono">
                    <Check size={13} className="text-emerald-500" strokeWidth={2} />
                    <span>{t}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Bottom assurance line */}
        <div className="mt-10 flex flex-col md:flex-row md:items-center md:justify-between gap-5 border border-slate-800 rounded-sm bg-slate-950/60 p-6">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 border border-emerald-500/40 bg-emerald-500/[0.05] rounded-sm flex items-center justify-center">
              <HandCoins size={18} className="text-emerald-400" />
            </div>
            <div>
              <div className="font-display text-[15px] text-white">Honoraires uniquement au succès.</div>
              <div className="text-[12.5px] text-slate-400">
                Si rien n&apos;est récupéré, vous ne devez rien. Aucune exception, aucun frais caché.
              </div>
            </div>
          </div>
          <a
            href="#hero-widget"
            className="inline-flex items-center gap-2 px-5 py-3 border border-emerald-500/70 text-emerald-400 hover:bg-emerald-500/10 hover:text-white transition-all text-[12px] uppercase tracking-[0.14em] rounded-sm font-medium emerald-glow self-start md:self-auto"
          >
            <span>Démarrer mon audit</span>
            <ArrowRight size={14} />
          </a>
        </div>
      </div>
    </section>
  );
}