// Symphony × Agent OS — Dashboard JS (with intelligent sidebar)
// Polls /api/* endpoints, renders live updates + intelligence.

const PHASE_ORDER = ["WAKE", "PROBE", "DECIDE", "EXECUTE", "OBSERVE", "LEARN", "SIGNAL", "SLEEP"];
const TREND_ARROWS = { up: "▲", down: "▼", stable: "→" };

let lastPulseCount = 0;
let lastIntelligenceKey = "";
let autoRefresh = true;
let pollInterval = null;
let tickInProgress = false;
let activePhaseFilter = null; // when set, pulse stream only shows this phase

// --- Helpers ---
async function fetchJSON(path) {
    const res = await fetch(path);
    if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`);
    return res.json();
}

function escapeHtml(str) {
    if (str == null) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function formatTime(isoStr) {
    if (!isoStr) return "—";
    try {
        const d = new Date(isoStr);
        return d.toLocaleTimeString("en-GB", { hour12: false });
    } catch { return isoStr; }
}

function detectGateClass(decision) {
    if (!decision) return "";
    if (/PASS/i.test(decision) && !/BLOCKED/i.test(decision)) return "pass";
    if (/BLOCKED/i.test(decision)) return "blocked";
    if (/CONDITIONAL/i.test(decision)) return "cond";
    return "";
}

function trendClass(trend) {
    if (trend === "up") return "up";
    if (trend === "down") return "down";
    return "stable";
}

// --- Clock ---
function updateClock() {
    const now = new Date();
    document.getElementById("clock").textContent = now.toLocaleTimeString("en-GB", { hour12: false });
}
setInterval(updateClock, 1000);
updateClock();

// === COLLAPSIBLE SECTIONS ===
function wireCollapsibles() {
    document.querySelectorAll(".section-header[data-toggle]").forEach(header => {
        if (header.dataset.wired) return;
        header.dataset.wired = "true";
        header.addEventListener("click", () => {
            const section = header.closest(".sidebar-section");
            section.classList.toggle("collapsed");
        });
    });
}

// === SIDEBAR: SUGGESTIONS (always visible) ===
async function renderSuggestions(data) {
    const list = document.getElementById("suggestions-list");
    const countEl = document.getElementById("suggestions-count");
    countEl.textContent = data.suggestions.length;
    // Set count color
    const maxLevel = data.suggestions.reduce((m, s) => {
        const rank = { warn: 3, info: 2, ok: 1 }[s.level] || 0;
        return Math.max(m, rank);
    }, 0);
    countEl.className = "section-count " + ({ 3: "warn", 2: "info", 1: "ok" }[maxLevel] || "");

    if (data.suggestions.length === 0) {
        list.innerHTML = `<p class="empty">No suggestions</p>`;
        return;
    }
    list.innerHTML = data.suggestions.map(s =>
        `<div class="suggestion ${s.level}">
            <span class="text">${escapeHtml(s.text)}</span>
        </div>`
    ).join("");
}

// === SIDEBAR: VIOLATIONS (D2 ADR-SYMPH-003) ===
async function renderViolations(data) {
    const list = document.getElementById("violations-list");
    const countEl = document.getElementById("violations-count");
    countEl.textContent = data.violations.length;
    countEl.className = "section-count " + (data.violations.some(v => v.level === "warn") ? "warn" : data.violations.length > 0 ? "info" : "");

    if (data.violations.length === 0) {
        list.innerHTML = `<div class="violation" style="opacity: 0.6; border-left-color: var(--green);">
            <div class="type">✅ no D2 violation</div>
        </div>`;
        return;
    }
    list.innerHTML = data.violations.map(v => `
        <div class="violation ${v.level}">
            <div class="type">${escapeHtml(v.type)}</div>
            <div>${escapeHtml(v.message)}</div>
        </div>
    `).join("");
}

// === SIDEBAR: TRENDS ===
async function renderTrends(data) {
    const t = data.trends;
    document.getElementById("trends-count").textContent = `${t.ticks_analyzed} tick${t.ticks_analyzed !== 1 ? 's' : ''}`;
    document.getElementById("trend-cost").textContent = `$${t.last_cost_usd.toFixed(4)}`;
    document.getElementById("trend-cost-arrow").textContent = TREND_ARROWS[t.cost_trend];
    document.getElementById("trend-cost-arrow").className = "trend-arrow " + trendClass(t.cost_trend);
    document.getElementById("trend-duration").textContent = `${t.last_total_duration_ms}ms`;
    document.getElementById("trend-duration-arrow").textContent = TREND_ARROWS[t.duration_trend];
    document.getElementById("trend-duration-arrow").className = "trend-arrow " + trendClass(t.duration_trend);
}

// === SIDEBAR: STANDARDS COVERAGE ===
async function renderCoverage(data) {
    const d = data.drift;
    const total = d.total_standards;
    const used = d.used.length;
    const unused = d.unused.length;
    document.getElementById("coverage-count").textContent = `${used} / ${total}`;
    document.getElementById("coverage-used").textContent = `${used} used`;
    document.getElementById("coverage-unused").textContent = `${unused} unused`;
    document.getElementById("coverage-fill").style.width = total > 0 ? `${(used / total * 100).toFixed(0)}%` : "0%";

    // List all standards with used/unused visual
    const allStds = [...d.used, ...d.unused].sort();
    const list = document.getElementById("coverage-unused-list");
    list.innerHTML = allStds.map(s => {
        const isUsed = d.used.includes(s);
        return `<span class="std-chip ${isUsed ? 'used' : ''}" title="${isUsed ? 'Used in last tick' : 'Not used in last tick (drift!)'}">${escapeHtml(s.replace('.md', ''))}</span>`;
    }).join("");
}

// === SIDEBAR: PHASE HEALTH ===
async function renderPhaseHealth(data) {
    const per = data.trends.per_phase || {};
    const body = document.getElementById("phases-body");
    document.getElementById("phases-count").textContent = PHASE_ORDER.length;
    body.innerHTML = PHASE_ORDER.map(phase => {
        const s = per[phase] || { avg: 0, count: 0, warn: false };
        const isActive = activePhaseFilter === phase;
        return `
            <div class="phase-row phase-${phase} ${s.warn ? 'warn' : ''} ${isActive ? 'active' : ''}"
                 data-phase="${phase}" title="Click to ${isActive ? 'clear filter' : 'filter pulse by ' + phase}">
                <span class="dot"></span>
                <span class="name">${phase}</span>
                <span class="ms">${s.avg ? s.avg.toFixed(0) + 'ms' : '—'}</span>
            </div>
        `;
    }).join("");

    body.querySelectorAll(".phase-row").forEach(row => {
        row.addEventListener("click", () => {
            const phase = row.dataset.phase;
            if (activePhaseFilter === phase) {
                activePhaseFilter = null;
            } else {
                activePhaseFilter = phase;
            }
            renderPulse();
            // Re-render to show active state
            body.querySelectorAll(".phase-row").forEach(r => {
                r.classList.toggle("active", r.dataset.phase === activePhaseFilter);
            });
        });
    });
}

// === SIDEBAR: RECENT DECISIONS ===
async function renderDecisions() {
    const data = await fetchJSON("/api/recent-decisions?n=5");
    const body = document.getElementById("decisions-body");
    document.getElementById("decisions-count").textContent = data.decisions.length;
    if (data.decisions.length === 0) {
        body.innerHTML = `<p class="empty">No decisions yet</p>`;
        return;
    }
    body.innerHTML = data.decisions.map(d => `
        <div class="decision-row gate-${d.gate}">
            <div class="head">
                <span class="phase">${escapeHtml(d.phase)}</span>
                <span class="gate">${d.gate}</span>
            </div>
            <div class="decision">${escapeHtml(d.decision)}</div>
        </div>
    `).join("");
}

// === MAIN: PULSE STREAM ===
async function renderPulse() {
    const data = await fetchJSON("/api/pulse?last=200");
    const stream = document.getElementById("pulse-stream");
    let lines = data.lines;
    if (activePhaseFilter) {
        lines = lines.filter(l => l.phase === activePhaseFilter);
    }
    document.getElementById("pulse-counter").textContent = activePhaseFilter
        ? `${lines.length} (filter: ${activePhaseFilter})`
        : `${data.count} / ${data.total_in_file}`;

    if (data.lines.length === 0) {
        if (!stream.querySelector(".empty")) {
            stream.innerHTML = `<p class="empty">No pulses yet. Click <strong>▶ Trigger tick</strong> to run a demo.</p>`;
        }
        return;
    }
    // Only re-render if count changed OR filter changed
    const renderKey = `${data.count}|${activePhaseFilter || ""}`;
    if (renderKey === lastPulseCount) return;
    lastPulseCount = renderKey;

    stream.innerHTML = "";
    lines.forEach(line => {
        const div = document.createElement("div");
        const phaseClass = `phase-${line.phase || "UNKNOWN"}`;
        const isError = line.error && line.error !== null;
        div.className = `pulse-line ${phaseClass}` + (isError ? " error" : "");

        const meta = [];
        if (line.duration_ms) meta.push(`<span class="duration">${line.duration_ms}ms</span>`);
        if (line.cost_delta_usd != null) meta.push(`<span class="cost">+$${line.cost_delta_usd.toFixed(4)}</span>`);
        if (line.cumulative_cost_usd != null) meta.push(`Σ $${line.cumulative_cost_usd.toFixed(4)}`);
        if (line.issue_id) meta.push(`issue: ${escapeHtml(line.issue_id)}`);
        if (isError) meta.push(`<span style="color: var(--red);">ERROR</span>`);

        div.innerHTML = `
            <div class="phase">${escapeHtml(line.phase || "?")}</div>
            <div class="decision" title="${escapeHtml(line.decision || "")}">${escapeHtml(line.decision || "")}</div>
            <div class="meta">${meta.join(" · ")}</div>
        `;
        stream.appendChild(div);
    });
    stream.scrollTop = stream.scrollHeight;
}

// === MAIN: COST & DURATION CHARTS ===
async function renderCharts() {
    const data = await fetchJSON("/api/phase-stats");
    const totalCost = data.phases.reduce((s, p) => s + p.total_cost_delta, 0);
    const totalDuration = data.phases.reduce((s, p) => s + p.total_duration_ms, 0);

    document.getElementById("cost-total").textContent = `$${totalCost.toFixed(4)}`;
    document.getElementById("duration-total").textContent = `${totalDuration} ms`;

    const maxCost = Math.max(...data.phases.map(p => p.total_cost_delta), 0.0001);
    const maxDur = Math.max(...data.phases.map(p => p.avg_duration_ms), 1);

    const renderBar = (phase, value, max, suffix, decimals = 4) => {
        const pct = (value / max) * 100;
        return `
            <div class="bar-row phase-${phase.phase}">
                <div class="label" style="color: ${phase.color}">${phase.phase}</div>
                <div class="bar-container">
                    <div class="bar" style="width: ${pct.toFixed(1)}%;"></div>
                </div>
                <div class="value">${decimals === 0 ? Math.round(value) : value.toFixed(decimals)}${suffix}</div>
            </div>
        `;
    };

    if (data.phases.every(p => p.count === 0)) return;

    document.getElementById("cost-chart").innerHTML = data.phases
        .filter(p => p.count > 0)
        .map(p => renderBar(p, p.total_cost_delta, maxCost, " USD"))
        .join("");

    document.getElementById("duration-chart").innerHTML = data.phases
        .filter(p => p.count > 0)
        .map(p => renderBar(p, p.avg_duration_ms, maxDur, " ms", 0))
        .join("");
}

// === MAIN: SNAPSHOT ===
async function renderSnapshot() {
    try {
        const snap = await fetchJSON("/api/snapshot");
        const body = document.getElementById("snapshot-body");
        document.getElementById("snapshot-tick-id").textContent = snap.last_tick_id || "—";

        const gateClass = detectGateClass(snap.last_decision);

        body.innerHTML = `
            <div class="snapshot-grid">
                <div class="snapshot-card">
                    <div class="k">Workflow</div>
                    <div class="v">${escapeHtml(snap.workflow_id || "—")}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Tick count</div>
                    <div class="v">${snap.tick_count}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Layer</div>
                    <div class="v">${escapeHtml(snap.aspace_layer || "—")}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Total cost</div>
                    <div class="v">$${snap.cumulative_cost_usd_total.toFixed(4)}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Last decision</div>
                    <div class="v ${gateClass}">${escapeHtml(snap.last_decision || "—")}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Standards used</div>
                    <div class="v">
                        ${snap.standards_used.length === 0
                            ? "—"
                            : `<div class="standards-list-inline">
                                ${snap.standards_used.map(s => `<span class="std-tag">${escapeHtml(s)}</span>`).join("")}
                               </div>`
                        }
                    </div>
                </div>
                <div class="snapshot-card">
                    <div class="k">Phases seen</div>
                    <div class="v" style="font-size: 10px;">${Object.entries(snap.phases_seen).map(([p, c]) => `${p}:${c}`).join(" · ") || "—"}</div>
                </div>
                <div class="snapshot-card">
                    <div class="k">SLEEP</div>
                    <div class="v" style="font-size: 10px;">${escapeHtml(snap.last_sleep_decision || "—")}</div>
                </div>
            </div>
        `;
    } catch (e) { console.error("snapshot error:", e); }
}

// === MAIN: RENDER ALL ===
async function renderAll() {
    if (!autoRefresh) return;
    try {
        const intel = await fetchJSON("/api/intelligence");
        const intelKey = JSON.stringify({s: intel.suggestions.length, v: intel.violations.length, t: intel.trends.ticks_analyzed, c: intel.trends.cost_trend, d: intel.trends.duration_trend});
        if (intelKey !== lastIntelligenceKey) {
            lastIntelligenceKey = intelKey;
            renderSuggestions(intel);
            renderViolations(intel);
            renderTrends(intel);
            renderCoverage(intel);
            renderPhaseHealth(intel);
            renderDecisions();
        }
        await Promise.allSettled([renderPulse(), renderCharts(), renderSnapshot()]);
        document.getElementById("last-refresh").textContent = `last refresh: ${new Date().toLocaleTimeString("en-GB", { hour12: false })}`;
    } catch (e) {
        console.error("renderAll error:", e);
    }
}

// === TRIGGER TICK ===
async function triggerTick() {
    if (tickInProgress) return;
    tickInProgress = true;
    const btn = document.getElementById("trigger-tick");
    btn.disabled = true;
    btn.textContent = "⏳ Running…";
    document.getElementById("status-indicator").style.color = "var(--yellow)";

    try {
        const res = await fetchJSON("/api/tick");
        console.log("tick triggered:", res);
        for (let i = 0; i < 20; i++) {
            await new Promise(r => setTimeout(r, 500));
            await renderAll();
        }
    } catch (e) {
        alert(`Tick failed: ${e.message}`);
    } finally {
        tickInProgress = false;
        btn.disabled = false;
        btn.textContent = "▶ Trigger tick";
        document.getElementById("status-indicator").style.color = "var(--green)";
    }
}

// === WIRE UP ===
document.getElementById("trigger-tick").addEventListener("click", triggerTick);
document.getElementById("refresh").addEventListener("click", renderAll);
document.getElementById("auto-refresh").addEventListener("change", (e) => {
    autoRefresh = e.target.checked;
    if (autoRefresh) {
        pollInterval = setInterval(renderAll, 1500);
    } else if (pollInterval) {
        clearInterval(pollInterval);
        pollInterval = null;
    }
});

// === INIT ===
(async () => {
    wireCollapsibles();
    await renderAll();
    pollInterval = setInterval(renderAll, 1500);
})();
