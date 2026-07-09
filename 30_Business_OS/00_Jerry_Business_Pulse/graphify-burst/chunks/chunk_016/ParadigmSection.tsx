import { SOLARIS_PARADIGMS } from "@/lib/data";

export default function ParadigmSection() {
  const paradigms = SOLARIS_PARADIGMS;
  return (
    <section className="section" id="paradigms">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">06 · the 2026 levers</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Agencies no longer<br />believe in <em>tools.</em>
          </h2>
        </div>
        <p className="s-sub">
          You believe in{" "}
          <b style={{ color: "var(--ink)", fontWeight: 500 }}>system guarantees</b>.
          Three levers Solaris unlocks for you — each one shatters an old
          belief about what an agency is supposed to be.
        </p>
      </div>
      <div className="paradigm-grid">
        {paradigms.map((p) => (
          <div className="paradigm" key={p.n}>
            <div className="paradigm-n">{p.n}</div>
            <div className="paradigm-anchor">
              <span className="from">{p.anchor.split("→")[0].trim()}</span>
              <span className="arrow">→</span>
              <span className="to">{p.anchor.split("→")[1].trim()}</span>
            </div>
            <h3 className="paradigm-name">{p.name}</h3>
            <p className="paradigm-promise">{p.promise}</p>
            <div className="paradigm-mech">
              <div className="k">How</div>
              <p>{p.mechanism}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
