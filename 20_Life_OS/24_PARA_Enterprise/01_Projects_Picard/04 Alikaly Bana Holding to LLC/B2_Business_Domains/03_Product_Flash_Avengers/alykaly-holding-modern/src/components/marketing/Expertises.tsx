import { Home, Landmark, FileSearch, ArrowUpRight } from "lucide-react";

export function Expertises() {
  const cards = [
    {
      tag: "01 / Foreclosure Surplus",
      icon: Home,
      title: "Saisies Bancaires",
      desc: "Lorsqu'une maison est vendue aux enchères pour plus que la dette hypothécaire, l'excédent vous revient — pas à la banque. Nous l'extrayons du greffe.",
      kpi: "Médiane: $42K",
      kpiSub: "par dossier récupéré"
    },
    {
      tag: "02 / Tax Lien Overages",
      icon: Landmark,
      title: "Excédents Fiscaux",
      desc: "Après une saisie pour impôts fonciers impayés, le Trésorier garde l'excédent. Trois ans plus tard, il est versé au comté. Nous le réclamons avant prescription.",
      kpi: "Prescription: 3 ans",
      kpiSub: "à compter de la vente"
    },
    {
      tag: "03 / Ghost Probate",
      icon: FileSearch,
      title: "Successions Bloquées",
      desc: "Un parent est décédé en laissant des fonds non réclamés. Sans succession ouverte, l'argent dort. Nous initions la probate et reconstituons la chaîne d'héritiers.",
      kpi: "12 héritiers/an",
      kpiSub: "identifiés en moyenne"
    }
  ];

  return (
    <section id="expertises" className="border-b border-slate-800/70 grid-bg relative">
      <div className="absolute inset-0 bg-gradient-to-b from-background via-transparent to-background pointer-events-none"></div>
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20 lg:py-28 relative">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6 mb-14">
          <div>
            <div className="flex items-center gap-3 mb-5">
              <span className="h-px w-10 bg-emerald-500/70"></span>
              <span className="text-[11px] uppercase tracking-[0.28em] text-emerald-400 font-mono">Nos Expertises</span>
            </div>
            <h2 className="font-display font-medium text-[34px] lg:text-[46px] leading-[1.05] tracking-[-0.03em] text-white max-w-2xl">
              Trois territoires juridiques.<br/>
              <span className="text-slate-500">Un seul réflexe :</span> rapatrier vos fonds.
            </h2>
          </div>
          <p className="text-[14px] text-slate-400 max-w-sm leading-relaxed">
            Chaque dossier est traité par un binôme auditeur juridique + avocat du Barreau de l'Ohio. Aucune intervention n'est délégée à un tiers non agréé.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-5">
          {cards.map((c, i) => (
            <article key={i} className="expertise-card relative border border-slate-800 bg-slate-950/50 rounded-sm p-7 flex flex-col group cursor-pointer">
              <div className="flex items-center justify-between mb-7">
                <span className="text-[10.5px] uppercase tracking-[0.22em] font-mono text-slate-500">{c.tag}</span>
                <ArrowUpRight size={16} className="card-arrow text-slate-600 transition-all" />
              </div>

              <div className="w-11 h-11 border border-slate-800 group-hover:border-emerald-500/50 rounded-sm flex items-center justify-center bg-slate-950 mb-6 transition-colors">
                <c.icon size={20} className="text-emerald-400" strokeWidth={1.4} />
              </div>

              <h3 className="font-display text-[22px] text-white tracking-tight mb-3">{c.title}</h3>
              <p className="text-[13.5px] text-slate-400 leading-relaxed mb-7">{c.desc}</p>

              <div className="mt-auto pt-5 border-t border-slate-800/80">
                <div className="text-[10.5px] uppercase tracking-[0.2em] text-slate-500 font-mono">{c.kpiSub}</div>
                <div className="mt-1 font-display text-[20px] text-emerald-400 tracking-tight">{c.kpi}</div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
