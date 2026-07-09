"use client";

import { SOLARIS_ARCHETYPES } from "@/lib/data";

interface TopbarProps {
  icp: string;
  setIcp: (id: string) => void;
}

export default function Topbar({ icp, setIcp }: TopbarProps) {
  return (
    <header className="topbar">
      <div className="brand">
        <div className="brand-mark" />
        <div className="brand-name">
          <b>solaris</b>
        </div>
        <div className="brand-tag">the ghost factory · oh / ky</div>
      </div>
      <nav className="nav" aria-label="Sections">
        <a href="#hook">
          <span className="num">01</span>The hook
        </a>
        <a href="#anatomy">
          <span className="num">02</span>B1/B2/B3 anatomy
        </a>
        <a href="#shield">
          <span className="num">03</span>Your margins
        </a>
        <a href="#wheel">
          <span className="num">04</span>8 poles
        </a>
        <a href="#archetypes">
          <span className="num">05</span>Profiles
        </a>
        <a href="#paradigms">
          <span className="num">06</span>2026 levers
        </a>
        <a href="#vault">
          <span className="num">07</span>Onboarding
        </a>
      </nav>
      <div style={{ display: "flex", gap: 14, alignItems: "center" }}>
        <div className="icp-strip" aria-label="Your profile">
          {SOLARIS_ARCHETYPES.map((f) => (
            <button
              key={f.id}
              className={icp === f.id ? "active" : ""}
              onClick={() => setIcp(f.id)}
            >
              {f.name}
            </button>
          ))}
        </div>
        <a className="top-cta" href="#vault-form">
          <span className="pulse" />
          submit a url
        </a>
      </div>
    </header>
  );
}
