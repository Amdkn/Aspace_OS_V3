"use client";

import { useState } from "react";

type Status = "idle" | "submitting" | "success" | "error";

const ARCHETYPES = [
  { id: "forges", label: "Content / media factory" },
  { id: "revops", label: "RevOps / performance" },
  { id: "aaa", label: "AI automation agency" },
  { id: "boutiques", label: "Strategy boutique" },
] as const;

function readUtm(): Record<string, string> {
  if (typeof window === "undefined") return {};
  const p = new URLSearchParams(window.location.search);
  const out: Record<string, string> = {};
  for (const k of ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "ref"]) {
    const v = p.get(k);
    if (v) out[k] = v;
  }
  return out;
}

export default function LeadForm() {
  const [status, setStatus] = useState<Status>("idle");
  const [errorFields, setErrorFields] = useState<string[]>([]);

  async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (status === "submitting") return;
    setStatus("submitting");
    setErrorFields([]);

    const form = e.currentTarget;
    const fd = new FormData(form);
    const payload = {
      url: String(fd.get("url") ?? ""),
      email: String(fd.get("email") ?? ""),
      archetype: String(fd.get("archetype") ?? ""),
      company_website: String(fd.get("company_website") ?? ""), // honeypot
      utm: readUtm(),
    };

    try {
      const res = await fetch("/api/leads", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data.ok) {
        setStatus("success");
        form.reset();
      } else {
        setErrorFields(Array.isArray(data.fields) ? data.fields : []);
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  }

  if (status === "success") {
    return (
      <div className="lead-form lead-form--done" role="status">
        <h3 style={{ margin: 0 }}>Order received. ☀</h3>
        <p className="sub" style={{ marginTop: 8 }}>
          Your friction audit is queued. The factory replies within 48 hours — no call, no follow-up.
        </p>
      </div>
    );
  }

  return (
    <form className="lead-form" onSubmit={onSubmit} noValidate aria-label="Submit your agency for a friction audit">
      {/* Honeypot — hidden from humans, catches bots */}
      <input
        type="text"
        name="company_website"
        tabIndex={-1}
        autoComplete="off"
        aria-hidden="true"
        style={{ position: "absolute", left: "-9999px", width: 1, height: 1, opacity: 0 }}
      />

      <label className="lead-field">
        <span>Agency URL</span>
        <input
          name="url"
          type="text"
          inputMode="url"
          placeholder="acme-studio.com"
          required
          aria-invalid={errorFields.includes("url")}
        />
      </label>

      <label className="lead-field">
        <span>Work email</span>
        <input
          name="email"
          type="email"
          placeholder="you@acme-studio.com"
          required
          aria-invalid={errorFields.includes("email")}
        />
      </label>

      <label className="lead-field">
        <span>Your shape</span>
        <select name="archetype" defaultValue="forges">
          {ARCHETYPES.map((a) => (
            <option key={a.id} value={a.id}>
              {a.label}
            </option>
          ))}
        </select>
      </label>

      <button className="btn-primary" type="submit" disabled={status === "submitting"}>
        {status === "submitting" ? "sending…" : "submit your url"} <span className="arrow">→</span>
      </button>

      {status === "error" && (
        <p className="lead-error" role="alert">
          {errorFields.length
            ? `Check: ${errorFields.join(", ")}.`
            : "Couldn't reach the factory. Try again, or email hello@solaris.factory."}
        </p>
      )}
    </form>
  );
}
