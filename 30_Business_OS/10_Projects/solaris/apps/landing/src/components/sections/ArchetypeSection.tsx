"use client";

import { SOLARIS_ARCHETYPES } from "@/lib/data";

// ─── Archetype Glyphs ────────────────────────────────────────────
function ArchGlyph({ id }: { id: string }) {
  if (id === "revops")
    return (
      <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
        <rect x="6" y="14" width="12" height="10" fill="none" stroke="var(--accent)" />
        <rect x="22" y="6" width="12" height="10" fill="none" stroke="var(--accent)" />
        <rect x="22" y="40" width="12" height="10" fill="none" stroke="var(--accent)" />
        <rect x="38" y="14" width="12" height="10" fill="none" stroke="var(--accent)" />
        <rect x="38" y="32" width="12" height="10" fill="none" stroke="var(--accent)" />
        <path
          d="M18 19 L22 11 M18 19 L22 45 M34 11 L38 19 M34 45 L38 37 M28 16 V40"
          stroke="var(--accent)"
          strokeOpacity="0.6"
          strokeDasharray="2 2"
          fill="none"
        />
        <circle cx="28" cy="28" r="4" fill="var(--accent)" />
      </svg>
    );
  if (id === "forges")
    return (
      <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
        {[10, 18, 26, 34, 42].map((y) => (
          <line
            key={y}
            x1="6"
            y1={y}
            x2="50"
            y2={y}
            stroke="var(--accent)"
            strokeOpacity={y === 26 ? 1 : 0.4}
            strokeWidth={y === 26 ? 1.5 : 1}
          />
        ))}
        <rect x="22" y="6" width="2" height="44" fill="var(--accent)" />
        <rect x="32" y="6" width="2" height="44" fill="var(--accent)" opacity="0.4" />
      </svg>
    );
  if (id === "aaa")
    return (
      <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
        <path
          d="M8 48 L8 28 L28 8 L48 28 L48 48 Z"
          fill="none"
          stroke="var(--accent)"
        />
        <rect x="22" y="34" width="12" height="14" fill="var(--accent)" />
        <circle cx="28" cy="26" r="3" fill="var(--accent)" />
        <line
          x1="8"
          y1="28"
          x2="48"
          y2="28"
          stroke="var(--accent)"
          strokeOpacity="0.5"
        />
      </svg>
    );
  return (
    <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
      <polygon points="28,6 50,42 6,42" fill="none" stroke="var(--accent)" />
      <circle cx="28" cy="30" r="3" fill="var(--accent)" />
      <circle cx="20" cy="36" r="2" fill="var(--accent)" opacity="0.6" />
      <circle cx="36" cy="36" r="2" fill="var(--accent)" opacity="0.6" />
    </svg>
  );
}

// ─── Archetype Section ───────────────────────────────────────────
interface ArchetypeSectionProps {
  icp: string;
  setIcp: (id: string) => void;
}

export default function ArchetypeSection({ icp, setIcp }: ArchetypeSectionProps) {
  const archetypes = SOLARIS_ARCHETYPES;
  return (
    <section
      className="section"
      id="archetypes"
      style={{ background: "var(--bg-2)" }}
    >
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">05 · solutions by profile</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Entropy hits
            <br />
            every model differently.
            <br />
            <em>Find yours.</em>
          </h2>
        </div>
        <p className="s-sub">
          Four agency archetypes. Four named pains. Four pre-configured
          factories. Pick your profile — your Solaris instance is already built.
        </p>
      </div>
      <div className="archetype-grid">
        {archetypes.map((a) => (
          <article
            key={a.id}
            className={
              "archetype" +
              (icp === a.id ? " current" : "") +
              (a.recommended ? " recommended" : "")
            }
            onClick={() => setIcp(a.id)}
          >
            {a.recommended && (
              <div className="reco-badge">PRIORITY · WAVE 01</div>
            )}
            <div className="arch-head">
              <div className="arch-code">
                <span className="ix">{a.code}</span>
                <span className="full">{a.fullName}</span>
              </div>
              <div className="arch-glyph">
                <ArchGlyph id={a.id} />
              </div>
            </div>
            <h3 className="arch-name">{a.name}</h3>
            <div className="arch-tag">{a.tag}</div>

            <div className="arch-pain">
              <div className="k">⚠ Your pain · {a.painName}</div>
              <p>{a.painDesc}</p>
            </div>

            <div className="arch-remedy">
              <div className="k">↻ The Solaris remedy · {a.remedyName}</div>
              <p>{a.remedyDesc}</p>
            </div>

            <div className="arch-pitch">{a.pitch}</div>

            <ul className="arch-targets">
              {a.targets.map((t, i) => (
                <li key={i}>
                  <span className="k">{t.k}</span>
                  <span className="v">{t.v}</span>
                </li>
              ))}
              {a.ticket && (
                <li>
                  <span className="k">Ticket</span>
                  <span className="v" style={{ color: "var(--accent-2)" }}>
                    {a.ticket}
                  </span>
                </li>
              )}
            </ul>

            <div className="arch-footer">
              {icp === a.id
                ? "✓ active profile in the vault"
                : "→ this is my profile"}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
