"use client";

import { useState, useMemo } from "react";

export default function MarginShield() {
  const [load, setLoad] = useState(60);
  const [mode, setMode] = useState<"shield" | "brute">("shield");

  // Routing distribution
  const cheapShare =
    mode === "shield"
      ? Math.max(60, 95 - load * 0.4)
      : Math.max(10, 50 - load * 0.5);
  const midShare =
    mode === "shield" ? Math.min(30, load * 0.3) : 30;
  const heavyShare = 100 - cheapShare - midShare;

  // Cost: shield stays flat near $0.50/day, brute scales linearly
  const dailyCost =
    mode === "shield"
      ? 0.2 + (load / 100) * 0.5
      : 0.4 + (load / 100) * 9.0;
  const monthlyCost = dailyCost * 30;
  const ceiling = 20;
  const headroom = Math.max(
    0,
    Math.round((1 - monthlyCost / ceiling) * 100)
  );
  const exceeded = monthlyCost > ceiling;

  // bars — 18 ticks, evolving with load
  const bars = useMemo(() => {
    return Array.from({ length: 18 }).map((_, i) => {
      const variance = Math.sin(i * 0.9) * 0.18 + 1;
      const base =
        mode === "shield"
          ? 12 + (load / 100) * 25 * variance
          : 8 + (load / 100) * 85 * variance;
      return Math.min(95, base);
    });
  }, [load, mode]);

  return (
    <div className="shield-card">
      <div className="label-row">
        <div>Margin Shield · télémétrie compute</div>
        <div className="live">live</div>
      </div>

      <div className="shield-chart">
        <div
          className="shield-threshold"
          data-label="$20 / mois — plafond"
          style={{
            top: `${(1 - 20 / (monthlyCost > 20 ? monthlyCost * 1.1 : 25)) * 100}%`,
          }}
        />
        {bars.map((h, i) => (
          <div
            key={i}
            className={"shield-bar" + (mode === "brute" ? " brute" : "")}
            style={{
              height: `${h}%`,
              left: `${i * (100 / 18) + 0.5}%`,
            }}
          />
        ))}
      </div>

      <div className="shield-readouts">
        <div className="shield-readout">
          <div className="k">Coût / jour</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>
            ${dailyCost.toFixed(2)}
          </div>
        </div>
        <div className="shield-readout">
          <div className="k">Coût / mois</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>
            ${monthlyCost.toFixed(2)}
          </div>
        </div>
        <div className="shield-readout">
          <div className="k">Marge restante</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>
            {exceeded ? "OVER" : `${headroom}%`}
          </div>
        </div>
      </div>

      <div className="shield-router">
        <div className="router-row cheap">
          <div className="model">MiniMax 2.7</div>
          <div className="bar">
            <div style={{ width: `${cheapShare}%` }} />
          </div>
          <div className="pct">{cheapShare.toFixed(0)}%</div>
        </div>
        <div className="router-row mid">
          <div className="model">GLM 4.7 Flash</div>
          <div className="bar">
            <div style={{ width: `${midShare}%` }} />
          </div>
          <div className="pct">{midShare.toFixed(0)}%</div>
        </div>
        <div className="router-row heavy">
          <div className="model">Claude / GPT</div>
          <div className="bar">
            <div style={{ width: `${heavyShare}%` }} />
          </div>
          <div className="pct">{heavyShare.toFixed(0)}%</div>
        </div>
      </div>

      <div className="shield-control">
        <div className="row">
          <span>Charge de production</span>
          <span style={{ color: "var(--ink)" }}>{load}%</span>
        </div>
        <input
          type="range"
          className="shield-slider"
          min="10"
          max="100"
          value={load}
          onChange={(e) => setLoad(parseInt(e.target.value))}
        />
        <div className="row" style={{ marginTop: 14 }}>
          <span>Mode routeur</span>
          <span
            style={{
              display: "flex",
              gap: 0,
              border: "1px solid var(--line-2)",
              borderRadius: 0,
            }}
          >
            <button
              onClick={() => setMode("shield")}
              style={{
                padding: "4px 10px",
                fontSize: 10,
                fontFamily: "var(--font-mono)",
                letterSpacing: "0.15em",
                background:
                  mode === "shield" ? "var(--accent)" : "transparent",
                color:
                  mode === "shield" ? "var(--bg)" : "var(--ink-2)",
              }}
            >
              SHIELD
            </button>
            <button
              onClick={() => setMode("brute")}
              style={{
                padding: "4px 10px",
                fontSize: 10,
                fontFamily: "var(--font-mono)",
                letterSpacing: "0.15em",
                background:
                  mode === "brute" ? "var(--flare)" : "transparent",
                color:
                  mode === "brute" ? "var(--bg)" : "var(--ink-2)",
              }}
            >
              FORCE BRUTE
            </button>
          </span>
        </div>
      </div>
    </div>
  );
}
