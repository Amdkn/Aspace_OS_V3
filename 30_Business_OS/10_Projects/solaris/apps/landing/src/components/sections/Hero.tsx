"use client";

import { useState, useEffect } from "react";
import { SOLARIS_DOMAINS, SOLARIS_ARCHETYPES } from "@/lib/data";
import OrbitalDiagram from "@/components/diagrams/OrbitalDiagram";

interface HeroProps {
  icp: string;
}

export default function Hero({ icp }: HeroProps) {
  const domains = SOLARIS_DOMAINS;
  const [active, setActive] = useState(domains[0].id);
  const icpData = SOLARIS_ARCHETYPES.find((f) => f.id === icp) || SOLARIS_ARCHETYPES[0];

  useEffect(() => {
    const id = setInterval(() => {
      setActive((curr) => {
        const i = domains.findIndex((d) => d.id === curr);
        return domains[(i + 1) % domains.length].id;
      });
    }, 3200);
    return () => clearInterval(id);
  }, [domains]);

  return (
    <section className="hero">
      <div className="hero-grid" />
      <div className="hero-copy">
        <div className="eyebrow">
          AaaS · agency as a service · profile detected · {icpData.name}
        </div>
        <h1 className="display">
          Stop hiring
          <br />
          operators.
          <br />
          <em>Plug into our factory.</em>
        </h1>
        <p className="sub">
          You sell the strategy and own the client relationship. We handle total
          execution in the background. Solaris is a white-label production
          infrastructure. Scale your operations and protect your margins —
          without ever growing your payroll, without managing freelances.
        </p>
        <p
          className="sub"
          style={{ marginTop: 18, fontStyle: "italic", color: "var(--accent-2)" }}
        >
          You&apos;re not buying another SaaS tool.
          <br />
          You&apos;re renting an{" "}
          <b style={{ color: "var(--ink)", fontStyle: "normal", fontWeight: 500 }}>
            autonomous org chart
          </b>
          .
        </p>
        <div className="hero-cta-row">
          <a className="btn-primary" href="#vault-form">
            submit your url <span className="arrow">→</span>
          </a>
          <a className="btn-ghost" href="#anatomy">
            meet your new team
          </a>
        </div>
        <div className="hero-meta">
          <div className="stat">
            <div className="v">70%</div>
            <div className="l">margin kept · under your brand</div>
          </div>
          <div className="stat">
            <div className="v">0</div>
            <div className="l">hires · 0 freelances to manage</div>
          </div>
          <div className="stat">
            <div className="v">24h</div>
            <div className="l">audit delivered · no calls</div>
          </div>
          <div className="stat">
            <div className="v">
              3<span style={{ fontSize: "60%", opacity: 0.5 }}>×</span>10
              <span style={{ fontSize: "60%", opacity: 0.5 }}>²</span>+
            </div>
            <div className="l">agents · ready to execute</div>
          </div>
        </div>
      </div>
      <OrbitalDiagram activeId={active} onHover={setActive} />
    </section>
  );
}
