import { Building2, Mountain, Lock, EyeOff, ArrowRight, Loader2 } from 'lucide-react';
import { useHoldings } from '../hooks/useHoldings';
import { useSEO } from '../hooks/useSEO';

export default function Portfolio() {
  const { holdings, metrics, loading } = useHoldings();

  useSEO({
    title: 'Strategic Real Estate Asset Recovery',
    description: 'Architecting value in real estate assets through algorithmic recovery and strategic land acquisition.',
  });

  const formattedExposure = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(metrics.globalExposure);

  const renderIcon = (iconName: string) => {
    switch (iconName) {
      case 'Building2':
        return <Building2 className="text-secondary w-10 h-10" strokeWidth={1.5} />;
      case 'Mountain':
        return <Mountain className="text-primary-fixed w-10 h-10" strokeWidth={1.5} />;
      case 'Lock':
        return <Lock className="text-error w-10 h-10" strokeWidth={1.5} />;
      default:
        return null;
    }
  };

  const getAumBadgeClass = (iconName: string) => {
    switch (iconName) {
      case 'Building2':
        return 'font-label text-[10px] text-secondary border border-secondary/30 px-2 py-1 uppercase tracking-widest';
      case 'Mountain':
        return 'font-label text-[10px] text-on-surface-variant border border-outline-variant/30 px-2 py-1 uppercase tracking-widest';
      case 'Lock':
        return 'font-label text-[10px] text-error border border-error/30 px-2 py-1 uppercase tracking-widest';
      default:
        return '';
    }
  };

  if (loading) {
    return (
      <div className="w-full min-h-[90vh] flex items-center justify-center bg-surface" role="status" aria-label="loading">
        <Loader2 className="w-12 h-12 text-secondary animate-spin" aria-hidden="true" />
      </div>
    );
  }

  return (
    <div className="w-full">
      {/* Hero Section */}
      <section className="relative min-h-[90vh] flex flex-col justify-center px-8 md:px-12 py-24 wireframe-grid border-b border-outline-variant/20">
        <div className="max-w-5xl relative z-10">
          <div className="inline-block px-3 py-1 bg-secondary-container/30 border border-secondary/20 mb-8">
            <span className="font-label text-secondary text-xs uppercase tracking-[0.2em]">Sovereign Asset Protocol v4.0</span>
          </div>
          <h1 className="font-headline text-6xl md:text-8xl font-bold text-primary-fixed leading-[1.1] tracking-tighter mb-8">
            Architecting Value in <br />Real Estate Assets.
          </h1>
          <p className="font-body text-xl text-on-surface-variant max-w-2xl mb-12 leading-relaxed">
            Algorithmic asset recovery and strategic land acquisition powered by the proprietary SOB Engine™. Hard-coded trust for a liquid future.
          </p>
          <div className="flex flex-wrap gap-6">
            <button className="bg-primary-fixed text-on-primary-fixed px-8 py-4 font-label font-bold uppercase tracking-widest text-sm hover:brightness-110 transition-all">
              View Portfolio
            </button>
            <button className="border border-outline-variant text-primary-fixed px-8 py-4 font-label font-bold uppercase tracking-widest text-sm hover:bg-surface-container transition-all">
              Investor Login
            </button>
          </div>
        </div>
        
        {/* Asymmetric Data Fragment */}
        <div className="absolute bottom-12 right-12 hidden xl:block border-l border-outline-variant/30 pl-6 z-10">
          <div className="font-label text-[10px] text-on-surface-variant uppercase mb-2 tracking-widest">Current Global Exposure</div>
          <div className="font-label text-4xl text-primary-fixed">{formattedExposure}</div>
          <div className="font-label text-secondary text-xs mt-1 tracking-widest">+{metrics.ytdYield}% YTD Yield</div>
        </div>
      </section>

      {/* Portfolio Section: Monolith Header & Bento Cards */}
      <section className="py-24 bg-surface-container-low">
        <div className="px-8 md:px-12 mb-16 flex flex-col md:flex-row justify-between items-end gap-8">
          <div className="max-w-2xl">
            <span className="font-label text-on-surface-variant text-xs uppercase tracking-widest mb-4 block">Asset Manifest</span>
            <h2 className="font-headline text-5xl font-semibold text-primary-fixed tracking-tight">Strategic Holdings</h2>
          </div>
          <div className="text-left md:text-right">
            <div className="font-label text-[10px] text-on-surface-variant uppercase tracking-widest mb-1">Updated</div>
            <div className="font-label text-sm text-primary-fixed tracking-widest">{metrics.lastUpdated}</div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-1 px-8 md:px-12">
          {holdings.map((holding) => (
            <div
              key={holding.id}
              className={`p-10 flex flex-col justify-between min-h-[450px] border border-outline-variant/10 hover:border-secondary/40 transition-colors group relative overflow-hidden ${
                holding.isRedacted ? 'bg-surface-container-lowest' : 'glass-card'
              }`}
            >
              {holding.isRedacted && (
                <div className="absolute inset-0 opacity-10 pointer-events-none">
                  <img 
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuAbMME_P4rKVtPqdHBmPWzs-32ZasY75adMyTxeYkB7iR-mUDqXnKgJ9b2ASS5K_DkMKvOv8sAKDiiqy8rYjnXa5onCYfFqdzHsDk40P9NMj5owN11-JezAvlzSb5enLDbVPpsr5ER5bPs8k4dcQ_mhTf2mzPBAO__jTYYlgGMzMiiJ_MXbTS4TdbeY0vgN-wc0kudUo2IoNmX8oszMPEsBskkLYERC04szIhqtyfNVTucfUMW1mLTMrf2jqSZYD3kIoHx5xVz3RDHe" 
                    alt="Redacted abstract" 
                    className="w-full h-full object-cover"
                    referrerPolicy="no-referrer"
                  />
                </div>
              )}
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-12">
                  {renderIcon(holding.iconName)}
                  <span className={getAumBadgeClass(holding.iconName)}>{holding.aum}</span>
                </div>
                <h3 className="font-headline text-3xl text-primary-fixed mb-4 tracking-tight">{holding.name}</h3>
                <p className="font-body text-on-surface-variant text-sm leading-relaxed">{holding.description}</p>
              </div>
              <div className="pt-8 flex justify-between items-center border-t border-outline-variant/20 relative z-10">
                <span className="font-label text-xs uppercase tracking-widest text-on-surface-variant">{holding.role}</span>
                {holding.isRedacted ? (
                  <EyeOff className="text-on-surface-variant w-5 h-5" strokeWidth={1.5} />
                ) : (
                  <ArrowRight className="text-primary group-hover:translate-x-1 transition-transform w-5 h-5" strokeWidth={1.5} />
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* SOB Engine Section */}
      <section className="py-32 px-8 md:px-12 bg-surface overflow-hidden border-t border-outline-variant/10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
          <div>
            <span className="font-label text-secondary text-xs uppercase tracking-[0.3em] mb-6 block">The Sovereign Instrument</span>
            <h2 className="font-headline text-5xl md:text-6xl font-bold text-primary-fixed mb-12 tracking-tighter">Signal in the Noise.</h2>
            
            <div className="space-y-10">
              <div className="flex gap-6">
                <div className="font-label text-secondary font-bold text-xl">01</div>
                <div>
                  <h4 className="font-label uppercase tracking-widest text-primary-fixed mb-2">Ingestion</h4>
                  <p className="text-on-surface-variant text-sm leading-relaxed">Real-time scraping of public records, tax liens, and court filings at 400ms intervals.</p>
                </div>
              </div>
              <div className="flex gap-6">
                <div className="font-label text-secondary font-bold text-xl">02</div>
                <div>
                  <h4 className="font-label uppercase tracking-widest text-primary-fixed mb-2">Debt Stack Analysis</h4>
                  <p className="text-on-surface-variant text-sm leading-relaxed">Automated calculation of LTV, equity buffers, and legal encumbrances via proprietary models.</p>
                </div>
              </div>
              <div className="flex gap-6">
                <div className="font-label text-secondary font-bold text-xl">03</div>
                <div>
                  <h4 className="font-label uppercase tracking-widest text-primary-fixed mb-2">Execution</h4>
                  <p className="text-on-surface-variant text-sm leading-relaxed">Direct-to-trustee offer generation and legal document automation for immediate filing.</p>
                </div>
              </div>
            </div>
          </div>

          {/* Technical Blueprint Visual */}
          <div className="relative bg-surface-container h-[500px] border border-outline-variant/20 flex items-center justify-center">
            <div className="absolute inset-0 wireframe-grid opacity-30"></div>
            <div className="relative w-full max-w-md p-8 border border-outline-variant/40 bg-background/80 backdrop-blur-md">
              <div className="flex justify-between items-center mb-10">
                <span className="font-label text-[10px] text-on-surface-variant tracking-widest">ENGINE_CORE::SOB_V4</span>
                <div className="flex gap-1">
                  <div className="w-1.5 h-1.5 bg-secondary"></div>
                  <div className="w-1.5 h-1.5 bg-secondary/40"></div>
                  <div className="w-1.5 h-1.5 bg-secondary/20"></div>
                </div>
              </div>
              
              {/* Technical Visualization Nodes */}
              <div className="space-y-4">
                <div className="p-4 border border-outline-variant/30 bg-surface flex justify-between items-center">
                  <span className="font-label text-[10px] uppercase text-on-surface-variant tracking-widest">Input: Fed_Data_Stream</span>
                  <span className="font-label text-xs text-secondary tracking-widest">OK</span>
                </div>
                <div className="flex justify-center h-8">
                  <div className="w-px bg-outline-variant/40"></div>
                </div>
                <div className="p-4 border border-secondary/50 bg-surface flex justify-between items-center shadow-[0_0_20px_rgba(6,183,127,0.1)]">
                  <span className="font-label text-[10px] uppercase text-primary-fixed tracking-widest">Processing: Debt_Optimization</span>
                  <span className="font-label text-xs text-secondary tracking-widest">ACTIVE</span>
                </div>
                <div className="flex justify-center h-8">
                  <div className="w-px bg-outline-variant/40"></div>
                </div>
                <div className="p-4 border border-outline-variant/30 bg-surface flex justify-between items-center">
                  <span className="font-label text-[10px] uppercase text-on-surface-variant tracking-widest">Output: Asset_Target_Alpha</span>
                  <span className="font-label text-xs text-primary-fixed tracking-widest">14.2%</span>
                </div>
              </div>
              
              <div className="mt-12 pt-6 border-t border-outline-variant/20">
                <div className="font-label text-[9px] text-on-surface-variant leading-relaxed tracking-widest">
                  // QUANTUM ENCRYPTION ENABLED <br/>
                  // AUTH_TOKEN: BANA_9942_XRT <br/>
                  // STATUS: MONITORED BY THE FORTRESS
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
