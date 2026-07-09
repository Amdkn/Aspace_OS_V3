import { SOLARIS_ANATOMY } from "@/lib/data";

export default function AnatomySection() {
  const anatomy = SOLARIS_ANATOMY;
  return (
    <section className="section" id="anatomy">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">02 · the anatomy of your strike force</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Forget the
            <br />
            job descriptions.
            <br />
            <em>Meet your new team.</em>
          </h2>
        </div>
        <p className="s-sub">
          Your Solaris infrastructure is split into 8 expertise poles, run by a
          strict and invisible hierarchy that never sleeps. Three tiers, three
          codenames, one single org chart.
        </p>
      </div>

      <div className="anatomy-stack">
        {anatomy.map((tier, i) => (
          <div
            className="anatomy-tier"
            key={tier.tier}
            data-tier={tier.tier.toLowerCase()}
          >
            <div className="anatomy-side">
              <div className="anatomy-tier-id">{tier.tier}</div>
              <div className="anatomy-codename">{tier.codename}</div>
              <div className="anatomy-meta">{tier.headcount}</div>
            </div>
            <div className="anatomy-body">
              <div className="anatomy-role">{tier.role}</div>
              <h3 className="anatomy-name">{tier.name}</h3>
              <p className="anatomy-desc">{tier.desc}</p>
              {tier.members && (
                <div className="anatomy-roster">
                  <div className="anatomy-roster-label">
                    Current {tier.tier} roster
                  </div>
                  <div className="anatomy-chips">
                    {tier.members.map((m) => (
                      <span key={m} className="anatomy-chip">
                        {tier.tier}.{m}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
            <div className="anatomy-flow">
              {i < anatomy.length - 1 && (
                <>
                  <div className="anatomy-arrow">↓</div>
                  <div className="anatomy-flow-label">delegates to</div>
                </>
              )}
              {i === anatomy.length - 1 && (
                <>
                  <div
                    className="anatomy-arrow"
                    style={{ color: "var(--mint)" }}
                  >
                    ✓
                  </div>
                  <div className="anatomy-flow-label">ships to you</div>
                </>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
