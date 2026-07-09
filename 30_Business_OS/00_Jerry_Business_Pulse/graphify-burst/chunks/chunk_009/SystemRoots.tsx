import React from 'react';
import { motion } from 'motion/react';
import { 
  Database, 
  Terminal, 
  Server, 
  Activity, 
  Cpu, 
  Network,
  Play
} from 'lucide-react';
import { cn } from '../lib/utils';

export function SystemRoots() {
  const currentLogs = [
    "[16:42:01] n8n Webhook Triggered: DocuSign Completed",
    "[16:42:01] Updating Supabase table 'clients'",
    "[16:42:02] Status: 200 OK - Record #8829103 mapped to status 'signed'",
    "[16:45:10] CRON: Polling Hamilton County Docket...",
    "[16:45:12] FOUND: 3 new surplus filings. Parsing PDFs via Gemini...",
    "[16:45:15] Status: 200 OK - 3 leads injected into 'alpha_leads'",
    "[16:48:00] Stripe API: Verifying payout status for batch tx_A9201",
    "[16:48:01] Status: 202 ACCEPTED - Pending 2 business days"
  ];

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="p-8 max-w-7xl mx-auto space-y-8 h-full flex flex-col"
    >
      <header className="flex justify-between items-end shrink-0">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100 flex items-center gap-3">
            System Roots <Database className="w-6 h-6 text-stone-400" />
          </h1>
          <p className="text-sm text-stone-500 mt-1">Infrastructure vitale et flux de données automatisés.</p>
        </div>
      </header>

      {/* Top Widgets: API Health */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 shrink-0">
        {[
          { name: 'Supabase DB', icon: Database, status: 'online' },
          { name: 'n8n Orchestration', icon: Network, status: 'online' },
          { name: 'DocuSign API', icon: FileSignature, status: 'online' },
          { name: 'Gemini Models', icon: Cpu, status: 'online' },
        ].map(api => (
          <div key={api.name} className="p-4 rounded-xl bg-stone-900 border border-stone-800 flex items-center gap-3">
            <div className="w-8 h-8 rounded bg-stone-950 flex items-center justify-center border border-stone-800">
              <api.icon className="w-4 h-4 text-stone-400" />
            </div>
            <div className="flex flex-col">
              <span className="text-xs font-medium text-stone-300">{api.name}</span>
              <div className="flex items-center gap-1.5 mt-0.5">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 shadow-[0_0_5px_rgba(16,185,129,0.5)]" />
                <span className="text-[10px] text-emerald-400 uppercase tracking-wider">{api.status}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 flex-1 min-h-0">
        
        {/* Component A: Webhook Traffic Terminal */}
        <div className="bg-stone-950 border border-stone-800 rounded-xl flex flex-col overflow-hidden relative shadow-inner">
          <div className="bg-stone-900 px-4 py-2 border-b border-stone-800 flex items-center gap-2 shrink-0">
            <Terminal className="w-4 h-4 text-stone-500" />
            <span className="text-xs font-mono text-stone-400">root@alykaly-os:~/logs/webhooks</span>
            <div className="ml-auto flex gap-1.5">
              <div className="w-2.5 h-2.5 rounded-full bg-stone-700" />
              <div className="w-2.5 h-2.5 rounded-full bg-stone-700" />
              <div className="w-2.5 h-2.5 rounded-full bg-stone-700" />
            </div>
          </div>
          <div className="flex-1 p-4 font-mono text-[11px] leading-relaxed overflow-y-auto text-emerald-400/80">
            {currentLogs.map((log, i) => (
              <div key={i} className="mb-1">{log}</div>
            ))}
            <div className="flex items-center gap-2 mt-2">
              <span className="text-stone-500">_</span>
              <span className="w-1.5 h-3 bg-emerald-500/50 animate-pulse" />
            </div>
          </div>
        </div>

        {/* Component B: DB Quick Query */}
        <div className="bg-stone-900 border border-stone-800 rounded-xl flex flex-col overflow-hidden">
          <div className="p-4 border-b border-stone-800 bg-stone-950/30 flex items-center justify-between shrink-0">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
              <Server className="w-4 h-4 text-stone-400" />
              DB Quick-Query
            </h3>
            <span className="px-2 py-0.5 bg-rose-500/10 text-rose-500 text-[10px] font-medium uppercase tracking-wider rounded border border-rose-500/20">
              Root Access
            </span>
          </div>
          
          <div className="flex-1 p-5 flex flex-col gap-4">
            <div className="flex-1 bg-stone-950 border border-stone-800 rounded-lg p-1 relative">
              <textarea 
                className="w-full h-full bg-transparent text-stone-300 font-mono text-xs p-3 outline-none resize-none"
                defaultValue={"SELECT \n  case_number, \n  defendant_name, \n  osint_status\nFROM \n  alpha_leads\nWHERE \n  confidence_score = 5\nLIMIT 10;"}
              />
              <button className="absolute bottom-4 right-4 bg-emerald-500 hover:bg-emerald-400 text-stone-950 p-2 rounded flex items-center gap-2 shadow-lg transition-colors">
                <Play className="w-4 h-4 fill-current" /> <span className="text-xs font-bold uppercase tracking-wider">Run SQL</span>
              </button>
            </div>
            
            <div className="h-40 bg-stone-950 border border-stone-800 rounded-lg p-3 overflow-auto">
              <table className="w-full text-left font-mono text-[10px] text-stone-400">
                <thead>
                  <tr className="border-b border-stone-800 text-stone-500">
                    <th className="pb-2 font-medium">case_number</th>
                    <th className="pb-2 font-medium">defendant_name</th>
                    <th className="pb-2 font-medium">osint_status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="py-2 text-indigo-400">"B 1984221"</td>
                    <td className="py-2 text-yellow-100/70">"Apex Industrial LLC"</td>
                    <td className="py-2 text-emerald-400">"ready"</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </div>
    </motion.div>
  );
}

// Temporary icon to avoid import error
function FileSignature(props: any) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
      <path d="M20 19.5v.5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h5.5"/>
      <path d="m8 11.5 5 5 5-5"/>
      <path d="M13 14V4h7v10"/>
    </svg>
  );
}
