export default function HookSection() {
  return (
    <section className="section" id="hook">
      <div className="aaas">
        <div>
          <div className="eyebrow">01 · the positioning</div>
          <h2
            className="display"
            style={{
              fontSize: "clamp(40px, 5.5vw, 80px)",
              margin: "20px 0 0",
              lineHeight: 1,
            }}
          >
            You sell the
            <br />
            strategy.
            <br />
            <em>
              We execute
              <br />
              in silence.
            </em>
          </h2>
        </div>
        <div className="aaas-prose">
          <p style={{ fontSize: 19 }}>
            Solaris is a white-label{" "}
            <b style={{ color: "var(--accent)", fontWeight: 500 }}>
              Agency-as-a-Service
            </b>{" "}
            production infrastructure. A ghost factory running under your logo —
            never visible to your clients.
          </p>
          <p>
            You keep the relationship, the brief, the invoice. We run extraction,
            production, QA, delivery. Your clients don&apos;t even know we exist.
          </p>
          <div className="compare">
            <div className="compare-cell bad">
              <h4>The old model</h4>
              <ul>
                <li>
                  <span className="sym">·</span>Hire, train, manage, lose
                </li>
                <li>
                  <span className="sym">·</span>Freelancers ghost you on Mondays
                </li>
                <li>
                  <span className="sym">·</span>Endless sync meetings
                </li>
                <li>
                  <span className="sym">·</span>Margin eaten by salaries
                </li>
              </ul>
            </div>
            <div className="compare-cell good">
              <h4>You · on Solaris</h4>
              <ul>
                <li>
                  <span className="sym">+</span>A full org chart ready in 24h
                </li>
                <li>
                  <span className="sym">+</span>Agents that never sleep
                </li>
                <li>
                  <span className="sym">+</span>Zero meetings · async orders
                </li>
                <li>
                  <span className="sym">+</span>70% margin, mathematically
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
