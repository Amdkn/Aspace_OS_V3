import React from 'react';
import { motion } from 'motion/react';
import { 
  Users, 
  BrainCircuit, 
  Workflow, 
  Scale, 
  Headset,
  Activity,
  Zap,
  ArrowRight
} from 'lucide-react';
import { cn } from '../lib/utils';

export function People() {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="p-8 max-w-7xl mx-auto space-y-8"
    >
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100">Board of Directors</h1>
          <p className="text-sm text-stone-500 mt-1">Gestion de la force de travail asynchrone humaine et synthétique.</p>
        </div>
      </header>

      {/* Top Widgets: Workforce Health */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
              <Activity className="w-5 h-5 text-emerald-500" />
            </div>
            <div>
              <h4 className="text-stone-400 text-sm font-medium mb-0.5">Bande Passante (Charge système)</h4>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-semibold text-stone-100">80%</span>
                <span className="text-xs text-stone-500">25 leads en cours</span>
              </div>
            </div>
          </div>
          <div className="w-32 h-2 bg-stone-950 rounded-full overflow-hidden border border-stone-800/50">
            <div className="h-full bg-emerald-500 w-[80%] rounded-full shadow-[0_0_10px_rgba(16,185,129,0.5)]" />
          </div>
        </div>
        
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
              <Zap className="w-5 h-5 text-amber-500/80" />
            </div>
            <div>
              <h4 className="text-stone-400 text-sm font-medium mb-0.5">Coût d'Acquisition (CAC)</h4>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-semibold text-stone-100">$340</span>
                <span className="text-xs text-stone-500">par mandat signé</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Component A: The Roster */}
      <div>
        <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2 mb-4">
          <Users className="w-4 h-4 text-emerald-500" />
          The Roster (Agents Actifs)
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          
          {/* Jerry - n8n */}
          <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col relative overflow-hidden group hover:border-stone-700 transition-colors">
            <div className="flex justify-between items-start mb-4">
              <div className="w-10 h-10 rounded-lg bg-stone-950 flex items-center justify-center border border-stone-800 shadow-inner">
                <BrainCircuit className="w-5 h-5 text-emerald-400" />
              </div>
              <span className="flex items-center gap-1.5 text-xs font-medium px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" /> Live
              </span>
            </div>
            <h4 className="font-display font-semibold text-stone-200 mb-1">Jerry</h4>
            <p className="text-xs text-stone-500 mb-5 flex-1">Orchestrateur N8N (Synchro Airtable, DocuSign, Supabase).</p>
            <div className="pt-4 border-t border-stone-800 flex justify-between items-end">
              <div>
                <div className="text-xs text-stone-500 mb-0.5">Webhooks traités</div>
                <div className="font-mono text-sm text-stone-300">1,204 <span className="text-emerald-500/80 text-xs ml-1">(0.1% err)</span></div>
              </div>
            </div>
            <div className="absolute -bottom-6 -right-6 w-24 h-24 bg-emerald-500/5 blur-2xl rounded-full pointer-events-none group-hover:bg-emerald-500/10 transition-colors" />
          </div>

          {/* Batman - OSINT */}
          <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col relative overflow-hidden group hover:border-stone-700 transition-colors">
            <div className="flex justify-between items-start mb-4">
              <div className="w-10 h-10 rounded-lg bg-stone-950 flex items-center justify-center border border-stone-800 shadow-inner">
                <Workflow className="w-5 h-5 text-indigo-400" />
              </div>
              <span className="flex items-center gap-1.5 text-xs font-medium px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" /> Live
              </span>
            </div>
            <h4 className="font-display font-semibold text-stone-200 mb-1">Batman</h4>
            <p className="text-xs text-stone-500 mb-5 flex-1">Ops Manager / OSINT. Extraction TPS/Microbilt & Skip Tracing.</p>
            <div className="pt-4 border-t border-stone-800 flex justify-between items-end">
              <div>
                <div className="text-xs text-stone-500 mb-0.5">Hit Rate</div>
                <div className="font-mono text-sm text-emerald-400">86.4% <span className="text-stone-500 text-xs ml-1">valides</span></div>
              </div>
            </div>
          </div>

          {/* Aquaman - Legal */}
          <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col relative overflow-hidden group hover:border-stone-700 transition-colors">
            <div className="flex justify-between items-start mb-4">
              <div className="w-10 h-10 rounded-lg bg-stone-950 flex items-center justify-center border border-stone-800 shadow-inner">
                <Scale className="w-5 h-5 text-amber-500/80" />
              </div>
              <span className="flex items-center gap-1.5 text-xs font-medium px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" /> Live
              </span>
            </div>
            <h4 className="font-display font-semibold text-stone-200 mb-1">Aquaman</h4>
            <p className="text-xs text-stone-500 mb-5 flex-1">Legal Manager. Affidavits, Requêtes Pro Se & Probate.</p>
            <div className="pt-4 border-t border-stone-800 flex justify-between items-end">
              <div>
                <div className="text-xs text-stone-500 mb-0.5">Délai Préparation</div>
                <div className="font-mono text-sm text-stone-300">34h <span className="text-stone-500 text-xs ml-1">(SLA &lt;48h)</span></div>
              </div>
            </div>
          </div>

          {/* Human VA */}
          <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col relative overflow-hidden group hover:border-stone-700 transition-colors">
            <div className="flex justify-between items-start mb-4">
              <div className="w-10 h-10 rounded-lg bg-stone-950 flex items-center justify-center border border-stone-800 shadow-inner">
                <Headset className="w-5 h-5 text-cyan-400" />
              </div>
              <span className="flex items-center gap-1.5 text-xs font-medium px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" /> Active
              </span>
            </div>
            <h4 className="font-display font-semibold text-stone-200 mb-1">Human VA</h4>
            <p className="text-xs text-stone-500 mb-5 flex-1">Le Technicien. Appels empathiques & validation de closing.</p>
            <div className="pt-4 border-t border-stone-800 flex justify-between items-end">
              <div>
                <div className="text-xs text-stone-500 mb-0.5">Conversion (Call/Sign)</div>
                <div className="font-mono text-sm text-stone-300">12.5%</div>
              </div>
            </div>
          </div>
          
        </div>
      </div>

      {/* Component B: Task Router */}
      <div className="rounded-xl bg-stone-900 border border-stone-800 overflow-hidden flex flex-col">
        <div className="p-5 border-b border-stone-800">
          <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
            <Workflow className="w-4 h-4 text-stone-400" />
            Task Router (Assignation SOPs)
          </h3>
          <p className="text-xs text-stone-500 mt-1">Règles de routage automatique des dossiers vers les agents.</p>
        </div>
        <div className="p-5">
          <div className="space-y-3">
            
            {/* Rule 1 */}
            <div className="flex items-center justify-between p-4 rounded-lg bg-stone-950/50 border border-stone-800/80 hover:border-stone-700 transition-colors">
              <div className="flex items-center gap-4">
                <div className="px-2.5 py-1 rounded bg-stone-800 text-stone-300 text-xs font-mono border border-stone-700/50">
                  IF Status <span className="text-emerald-400">==</span> "Héritiers Inconnus"
                </div>
                <ArrowRight className="w-4 h-4 text-stone-600" />
                <div className="flex flex-col">
                  <span className="text-sm font-medium text-stone-200">Protocole Pivot Généalogique</span>
                  <span className="text-xs text-stone-500">SOP-004 (Knowledge base)</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs text-stone-500 mr-2">Assign to:</span>
                <div className="flex items-center gap-1.5 px-3 py-1.5 bg-stone-800 rounded-md border border-stone-700">
                  <Workflow className="w-3.5 h-3.5 text-indigo-400" />
                  <span className="text-xs font-medium text-stone-200">Batman</span>
                </div>
              </div>
            </div>

            {/* Rule 2 */}
            <div className="flex items-center justify-between p-4 rounded-lg bg-stone-950/50 border border-stone-800/80 hover:border-stone-700 transition-colors">
              <div className="flex items-center gap-4">
                <div className="px-2.5 py-1 rounded bg-stone-800 text-stone-300 text-xs font-mono border border-stone-700/50">
                  IF Event <span className="text-emerald-400">==</span> "DocuSign Completed"
                </div>
                <ArrowRight className="w-4 h-4 text-stone-600" />
                <div className="flex flex-col">
                  <span className="text-sm font-medium text-stone-200">Préparation Dépôt Cour</span>
                  <span className="text-xs text-stone-500">SOP-012 (Legal templates)</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs text-stone-500 mr-2">Assign to:</span>
                <div className="flex items-center gap-1.5 px-3 py-1.5 bg-stone-800 rounded-md border border-stone-700">
                  <Scale className="w-3.5 h-3.5 text-amber-500/80" />
                  <span className="text-xs font-medium text-stone-200">Aquaman</span>
                </div>
              </div>
            </div>

            {/* Rule 3 */}
            <div className="flex items-center justify-between p-4 rounded-lg border border-dashed border-stone-700 bg-transparent hover:border-stone-500 transition-colors cursor-pointer group">
              <span className="text-sm font-medium text-stone-400 group-hover:text-stone-300 flex items-center gap-2">
                + Ajouter une règle de routage
              </span>
            </div>

          </div>
        </div>
      </div>

    </motion.div>
  );
}
