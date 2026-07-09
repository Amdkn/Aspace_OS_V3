import { Lock, ShieldCheck, FileSearch } from "lucide-react";
import { StitchWidget } from "../widgets/StitchWidget";
import { RecoveryTicker } from "./RecoveryTicker";

export function Hero() {
  return (
    <section className="relative ambient-bg border-b border-slate-800/70 overflow-hidden">
      {/* Decorative side rulers */}
      <div className="absolute inset-y-0 left-6 lg:left-10 w-px hairline-v opacity-60 hidden md:block"></div>
      <div className="absolute inset-y-0 right-6 lg:right-10 w-px hairline-v opacity-60 hidden md:block"></div>

      <div className="max-w-[1400px] mx-auto px-6 lg:px-16 pt-16 pb-20 lg:pt-24 lg:pb-28 relative">

        {/* Eyebrow */}
        <div className="flex items-center gap-3 mb-10">
          <span className="h-px w-10 bg-emerald-500/70"></span>
          <span className="text-[11px] uppercase tracking-[0.28em] text-emerald-400 font-mono">
            File N° AB&middot;OH&middot;2026 / Récupération Excédentaire
          </span>
        </div>

        <div className="grid lg:grid-cols-12 gap-10 lg:gap-16 items-start">
          {/* LEFT: title + widget */}
          <div className="lg:col-span-7">
            <h1 className="font-display font-medium text-[40px] sm:text-[52px] lg:text-[68px] leading-[1.02] tracking-[-0.035em] text-white">
              L'État détient<br/>
              <span className="text-slate-500">votre argent.</span><br/>
              Nous forçons<br/>
              sa <span className="relative inline-block text-emerald-400">
                restitution.
                <svg className="absolute -bottom-2 left-0 w-full" height="10" viewBox="0 0 300 10" preserveAspectRatio="none">
                  <path d="M2 6 Q 75 1, 150 5 T 298 4" stroke="#10b981" strokeWidth="2" fill="none" strokeLinecap="round" opacity="0.7"/>
                </svg>
              </span>
            </h1>

            <p className="mt-8 text-[16px] lg:text-[17px] leading-relaxed text-slate-400 max-w-xl">
              Nous rapatrions vos <span className="text-cream">fonds excédentaires</span> bloqués au tribunal civil du
              comté de Hamilton. <span className="text-emerald-400">Zéro frais avancés.</span> Rémunération exclusivement
              au succès.
            </p>

            {/* Stitch Widget */}
            <div id="hero-widget" className="mt-10">
              <StitchWidget />
            </div>

            {/* Tiny legal print */}
            <div className="mt-5 flex flex-wrap items-center gap-x-5 gap-y-2 text-[11px] text-slate-500 font-mono uppercase tracking-[0.14em]">
              <span className="flex items-center gap-1.5"><Lock size={12} /> Connexion chiffrée</span>
              <span className="flex items-center gap-1.5"><ShieldCheck size={12} /> Données scellées 30j</span>
              <span className="flex items-center gap-1.5"><FileSearch size={12} /> Audit en moins de 48h</span>
            </div>
          </div>

          {/* RIGHT: Authority panel */}
          <div className="lg:col-span-5 relative">
            <AuthorityPanel />
          </div>
        </div>
      </div>

      {/* Bottom recent recoveries ticker */}
      <RecoveryTicker />
    </section>
  );
}

function AuthorityPanel() {
  return (
    <div className="relative border border-slate-800 bg-slate-950/60 backdrop-blur-sm rounded-sm overflow-hidden">
      {/* Header band */}
      <div className="border-b border-slate-800 px-5 py-3 flex items-center justify-between bg-slate-900/40">
        <div className="flex items-center gap-2 text-[10.5px] uppercase tracking-[0.22em] font-mono text-slate-400">
          <Lock size={13} className="text-emerald-500" />
          <span>Cabinet · Bilan public 2024</span>
        </div>
        <span className="text-[10px] text-emerald-400/80 font-mono uppercase tracking-[0.2em] flex items-center gap-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 pulse-dot"></span>
          Live
        </span>
      </div>

      {/* Big number */}
      <div className="p-6 border-b border-slate-800/70">
        <div className="text-[11px] uppercase tracking-[0.22em] text-slate-500 font-mono">Restitué aux ayants droit</div>
        <div className="mt-2 font-display text-[54px] leading-none tracking-tight text-white">
          $4.72<span className="text-emerald-400">M</span>
        </div>
        <div className="mt-2 text-[12px] text-slate-400">depuis l'ouverture du cabinet · OH only</div>
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
        <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-2">Partenaires Barreau OH</div>
        <div className="flex items-center gap-4 flex-wrap text-slate-400 text-[12px] font-display">
          <span className="flex items-center gap-1.5">Reyes &amp; Hall LLP</span>
          <span className="text-slate-800">·</span>
          <span className="flex items-center gap-1.5">Whitford Probate</span>
          <span className="text-slate-800">·</span>
          <span className="flex items-center gap-1.5">M. Bradbury Esq.</span>
        </div>
      </div>
    </div>
  );
}

function Stat({ label, value, sub, borderLeft, borderTop, accent }: any) {
  return (
    <div className={`px-5 py-4 ${borderLeft ? "border-l border-slate-800/70" : ""} ${borderTop ? "border-t border-slate-800/70" : ""}`}>
      <div className="text-[10.5px] uppercase tracking-[0.2em] text-slate-500 font-mono">{label}</div>
      <div className={`mt-1 font-display text-[26px] leading-none tracking-tight ${accent ? "text-emerald-400" : "text-white"}`}>{value}</div>
      <div className="mt-1 text-[10.5px] text-slate-500">{sub}</div>
    </div>
  );
}
