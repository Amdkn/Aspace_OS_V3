import React, { useState } from 'react';
import { motion } from 'motion/react';
import { 
  TrendingUp, 
  Mail, 
  MessageSquare, 
  Target, 
  Activity,
  Crosshair,
  Printer,
  ChevronRight
} from 'lucide-react';
import { cn } from '../lib/utils';

const mockCohorts = [
  { id: '1', name: 'Batch 01 - Saisies Hamilton', date: 'Mai 2026', size: 145, status: 'Active', smsSent: 84, mailSent: 145 },
  { id: '2', name: 'Batch 02 - Probate Franklin', date: 'Avr 2026', size: 82, status: 'Completed', smsSent: 82, mailSent: 82 },
  { id: '3', name: 'Batch 03 - Tax Liens Cuyahoga', date: 'Juin 2026', size: 210, status: 'Draft', smsSent: 0, mailSent: 0 },
];

const mockFeed = [
  { id: '1', time: '14:32:01', type: 'click', message: 'Lead A2403702 a cliqué sur le lien SMS.', highlight: true },
  { id: '2', time: '14:28:44', type: 'bounce', message: 'Courrier NIXIE retourné pour Dossier A1902549.', highlight: false },
  { id: '3', time: '14:15:12', type: 'sms_delivered', message: 'SMS délivré à Jane Doe (Case B3301).', highlight: false },
  { id: '4', time: '13:59:05', type: 'click', message: 'Lead C1102994 a consulté l\'Audit (Vue #3).', highlight: true },
];

export function Growth() {
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="p-8 max-w-7xl mx-auto space-y-8 h-full flex flex-col"
    >
      <header className="flex justify-between items-end shrink-0">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100 flex items-center gap-2">
            Growth & Outreach <TrendingUp className="w-6 h-6 text-emerald-500" />
          </h1>
          <p className="text-sm text-stone-500 mt-1">Centre de commandement pour les campagnes de contact (Cold Outreach).</p>
        </div>
      </header>

      {/* Top Widgets: Outreach Vitals */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 shrink-0">
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
              <Target className="w-5 h-5 text-indigo-400" />
            </div>
            <div>
              <h4 className="text-stone-400 text-sm font-medium mb-0.5">Hit Rate (Numéros Valides)</h4>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-semibold text-stone-100">68%</span>
                <span className="text-xs text-stone-500">Moyenne globale</span>
              </div>
            </div>
          </div>
        </div>
        
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
              <Activity className="w-5 h-5 text-emerald-500" />
            </div>
            <div>
              <h4 className="text-stone-400 text-sm font-medium mb-0.5">Vault Open Rate</h4>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-semibold text-stone-100">42%</span>
                <span className="text-xs text-stone-500">Prospects ayant cliqué</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-0">
        {/* Campaign Manager */}
        <div className="col-span-1 lg:col-span-2 bg-stone-900 border border-stone-800 rounded-xl flex flex-col overflow-hidden">
          <div className="p-5 border-b border-stone-800 flex justify-between items-center bg-stone-950/30">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
              <Mail className="w-4 h-4 text-stone-400" />
              Campaign Manager
            </h3>
            <button className="text-xs font-medium text-emerald-400 hover:text-emerald-300 transition-colors">
              + Nouvelle Cohorte
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {mockCohorts.map(cohort => (
              <div key={cohort.id} className="p-4 rounded-lg border border-stone-800 bg-stone-950/50 hover:border-stone-700 transition-colors">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h4 className="text-sm font-medium text-stone-200">{cohort.name}</h4>
                    <span className="text-xs text-stone-500">{cohort.size} leads • {cohort.date}</span>
                  </div>
                  <span className={cn(
                    "text-[10px] px-2 py-1 rounded-full font-medium uppercase tracking-wider border",
                    cohort.status === 'Active' ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20" :
                    cohort.status === 'Completed' ? "bg-stone-800 text-stone-400 border-stone-700" :
                    "bg-amber-500/10 text-amber-500 border-amber-500/20"
                  )}>
                    {cohort.status}
                  </span>
                </div>
                
                <div className="flex gap-3 mt-4 pt-4 border-t border-stone-800">
                  <button className="flex-1 flex items-center justify-center gap-2 py-2 bg-stone-800 hover:bg-stone-700 rounded text-xs font-medium text-stone-300 transition-colors">
                    <Printer className="w-3.5 h-3.5" /> Export Vistaprint (Mailing)
                  </button>
                  <button className="flex-1 flex items-center justify-center gap-2 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 rounded text-xs font-medium transition-colors border border-indigo-500/20">
                    <MessageSquare className="w-3.5 h-3.5" /> Sequence SMS
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Sniper Feed */}
        <div className="col-span-1 bg-stone-900 border border-stone-800 rounded-xl flex flex-col overflow-hidden relative">
          <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-emerald-900/10 via-stone-900/0 to-stone-900/0 pointer-events-none" />
          <div className="p-5 border-b border-stone-800 flex justify-between items-center relative z-10">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
              <Crosshair className="w-4 h-4 text-emerald-500" />
              Sniper Feed
            </h3>
            <span className="flex items-center gap-1.5 text-[10px] font-medium px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" /> LIVE
            </span>
          </div>
          <div className="flex-1 overflow-y-auto p-5 space-y-4 font-mono text-xs relative z-10">
            {mockFeed.map(item => (
              <div key={item.id} className={cn(
                "p-3 rounded border text-stone-300",
                item.highlight ? "bg-emerald-500/10 border-emerald-500/20" : "bg-stone-950/50 border-stone-800/80"
              )}>
                <div className="text-stone-500 mb-1">{item.time}</div>
                <div>{item.message}</div>
                {item.highlight && (
                  <button className="mt-2 text-emerald-400 hover:text-emerald-300 font-sans text-xs font-medium flex items-center gap-1">
                    Appeler maintenant <ChevronRight className="w-3 h-3" />
                  </button>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </motion.div>
  );
}
