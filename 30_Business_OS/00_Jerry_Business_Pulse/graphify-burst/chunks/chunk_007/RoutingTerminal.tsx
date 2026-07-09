"use client";

import { useState, useEffect, useMemo } from "react";

export default function RoutingTerminal() {
  const [step, setStep] = useState(0);
  const lines = useMemo(
    () => [
      { p: true, t: "vous@solaris.factory" },
      { c: 'post --payload "audit complet + 3 propositions de pivot"' },
      { type: "out" as const, t: "→ B1.Jerry reçoit la commande..." },
      { type: "dim" as const, t: "  · traduction en spécifications" },
      { type: "ok" as const, t: "✓ routé : B2.Wonder Woman (Production)" },
      { type: "out" as const, t: "" },
      { p: true, t: "B2.Wonder Woman" },
      { c: "dispatch --task extract --priority routine" },
      { type: "out" as const, t: "→ analyse de complexité..." },
      { type: "dim" as const, t: "  · payload léger · 4.2kb" },
      { type: "ok" as const, t: "✓ assigné : B3.Star-Lord  · coût : $0.0003" },
      { type: "out" as const, t: "" },
      { p: true, t: "B2.Wonder Woman" },
      { c: "dispatch --task synthèse --priority lourde" },
      { type: "out" as const, t: "→ escalade nécessaire..." },
      { type: "dim" as const, t: "  · raisonnement long · 38kb" },
      {
        type: "warn" as const,
        t: "↑ escaladé : B3.Captain Marvel · capé à $0.04",
      },
      { type: "out" as const, t: "" },
      { p: true, t: "B2.Batman" },
      { c: "watch --margin status" },
      { type: "out" as const, t: "  routine compute  $00.47 / jour" },
      { type: "out" as const, t: "  plafond actif    $20.00 / mois" },
      { type: "ok" as const, t: "  marge protégée   91% headroom" },
      { type: "out" as const, t: "" },
      { p: true, t: "B3.Star-Lord" },
      { c: "loop --scrape OH-KY" },
      {
        type: "err" as const,
        t: "✗ agent en boucle · 4 retries · arrêté",
      },
      {
        type: "warn" as const,
        t: "↪ B2.Batman intercepte · budget protégé",
      },
      {
        type: "ok" as const,
        t: "✓ agent mis en quarantaine · enquête",
      },
    ],
    []
  );

  useEffect(() => {
    if (step >= lines.length) return;
    const line = lines[step];
    const delay = line.c ? 600 : line.p ? 200 : 320;
    const id = setTimeout(() => setStep((s) => s + 1), delay);
    return () => clearTimeout(id);
  }, [step, lines]);

  // reset loop
  useEffect(() => {
    if (step < lines.length) return;
    const id = setTimeout(() => setStep(0), 4000);
    return () => clearTimeout(id);
  }, [step, lines.length]);

  return (
    <div className="terminal">
      <div className="terminal-bar">
        <div className="dots">
          <div className="dot" />
          <div className="dot" />
          <div className="dot" />
        </div>
        <div>routage interne · vous n&apos;avez jamais à voir ceci</div>
      </div>
      <div className="terminal-body">
        {lines.slice(0, step).map((l, i) => (
          <div key={i} className="line">
            {l.p && (
              <span>
                <span className="prompt">{l.t} </span>
                <span className="dim">$</span>{" "}
              </span>
            )}
            {l.c && (
              <>
                <span className="dim">$ </span>
                <span className="cmd">{l.c}</span>
              </>
            )}
            {l.type === "out" && <span className="out">{l.t}</span>}
            {l.type === "dim" && <span className="dim">{l.t}</span>}
            {l.type === "ok" && <span className="ok">{l.t}</span>}
            {l.type === "warn" && <span className="warn">{l.t}</span>}
            {l.type === "err" && <span className="err">{l.t}</span>}
          </div>
        ))}
        {step < lines.length && <span className="cursor" />}
      </div>
    </div>
  );
}
