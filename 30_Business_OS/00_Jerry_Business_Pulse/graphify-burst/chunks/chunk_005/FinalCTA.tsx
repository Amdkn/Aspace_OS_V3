import LeadForm from "./LeadForm";

export default function FinalCTA() {
  return (
    <section className="cta" id="vault-form">
      <div className="cta-sun" />
      <div className="eyebrow" style={{ justifyContent: "center", display: "inline-flex" }}>
        wave 01 · live · ohio / kentucky
      </div>
      <h2 style={{ marginTop: 32 }}>
        Plug in.<br /><em>Once.</em>
      </h2>
      <p className="sub">
        No call. No SaaS to rent. No freelance to manage. One URL, one audit,
        one vault — your new async team is waiting for its first order.
      </p>

      <div style={{ display: "flex", justifyContent: "center", marginTop: 32 }}>
        <LeadForm />
      </div>

      <div className="hero-cta-row" style={{ justifyContent: "center", marginTop: 24 }}>
        <a className="btn-ghost" href="mailto:hello@solaris.factory">
          or contact the factory
        </a>
      </div>
    </section>
  );
}
