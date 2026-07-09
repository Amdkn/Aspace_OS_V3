import { LockOpen, ArrowRight } from 'lucide-react';

export default function Compliance() {
  return (
    <div className="w-full">
      {/* Monolith Header */}
      <header className="w-full bg-surface-container-low px-8 md:px-12 py-24 flex flex-col md:flex-row justify-between items-end border-b border-outline-variant/20">
        <div className="max-w-4xl">
          <span className="font-label text-secondary uppercase tracking-[0.2em] text-xs mb-4 block">Governance & Access Control</span>
          <h1 className="font-headline text-6xl md:text-8xl font-bold tracking-tighter text-primary-fixed leading-none">THE SOVEREIGN LEDGER</h1>
        </div>
        <div className="mt-8 md:mt-0 text-left md:text-right">
          <p className="font-label text-on-surface-variant uppercase text-[10px] tracking-widest leading-loose">
            ESTABLISHED 2024<br/>
            ENCRYPTED NODE: 44.1.092<br/>
            SECURITY STATUS: OMNI
          </p>
        </div>
      </header>

      {/* Section 1: Managing Partner Bio (Minimalist) */}
      <section className="px-8 md:px-12 py-24 grid grid-cols-1 md:grid-cols-12 gap-12 border-b border-outline-variant/10">
        <div className="md:col-span-4">
          <div className="aspect-[3/4] bg-surface-container relative overflow-hidden border border-outline-variant/20">
            <div className="w-full h-full bg-surface-variant flex items-center justify-center">
               <LockOpen className="w-16 h-16 opacity-10" />
            </div>
            <div className="absolute bottom-0 left-0 p-8 bg-gradient-to-t from-background to-transparent w-full">
              <h2 className="font-headline text-3xl text-primary-fixed mb-2 tracking-tight">Kilian Van Der Meer</h2>
              <span className="font-label text-secondary text-xs uppercase tracking-widest">Managing Partner</span>
            </div>
          </div>
        </div>
        
        <div className="md:col-span-8 flex flex-col justify-center">
          <div className="max-w-2xl space-y-10">
            <span className="font-label text-on-surface-variant uppercase text-xs tracking-widest border-l-2 border-secondary pl-4">Leadership Mandate</span>
            <p className="font-body text-xl text-primary leading-relaxed">
              Van Der Meer oversees the strategic deployment of the Kalybana Engine. With twenty years of structural arbitrage experience, his focus remains on the preservation of capital through algorithmic rigidity and ethical governance.
            </p>
            <div className="grid grid-cols-2 gap-8 pt-8 border-t border-outline-variant/10">
              <div>
                <span className="font-label text-on-surface-variant text-[10px] uppercase block mb-2 tracking-widest">Primary Focus</span>
                <span className="font-body text-primary-fixed">Sovereign Debt Risk</span>
              </div>
              <div>
                <span className="font-label text-on-surface-variant text-[10px] uppercase block mb-2 tracking-widest">Board Seats</span>
                <span className="font-body text-primary-fixed">Aethelgard / Nexus IV</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Section 2: Gatekeeper Interface */}
      <section className="px-8 md:px-12 py-32 bg-surface-container-lowest relative overflow-hidden">
        <div className="absolute top-0 right-0 p-12 opacity-5 pointer-events-none">
          <span className="font-headline text-[20rem] font-black leading-none select-none">NO</span>
        </div>
        
        <div className="max-w-5xl mx-auto text-center space-y-12 relative z-10">
          <div className="inline-flex items-center space-x-4 border border-outline-variant/40 px-6 py-3">
            <LockOpen className="text-error w-5 h-5" strokeWidth={1.5} />
            <span className="font-label text-xs uppercase tracking-[0.3em] text-on-surface-variant">Gatekeeper Interface v2.0</span>
          </div>
          
          <h2 className="font-headline text-5xl md:text-7xl font-bold tracking-tight text-primary-fixed max-w-4xl mx-auto leading-[1.1]">
            We do not accept <br/>unsolicited solicitations.
          </h2>
          
          <div className="h-px w-24 bg-secondary mx-auto"></div>
          
          <p className="font-body text-on-surface-variant text-lg max-w-2xl mx-auto leading-relaxed italic">
            All acquisition inquiries and legal notifications must be directed through our authorized digital conduits. Standard contact forms have been deprecated to ensure transmission integrity.
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-px bg-outline-variant/20 mt-16 brutalist-border">
            <a href="mailto:legal@kalybana.com" className="bg-surface-container p-12 group transition-all duration-300 hover:bg-surface-container-high text-left block">
              <span className="font-label text-on-surface-variant text-[10px] uppercase block mb-4 tracking-widest">Legal Counsel</span>
              <span className="font-headline text-2xl text-primary-fixed block group-hover:text-secondary transition-colors underline underline-offset-8">legal@kalybana.com</span>
              <div className="mt-12 flex justify-between items-end">
                <span className="font-label text-[10px] text-on-surface-variant/50 tracking-widest">PGP: 0x8F22...</span>
                <ArrowRight className="text-on-surface-variant group-hover:translate-x-2 transition-transform w-5 h-5" strokeWidth={1.5} />
              </div>
            </a>
            
            <a href="mailto:acquisitions@kalybana.com" className="bg-surface-container p-12 group transition-all duration-300 hover:bg-surface-container-high text-left block">
              <span className="font-label text-on-surface-variant text-[10px] uppercase block mb-4 tracking-widest">Asset Acquisitions</span>
              <span className="font-headline text-2xl text-primary-fixed block group-hover:text-secondary transition-colors underline underline-offset-8">acquisitions@kalybana.com</span>
              <div className="mt-12 flex justify-between items-end">
                <span className="font-label text-[10px] text-on-surface-variant/50 tracking-widest">VETTING REQ.</span>
                <ArrowRight className="text-on-surface-variant group-hover:translate-x-2 transition-transform w-5 h-5" strokeWidth={1.5} />
              </div>
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}
