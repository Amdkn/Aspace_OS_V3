"use client";

import React, { useState } from "react";
import { Icon } from "@/components/icons";

export function AuditForm() {
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setStatus("loading");
    
    const formData = new FormData(e.currentTarget);
    const data = {
      name: formData.get("name"),
      email: formData.get("email"),
      company: formData.get("company"),
      revenue: formData.get("revenue"),
    };

    try {
      const res = await fetch("/api/audit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (res.ok) {
        setStatus("success");
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  };

  if (status === "success") {
    return (
      <div className="rounded-2xl border border-emerald-500/20 bg-emerald-500/5 p-8 text-center glass animate-rise">
        <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-emerald-500/20 text-emerald-400 mb-4">
          <Icon.Check size={28} />
        </div>
        <h3 className="text-xl font-semibold text-white">Demande confirmée</h3>
        <p className="mt-2 text-sm text-emerald-200/80">
          Notre IA Nova va vous contacter d'ici quelques minutes pour planifier l'audit stratégique.
        </p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="mt-10 mx-auto max-w-md text-left glass rounded-2xl p-6 sm:p-8 space-y-4">
      <div>
        <label htmlFor="name" className="block text-xs font-medium text-slate-400 mb-1.5 uppercase tracking-wider">Nom complet</label>
        <input required type="text" id="name" name="name" className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm text-white placeholder-slate-500 focus:border-fuchsia-500/50 focus:outline-none focus:ring-1 focus:ring-fuchsia-500/50 transition" placeholder="Omar Kounta" />
      </div>
      <div>
        <label htmlFor="email" className="block text-xs font-medium text-slate-400 mb-1.5 uppercase tracking-wider">Email professionnel</label>
        <input required type="email" id="email" name="email" className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm text-white placeholder-slate-500 focus:border-fuchsia-500/50 focus:outline-none focus:ring-1 focus:ring-fuchsia-500/50 transition" placeholder="omar@entreprise.com" />
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label htmlFor="company" className="block text-xs font-medium text-slate-400 mb-1.5 uppercase tracking-wider">Entreprise</label>
          <input required type="text" id="company" name="company" className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm text-white placeholder-slate-500 focus:border-fuchsia-500/50 focus:outline-none focus:ring-1 focus:ring-fuchsia-500/50 transition" placeholder="Ma Société" />
        </div>
        <div>
          <label htmlFor="revenue" className="block text-xs font-medium text-slate-400 mb-1.5 uppercase tracking-wider">CA Annuel</label>
          <select required id="revenue" name="revenue" className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm text-slate-300 focus:border-fuchsia-500/50 focus:outline-none focus:ring-1 focus:ring-fuchsia-500/50 transition appearance-none">
            <option value="" disabled selected>Sélectionner...</option>
            <option value="<100k">&lt; 100k€</option>
            <option value="100k-500k">100k€ - 500k€</option>
            <option value="500k-1M">500k€ - 1M€</option>
            <option value=">1M">&gt; 1M€</option>
          </select>
        </div>
      </div>
      
      {status === "error" && (
        <div className="text-sm text-rose-400 p-3 rounded-lg bg-rose-500/10 border border-rose-500/20">
          Une erreur est survenue. Veuillez réessayer.
        </div>
      )}

      <button disabled={status === "loading"} type="submit" className="w-full btn-mesh group inline-flex items-center justify-center gap-2 rounded-xl px-5 py-3.5 text-sm font-semibold text-white transition hover:brightness-110 disabled:opacity-70 disabled:cursor-not-allowed mt-2">
        <span className="relative z-10 flex items-center gap-2">
          {status === "loading" ? "Envoi en cours..." : "Réserver mon audit stratégique"}
          {status !== "loading" && <Icon.ArrowRight size={16} className="transition group-hover:translate-x-0.5" />}
        </span>
      </button>
      <div className="text-center mt-3">
        <span className="text-[11px] text-slate-500 flex items-center justify-center gap-1.5">
          <Icon.Shield size={12} className="text-emerald-400"/>
          Vos données sont sécurisées et ne seront jamais partagées.
        </span>
      </div>
    </form>
  );
}