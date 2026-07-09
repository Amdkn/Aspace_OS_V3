import { ShieldCheck } from "lucide-react";

export function ClosingCTA() {
  return (
    <section className="border-b border-slate-800/70 ambient-bg relative">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20 lg:py-28 relative">
        <div className="grid lg:grid-cols-12 gap-12 items-center">
          <div className="lg:col-span-7">
            <div className="flex items-center gap-3 mb-5">
              <span className="h-px w-10 bg-emerald-500/70"></span>
              <span className="text-[11px] uppercase tracking-[0.28em] text-emerald-400 font-mono">Dernière chose</span>
            </div>
            <h2 className="font-display font-medium text-[36px] lg:text-[54px] leading-[1.02] tracking-[-0.035em] text-white">
              Chaque jour qui passe<br/>
              <span className="text-slate-500">rapproche vos fonds</span><br/>
              de la <span className="text-emerald-400">prescription.</span>
            </h2>
            <p className="mt-7 text-[15.5px] text-slate-400 leading-relaxed max-w-xl">
              L'Ohio dispose d'un délai légal au-delà duquel les fonds excédentaires sont définitivement transférés au comté. Une vérification prend 90 secondes.
            </p>
          </div>
          <div className="lg:col-span-5">
            <div className="border border-slate-800 bg-slate-950/60 rounded-sm p-7">
              <div className="text-[11px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-5">Audit gratuit · 48h</div>
              <ol className="space-y-4">
                {[
                  "Entrez votre numéro de dossier ou votre nom",
                  "Recevez la fiche d'éligibilité signée",
                  "Mandatez le cabinet si vous le souhaitez"
                ].map((t, i) => (
                  <li key={i} className="flex items-start gap-4">
                    <span className="flex-shrink-0 w-7 h-7 border border-slate-700 rounded-sm font-mono text-[12px] text-emerald-400 flex items-center justify-center">{i+1}</span>
                    <span className="text-[14px] text-slate-300 leading-snug pt-1">{t}</span>
                  </li>
                ))}
              </ol>
              <a href="#hero-widget"
                 className="mt-7 w-full inline-flex items-center justify-center gap-2 px-5 py-4 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-semibold text-[13px] uppercase tracking-[0.14em] rounded-sm transition-all emerald-glow-strong">
                <ShieldCheck size={15} />
                <span>Vérifier mon éligibilité maintenant</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
