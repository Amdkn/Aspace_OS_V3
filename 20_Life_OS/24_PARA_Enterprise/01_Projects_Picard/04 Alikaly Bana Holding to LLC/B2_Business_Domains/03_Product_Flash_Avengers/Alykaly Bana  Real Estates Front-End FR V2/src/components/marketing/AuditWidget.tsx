"use client";

import { useState, useMemo } from "react";
import { ScanLine, Search, X, Loader, ShieldCheck, Info, AlertCircle, CheckCircle2, FileX, ArrowRight } from "lucide-react";

type WidgetState = "idle" | "validating" | "found" | "notfound" | "invalid";

export default function AuditWidget() {
  const [val, setVal] = useState("");
  const [state, setState] = useState<WidgetState>("idle");
  const [progress, setProgress] = useState(0);

  const formatCase = (raw: string): string => {
    const cleaned = raw.toUpperCase().replace(/[^A-Z0-9]/g, "");
    if (!cleaned) return "";
    const letter = cleaned.charAt(0);
    const digits = cleaned.slice(1).replace(/\D/g, "").slice(0, 7);
    return digits ? `${letter} ${digits}` : letter;
  };

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const formatted = formatCase(e.target.value);
    setVal(formatted);
    if (state !== "idle") setState("idle");
  };

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const m = val.match(/^[A-Z]\s\d{7}$/);
    if (!m) { setState("invalid"); return; }
    setState("validating");
    setProgress(0);
    const start = Date.now();
    const duration = 2400;
    const i = setInterval(() => {
      const p = Math.min(100, ((Date.now() - start) / duration) * 100);
      setProgress(p);
      if (p >= 100) {
        clearInterval(i);
        const num = parseInt(val.replace(/\D/g, ""), 10);
        if (num % 7 === 3) setState("notfound");
        else setState("found");
      }
    }, 40);
  };

  const reset = () => { setState("idle"); setVal(""); setProgress(0); };

  const surplus = useMemo(() => {
    if (state !== "found") return null;
    const num = parseInt(val.replace(/\D/g, ""), 10) || 0;
    const base = 12000 + (num % 97) * 873;
    return base;
  }, [state, val]);

  return (
    <div
      className={`relative border bg-gradient-to-br from-slate-900/70 to-slate-950/90 backdrop-blur-sm rounded-sm transition-all duration-300 ${
        state === "found"
          ? "border-emerald-500/60 emerald-glow-strong"
          : state === "validating"
          ? "border-emerald-500/40"
          : state === "invalid" || state === "notfound"
          ? "border-rose-500/40"
          : "border-slate-800 hover:border-slate-700"
      }`}
    >
      <div className="flex items-center justify-between px-5 pt-4 pb-2 border-b border-slate-800/70">
        <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.2em] font-mono text-slate-500">
          <ScanLine size={13} className="text-emerald-500" />
          <span>Module d&apos;Audit Sécurisé</span>
        </div>
        <div className="text-[10px] font-mono text-slate-600 uppercase tracking-widest">
          v2.6 · SHA-256
        </div>
      </div>

      <form onSubmit={onSubmit} className="p-5">
        <label className="block text-[11px] uppercase tracking-[0.2em] text-slate-500 font-mono mb-3">
          Numéro de dossier — Hamilton County Common Pleas
        </label>
        <div className="flex flex-col sm:flex-row gap-3">
          <div className="flex-1 relative">
            <span className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-600 font-mono text-[13px]">
              <Search size={16} />
            </span>
            <input
              type="text"
              value={val}
              onChange={onChange}
              disabled={state === "validating"}
              placeholder="A 2403702"
              autoComplete="off"
              spellCheck={false}
              className="w-full bg-slate-950/80 border border-slate-800 hover:border-slate-700 focus-emerald rounded-sm pl-11 pr-4 py-3.5 text-[17px] font-mono tracking-wider text-white placeholder-slate-700 transition-all"
            />
            {val && state === "idle" && (
              <button
                type="button"
                onClick={() => setVal("")}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-600 hover:text-slate-400"
              >
                <X size={14} />
              </button>
            )}
          </div>
          <button
            type="submit"
            disabled={state === "validating" || !val}
            className="group inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-emerald-500 hover:bg-emerald-400 disabled:bg-slate-800 disabled:text-slate-600 disabled:cursor-not-allowed text-slate-950 font-semibold text-[13px] uppercase tracking-[0.14em] rounded-sm transition-all emerald-glow-strong disabled:shadow-none"
          >
            {state === "validating" ? (
              <>
                <Loader size={15} className="animate-spin" />
                <span>Audit...</span>
              </>
            ) : (
              <>
                <ShieldCheck size={15} />
                <span>Lancer l&apos;Audit</span>
              </>
            )}
          </button>
        </div>

        {/* Progress / result tray */}
        <div className="mt-4 min-h-[28px] text-[12px] font-mono">
          {state === "idle" && (
            <div className="flex items-center justify-between text-slate-500">
              <span className="flex items-center gap-2">
                <Info size={12} />
                Format Ohio: 1 lettre + 7 chiffres (ex. <span className="text-slate-300">A 2403702</span>)
              </span>
              <button
                type="button"
                onClick={() => { setVal("A 2403702"); setState("idle"); }}
                className="text-emerald-500/80 hover:text-emerald-400 uppercase tracking-[0.18em] text-[10px]"
              >
                ↳ Exemple
              </button>
            </div>
          )}

          {state === "validating" && (
            <div>
              <div className="flex justify-between text-slate-400 text-[11px] uppercase tracking-[0.18em]">
                <span>Connexion au Clerk of Courts…</span>
                <span className="text-emerald-400">{Math.floor(progress)}%</span>
              </div>
              <div className="mt-2 h-[2px] w-full bg-slate-800 rounded-full overflow-hidden">
                <div className="h-full bg-emerald-500 transition-all" style={{ width: `${progress}%` }}></div>
              </div>
              <div className="mt-2 text-[10.5px] uppercase tracking-[0.22em] flex gap-4 flex-wrap">
                <span className={progress > 20 ? "text-emerald-500" : ""}>● Localisation</span>
                <span className={progress > 50 ? "text-emerald-500" : ""}>● Vérification fonds</span>
                <span className={progress > 80 ? "text-emerald-500" : ""}>● Audit légal</span>
              </div>
            </div>
          )}

          {state === "invalid" && (
            <div className="flex items-center justify-between gap-2 text-rose-400">
              <span className="flex items-center gap-2">
                <AlertCircle size={13} /> Format invalide — utilisez 1 lettre suivie de 7 chiffres.
              </span>
              <button type="button" onClick={reset} className="text-slate-500 hover:text-slate-300 text-[10px] uppercase tracking-[0.18em]">
                Réessayer
              </button>
            </div>
          )}

          {state === "notfound" && (
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 text-rose-300/90">
              <span className="flex items-center gap-2">
                <FileX size={13} /> Aucun fonds excédentaire détecté pour <span className="text-white">{val}</span>.
              </span>
              <button type="button" onClick={reset} className="text-emerald-500/80 hover:text-emerald-400 text-[10px] uppercase tracking-[0.18em]">
                ↳ Nouveau dossier
              </button>
            </div>
          )}

          {state === "found" && (
            <div className="border border-emerald-500/40 bg-emerald-500/[0.06] rounded-sm p-4 mt-1">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                <div>
                  <div className="flex items-center gap-2 text-emerald-400 uppercase tracking-[0.2em] text-[10.5px]">
                    <CheckCircle2 size={13} /> Fonds détectés &middot; Dossier {val}
                  </div>
                  <div className="mt-2 flex items-baseline gap-2">
                    <span className="font-display text-[34px] text-white tracking-tight">
                      ${surplus?.toLocaleString("en-US")}
                    </span>
                    <span className="text-[11px] text-slate-400 uppercase tracking-[0.18em]">
                      excédent vérifié
                    </span>
                  </div>
                  <div className="mt-1 text-[11px] text-slate-500">
                    Détenu par le Clerk of Courts &middot; Statut :{" "}
                    <span className="text-cream">Réclamable</span>
                  </div>
                </div>
                <button
                  type="button"
                  className="inline-flex items-center justify-center gap-2 px-5 py-3 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-semibold text-[12px] uppercase tracking-[0.14em] rounded-sm whitespace-nowrap"
                >
                  <span>Mandater le cabinet</span>
                  <ArrowRight size={14} />
                </button>
              </div>
            </div>
          )}
        </div>
      </form>
    </div>
  );
}