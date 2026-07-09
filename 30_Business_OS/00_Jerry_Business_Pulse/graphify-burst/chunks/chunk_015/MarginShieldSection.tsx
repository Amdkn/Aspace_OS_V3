"use client";

import RoutingTerminal from "@/components/diagrams/RoutingTerminal";
import MarginShield from "@/components/diagrams/MarginShield";

export default function MarginShieldSection() {
  return (
    <section
      className="section"
      id="shield"
      style={{ background: "var(--bg-2)" }}
    >
      <div className="shield-wrap">
        <div>
          <div className="eyebrow">03 · margins, locked in</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Your execution cost
            <br />
            is <em>a fixed input.</em>
          </h2>
          <p className="s-sub" style={{ marginTop: 28 }}>
            Your competitors burn margin sending every task to the most
            expensive AI on the market. We route. Routine work — extraction,
            sorting, formatting — runs on lean B3 squads. Only heavy reasoning
            ever escalates, and always under a ceiling.
          </p>
          <p className="s-sub" style={{ marginTop: 18 }}>
            If a squad stalls,{" "}
            <b style={{ color: "var(--ink)", fontWeight: 500 }}>Batman</b> (B2 ·
            Ops) shuts it down before it loops through your budget. You bill on
            value. We pay for frugality. That gap — that&apos;s your margin.
          </p>
          <div style={{ marginTop: 36 }}>
            <RoutingTerminal />
          </div>
        </div>
        <MarginShield />
      </div>
    </section>
  );
}
