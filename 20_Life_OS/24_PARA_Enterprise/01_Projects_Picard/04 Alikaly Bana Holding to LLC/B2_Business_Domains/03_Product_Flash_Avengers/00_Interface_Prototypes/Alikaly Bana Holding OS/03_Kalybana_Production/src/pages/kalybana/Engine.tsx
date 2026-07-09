import { Shield, Database, Network, ShieldCheck } from 'lucide-react';

export default function Engine() {
  return (
    <div className="w-full">
      {/* Monolith Header */}
      <section className="w-full bg-surface-container-low px-8 md:px-12 py-24 flex flex-col md:flex-row justify-between items-end gap-8 border-b border-outline-variant/20">
        <div className="max-w-4xl">
          <span className="font-label text-secondary uppercase tracking-[0.2em] text-xs mb-4 block">Proprietary Technology Deep Dive</span>
          <h1 className="font-headline text-5xl md:text-7xl font-bold text-primary-fixed leading-none tracking-tighter">The Engine of Sovereignty.</h1>
        </div>
        <div className="font-label text-left md:text-right">
          <p className="text-on-surface-variant text-xs uppercase tracking-widest mb-2">Technical Status</p>
          <p className="text-primary-fixed text-sm font-bold tracking-widest">V4.82 BUILD: STABLE</p>
        </div>
      </section>

      {/* Technical Visualization Section */}
      <section className="px-8 md:px-12 py-24">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          {/* Visualization Canvas */}
          <div className="lg:col-span-8 relative aspect-video bg-surface-container-lowest overflow-hidden group border border-outline-variant/20">
            {/* Stylized Technical Dashboard Mockup */}
            <div className="absolute inset-0 opacity-40 grayscale group-hover:grayscale-0 transition-all duration-700 bg-surface-variant">
            </div>
            
            {/* Overlay Grid */}
            <div className="absolute inset-0 grid grid-cols-6 grid-rows-6 pointer-events-none">
              {[...Array(36)].map((_, i) => (
                <div key={i} className="border-r border-b border-white/5"></div>
              ))}
            </div>
            
            {/* Centered Glass Logic Label */}
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="glass-panel p-8 text-center border border-white/10 max-w-md">
                <Shield className="text-secondary w-10 h-10 mx-auto mb-4" strokeWidth={1.5} />
                <h3 className="font-headline text-2xl text-primary-fixed mb-2 tracking-tight">Immutable Protocol</h3>
                <p className="font-body text-on-surface-variant text-sm">Visual architecture redacted for proprietary protection. Core logic operating within encrypted TEE environments.</p>
                <div className="mt-6 font-label text-[10px] text-secondary tracking-[0.3em] uppercase">Status: Operating @ Tier 1 Efficiency</div>
              </div>
            </div>
          </div>

          {/* Technical Stats Column */}
          <div className="lg:col-span-4 flex flex-col gap-12">
            <div className="space-y-2">
              <span className="font-label text-xs uppercase tracking-widest text-on-surface-variant">Asset Integrity</span>
              <div className="text-5xl font-label font-bold text-secondary tracking-tighter">$45M+</div>
              <p className="font-body text-on-surface-variant text-sm border-t border-outline-variant/20 pt-4">Assets recovered through proprietary scanning and automated ledger verification protocols.</p>
            </div>
            <div className="space-y-2">
              <span className="font-label text-xs uppercase tracking-widest text-on-surface-variant">Scan Velocity</span>
              <div className="text-5xl font-label font-bold text-primary-fixed tracking-tighter">150+</div>
              <p className="font-body text-on-surface-variant text-sm border-t border-outline-variant/20 pt-4">Properties scanned and indexed daily by the autonomous node network across global jurisdictions.</p>
            </div>
            <div className="mt-auto p-6 bg-surface-container border-l-2 border-secondary">
              <p className="font-label text-[10px] uppercase tracking-widest text-secondary mb-2">Direct Terminal Access</p>
              <p className="font-body text-xs text-on-surface-variant italic">"Architecture mirrors a sovereign ledger—once a recovery vector is identified, the protocol executes without human latency."</p>
            </div>
          </div>
        </div>
      </section>

      {/* Technical Deep Dive Bento Grid */}
      <section className="px-8 md:px-12 pb-32">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Data Source Layer */}
          <div className="bg-surface-container p-10 flex flex-col justify-between aspect-square border border-outline-variant/10">
            <div>
              <span className="font-label text-[10px] text-on-surface-variant tracking-[0.2em] uppercase block mb-4">Module 01</span>
              <h4 className="font-headline text-2xl text-primary-fixed mb-4 tracking-tight">Ingestion Engine</h4>
              <p className="font-body text-sm text-on-surface-variant leading-relaxed">Multi-threaded API connectors interfacing with global land registries and digital asset repositories simultaneously.</p>
            </div>
            <div className="flex items-center gap-4 pt-8 border-t border-outline-variant/20">
              <Database className="text-secondary w-5 h-5" strokeWidth={1.5} />
              <span className="font-label text-xs text-secondary tracking-widest uppercase">Supabase Pro Tier</span>
            </div>
          </div>

          {/* Logic Layer */}
          <div className="bg-surface-container-high p-10 flex flex-col justify-between aspect-square md:scale-105 z-10 border border-outline-variant/20 shadow-2xl">
            <div>
              <span className="font-label text-[10px] text-secondary tracking-[0.2em] uppercase block mb-4">Module 02</span>
              <h4 className="font-headline text-2xl text-primary-fixed mb-4 tracking-tight">Workflow Orchestration</h4>
              <p className="font-body text-sm text-on-surface-variant leading-relaxed">Complex conditional logic branching that mirrors the 'n8n' philosophy—automating legal filings and recovery scripts.</p>
            </div>
            <div className="flex items-center gap-4 pt-8 border-t border-outline-variant/20">
              <Network className="text-secondary w-5 h-5" strokeWidth={1.5} />
              <span className="font-label text-xs text-secondary tracking-widest uppercase">Active Orchestrator</span>
            </div>
          </div>

          {/* Verification Layer */}
          <div className="bg-surface-container p-10 flex flex-col justify-between aspect-square border border-outline-variant/10">
            <div>
              <span className="font-label text-[10px] text-on-surface-variant tracking-[0.2em] uppercase block mb-4">Module 03</span>
              <h4 className="font-headline text-2xl text-primary-fixed mb-4 tracking-tight">Audit Finality</h4>
              <p className="font-body text-sm text-on-surface-variant leading-relaxed">Triple-entry accounting verified against decentralized trust layers to ensure 100% recovery accuracy.</p>
            </div>
            <div className="flex items-center gap-4 pt-8 border-t border-outline-variant/20">
              <ShieldCheck className="text-secondary w-5 h-5" strokeWidth={1.5} />
              <span className="font-label text-xs text-secondary tracking-widest uppercase">Verified Ledger</span>
            </div>
          </div>
        </div>
      </section>

      {/* Final Call to Technical Trust */}
      <section className="bg-surface-container-lowest py-32 border-t border-outline-variant/10">
        <div className="max-w-4xl mx-auto text-center px-8">
          <span className="font-label text-xs text-secondary uppercase tracking-[0.4em] mb-6 block">Technological Authority</span>
          <h2 className="font-headline text-4xl md:text-6xl text-primary-fixed mb-12 leading-tight tracking-tighter">Trust is mathematical. We simply provide the proof.</h2>
          <div className="flex flex-col md:flex-row gap-6 justify-center">
            <button className="bg-primary-fixed text-on-primary-fixed px-10 py-4 font-label text-xs uppercase tracking-widest hover:bg-white transition-all">
              Request Architecture Briefing
            </button>
            <button className="border border-outline-variant/40 text-primary-fixed px-10 py-4 font-label text-xs uppercase tracking-widest hover:bg-surface-container transition-all">
              View Performance Audit
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}
