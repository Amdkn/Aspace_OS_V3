"use client";

import { useState } from "react";
import { SOLARIS_DOMAINS } from "@/lib/data";
import DomainWheel from "@/components/diagrams/DomainWheel";

export default function WheelSection() {
  const domains = SOLARIS_DOMAINS;
  const [idx, setIdx] = useState(0);
  const d = domains[idx];

  return (
    <section className="section" id="wheel">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">04 · the 8 expertise poles</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Eight chiefs.
            <br />
            Thirty-two squads.
            <br />
            <em>One order to give.</em>
          </h2>
        </div>
        <p className="s-sub">
          Each pole is run by a VP (B2 · Justice League DC) who signs off
          deliverables before release. Underneath, B3 squads (Marvels) crush
          the execution. Click a pole to see who&apos;s working for you there.
        </p>
      </div>
      <div className="wheel-wrap">
        <DomainWheel activeIdx={idx} onSelect={setIdx} />
        <div
          className="wheel-detail"
          key={d.id}
          style={{ display: "flex", flexDirection: "column" }}
        >
          <div className="domain-num">
            POLE {d.n} · {d.sub.toUpperCase()}
          </div>
          <h3>{d.name}</h3>
          <div className="role">
            {d.vp} · {d.agents} B3 squads under their command
          </div>
          <p className="description">{d.role}</p>
          {d.squads && (
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                gap: 6,
                marginBottom: 18,
              }}
            >
              {d.squads.map((s) => (
                <span
                  key={s}
                  style={{
                    fontFamily: "var(--font-mono)",
                    fontSize: 11,
                    letterSpacing: "0.05em",
                    padding: "4px 10px",
                    border: "1px solid var(--line-2)",
                    borderRadius: 999,
                    color: "var(--accent-2)",
                  }}
                >
                  {s}
                </span>
              ))}
            </div>
          )}
          <div className="telemetry">
            <div className="telem-cell">
              <div className="k">Pulse</div>
              <div className="v" style={{ color: "var(--mint)" }}>
                ● {d.metric}
              </div>
            </div>
            <div className="telem-cell">
              <div className="k">Status</div>
              <div className="v">
                {d.status === "active"
                  ? "active"
                  : d.status === "stable"
                    ? "stable"
                    : "standby"}
              </div>
            </div>
            <div className="telem-cell">
              <div className="k">B2 VP</div>
              <div className="v">{d.vp}</div>
            </div>
            <div className="telem-cell">
              <div className="k">B3 squads</div>
              <div className="v">{d.agents} active</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
