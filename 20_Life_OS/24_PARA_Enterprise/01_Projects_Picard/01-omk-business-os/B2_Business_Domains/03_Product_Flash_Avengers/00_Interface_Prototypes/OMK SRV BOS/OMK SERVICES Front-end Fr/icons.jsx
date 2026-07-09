// Minimal icon set — inline SVGs, lucide-style stroke geometry.
// Single source so component code stays compact and dependable.

const I = ({ children, size = 20, stroke = 1.6, className = '' }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24"
       fill="none" stroke="currentColor" strokeWidth={stroke} strokeLinecap="round" strokeLinejoin="round"
       className={className}>
    {children}
  </svg>
);

const Icon = {
  Cpu: (p) => <I {...p}><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></I>,
  Workflow: (p) => <I {...p}><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><path d="M14 17.5h-3a4 4 0 0 1-4-4V10"/></I>,
  Bot: (p) => <I {...p}><path d="M12 8V4H8"/><rect x="2" y="8" width="20" height="12" rx="2"/><path d="M2 14h2M20 14h2M15 13v2M9 13v2"/></I>,
  Layers: (p) => <I {...p}><path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/></I>,
  Mic: (p) => <I {...p}><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4M8 22h8"/></I>,
  ArrowRight: (p) => <I {...p}><path d="M5 12h14M13 5l7 7-7 7"/></I>,
  ArrowUpRight: (p) => <I {...p}><path d="M7 17 17 7M8 7h9v9"/></I>,
  Sparkles: (p) => <I {...p}><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><path d="m6 6 2 2M16 16l2 2M6 18l2-2M16 8l2-2"/></I>,
  Database: (p) => <I {...p}><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/></I>,
  FileSign: (p) => <I {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 17c1.5-2 3-2 4 0s2.5 2 4 0"/></I>,
  Receipt: (p) => <I {...p}><path d="M4 2v20l3-2 3 2 3-2 3 2 3-2 1 2V2L19 4l-3-2-3 2-3-2-3 2L4 2Z"/><path d="M8 8h8M8 12h6"/></I>,
  Book: (p) => <I {...p}><path d="M4 4a2 2 0 0 1 2-2h13v18H6a2 2 0 0 0-2 2z"/><path d="M4 4v18M9 7h6M9 11h6"/></I>,
  BarChart: (p) => <I {...p}><path d="M3 3v18h18"/><rect x="7" y="13" width="3" height="5"/><rect x="12" y="9" width="3" height="9"/><rect x="17" y="5" width="3" height="13"/></I>,
  Activity: (p) => <I {...p}><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></I>,
  Shield: (p) => <I {...p}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></I>,
  Zap: (p) => <I {...p}><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/></I>,
  Check: (p) => <I {...p}><path d="m5 12 5 5L20 7"/></I>,
  Phone: (p) => <I {...p}><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92Z"/></I>,
  Languages: (p) => <I {...p}><path d="m5 8 6 6M4 14l6-6 2-3"/><path d="M2 5h12M7 2h1"/><path d="m22 22-5-10-5 10M14 18h6"/></I>,
  Wallet: (p) => <I {...p}><path d="M19 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-2"/><path d="M3 5v0a2 2 0 0 0 2 2h16v8H5a2 2 0 0 1-2-2V5Z"/><circle cx="16" cy="12" r="1.2" fill="currentColor"/></I>,
  Inbox: (p) => <I {...p}><path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11Z"/></I>,
  Globe: (p) => <I {...p}><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10Z"/></I>,
  Linkedin: (p) => <I {...p}><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6Z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></I>,
  Twitter: (p) => <I {...p}><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2-3-1-5-4-4-7 1 1 2 1 3 1-3-2-4-6-2-9 3 4 7 6 11 6-1-4 4-7 6-4 1 0 3-1 3-1Z"/></I>,
  Github: (p) => <I {...p}><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></I>,
  Logo: (p) => <I {...p}>
    <path d="M4 12a8 8 0 1 1 16 0 8 8 0 0 1-16 0Z"/>
    <path d="M12 4v16M4 12h16"/>
  </I>,
};

window.Icon = Icon;
