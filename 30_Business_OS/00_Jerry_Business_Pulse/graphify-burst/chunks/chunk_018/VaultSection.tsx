"use client";

import { SOLARIS_ARCHETYPES, VAULT_BY_ARCH } from "@/lib/data";

interface VaultSectionProps {
  icp: string;
}

export default function VaultSection({ icp }: VaultSectionProps) {
  const v = VAULT_BY_ARCH[icp] || VAULT_BY_ARCH.aaa;
  const arch = SOLARIS_ARCHETYPES.find((a) => a.id === icp) || SOLARIS_ARCHETYPES[2];

  return (
    <section className="section" id="vault">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">07 · onboarding · zero friction, zero calls</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            We don&apos;t do<br />discovery calls.<br /><em>Time is non-renewable.</em>
          </h2>
        </div>
        <p className="s-sub">
          Three async steps. No calendar. No sales follow-up. You read, you
          decide, you activate. Your new team is ready to take its first work
          order within 48 hours.
        </p>
      </div>
      <div className="vault-wrap">
        <div className="vault-mock">
          <div className="vault-chrome">
            <div className="dots"><div className="dot" /><div className="dot" /><div className="dot" /></div>
            <div className="url">vault.solaris.factory / {v.slug} / 7f3a-2c81</div>
            <div className="lock">⬢ TLS · async · 2-FA</div>
          </div>
          <div className="vault-body">
            <div className="vault-greet">
              <b>{v.lead}</b> · {arch.code} · audit delivered · {new Date().toLocaleDateString("en-US", { day: "2-digit", month: "short" })}
            </div>
            <h3 className="vault-title">
              Friction report.<br />
              <span style={{ color: "var(--accent-2)", fontStyle: "italic" }}>{v.headline}</span>
            </h3>
            <div className="vault-audit">
              {v.rows.map((a, i) => (
                <div className="vault-audit-row" key={i}>
                  <div className="label">{a.l}</div>
                  <div className={"sev " + a.s}>{a.s === "high" ? "critical" : a.s === "med" ? "moderate" : "minor"}</div>
                  <div className="ms">{a.t}</div>
                </div>
              ))}
            </div>
            <div style={{ fontFamily: "var(--font-mono)", fontSize: 11, letterSpacing: "0.15em", textTransform: "uppercase" as const, color: "var(--ink-3)", padding: "12px 14px", border: "1px solid var(--line)", borderRadius: 4, background: "var(--surface-2)" }}>
              <div style={{ color: "var(--ink-4)", marginBottom: 6 }}>Pre-configured remedy</div>
              <div style={{ color: "var(--accent)", textTransform: "none" as const, letterSpacing: 0, fontSize: 13 }}>↻ {v.remedy}</div>
            </div>
            <div className="vault-actions">
              <div className="vault-action">
                <div className="k">Action / 01</div>
                <div className="v">Review the architecture plan</div>
              </div>
              <div className="vault-action primary">
                <div className="k">Action / 02</div>
                <div className="v">Activate my factory →</div>
              </div>
            </div>
          </div>
        </div>

        <div className="vault-steps">
          <div className="vault-step done">
            <div className="step-meta">
              <span className="num">STEP / 01</span>
              <span className="when">D · now</span>
            </div>
            <h4>The Silent Audit</h4>
            <p>Drop your URL or your operational bottleneck through our portal. No 40-question form. No call. You post, we take it from there.</p>
          </div>
          <div className="vault-step done">
            <div className="step-meta">
              <span className="num">STEP / 02</span>
              <span className="when">D+1 · &lt;24h</span>
            </div>
            <h4>The Sanctuary</h4>
            <p>You get an encrypted link to a secure space. Inside: the friction report on your agency drafted by our B2 VPs, plus the exact architecture plan of your future factory. Read at your own pace.</p>
          </div>
          <div className="vault-step">
            <div className="step-meta">
              <span className="num">STEP / 03</span>
              <span className="when">on your signal</span>
            </div>
            <h4>Activation</h4>
            <p>You sign off. The B1/B2/B3 hierarchy is instantiated and wired into your comms channels (Slack/Teams). Your new async team is ready to take its first work order.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
