import { Link, Outlet, useLocation } from 'react-router-dom';

export default function HoldingLayout() {
  const location = useLocation();

  const getNavClass = (path: string) => {
    const isActive = location.pathname === path;
    const baseClass = "font-label uppercase tracking-widest text-xs transition-all duration-200 px-2 py-1";
    if (isActive) {
      return `${baseClass} text-primary-fixed border-b-2 border-primary-fixed pb-1`;
    }
    return `${baseClass} text-on-surface-variant hover:text-primary-fixed hover:bg-surface-container`;
  };

  return (
    <div className="min-h-screen flex flex-col relative" data-theme="dark">
      <div className="grain-texture absolute inset-0 z-0"></div>
      
      {/* TopAppBar */}
      <nav className="bg-surface text-primary-fixed flex justify-between items-center w-full px-8 py-4 max-w-full sticky top-0 z-50 border-b border-outline-variant/10">
        <Link to="/" className="text-2xl font-bold tracking-tighter font-headline hover:opacity-80 transition-opacity">Kalybana</Link>
        
        <div className="hidden md:flex items-center space-x-12">
          <Link to="/" className={getNavClass('/')}>Portfolio</Link>
          <Link to="/engine" className={getNavClass('/engine')}>The Engine</Link>
          <Link to="/compliance" className={getNavClass('/compliance')}>Compliance</Link>
          <a href="/bana" className={`${getNavClass('/bana')} opacity-50`}>Bana Affiliate</a>
        </div>
        
        <div className="flex items-center space-x-6">
          <span className="font-label uppercase tracking-widest text-secondary text-[10px] hidden lg:block">
            SYSTEM: ONLINE // LATENCY: 24ms
          </span>
          <button className="bg-primary-fixed text-on-primary-fixed font-label font-bold text-xs uppercase tracking-widest px-6 py-2 hover:bg-primary-fixed-dim transition-all active:scale-95 duration-100">
            Investor Portal
          </button>
        </div>
      </nav>

      {/* Main Content */}
      <main className="flex-grow relative z-10">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="bg-surface-container-lowest text-primary-fixed w-full relative z-10 pt-20 pb-10 border-t border-surface-container/20">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 px-8 md:px-12 w-full">
          <div className="space-y-8">
            <div className="text-6xl font-black text-surface-container uppercase font-headline select-none tracking-tighter">KALYBANA</div>
            <p className="font-label text-xs text-on-surface-variant max-w-sm">
              © 2026 KALYBANA HOLDINGS. ALL RIGHTS RESERVED. THE FORTRESS.
              OPERATING UNDER PROTOCOL 19-B.
            </p>
          </div>
          <div className="grid grid-cols-2 gap-8">
            <div className="flex flex-col space-y-3">
              <span className="font-label text-[10px] text-on-surface-variant uppercase tracking-widest mb-2">Communications</span>
              <a href="mailto:legal@kalybana.com" className="font-label text-xs text-on-surface-variant hover:text-primary-fixed underline underline-offset-4 transition-colors">legal@kalybana.com</a>
              <a href="mailto:acquisitions@kalybana.com" className="font-label text-xs text-on-surface-variant hover:text-primary-fixed underline underline-offset-4 transition-colors">acquisitions@kalybana.com</a>
            </div>
            <div className="flex flex-col space-y-3">
              <span className="font-label text-[10px] text-on-surface-variant uppercase tracking-widest mb-2">Authority</span>
              <a href="#" className="font-label text-xs text-on-surface-variant hover:text-primary-fixed underline underline-offset-4 transition-colors">Terms of Service</a>
              <a href="#" className="font-label text-xs text-on-surface-variant hover:text-primary-fixed underline underline-offset-4 transition-colors">Privacy Policy</a>
              <a href="#" className="font-label text-xs text-on-surface-variant hover:text-primary-fixed underline underline-offset-4 transition-colors">Regulatory Disclosures</a>
            </div>
          </div>
        </div>
        <div className="mt-20 px-8 md:px-12 flex justify-between items-center border-t border-surface-container/20 pt-8">
          <div className="flex space-x-4 items-center">
            <div className="w-2 h-2 bg-secondary rounded-full animate-pulse"></div>
            <span className="font-label text-[10px] text-on-surface-variant uppercase tracking-widest">Global Governance Active</span>
          </div>
          <span className="font-label text-[10px] text-on-surface-variant uppercase tracking-widest">Node: LX-990</span>
        </div>
      </footer>
    </div>
  );
}
