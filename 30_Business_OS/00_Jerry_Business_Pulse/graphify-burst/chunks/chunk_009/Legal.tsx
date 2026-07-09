import React from 'react';
import { motion } from 'motion/react';
import { 
  Scale, 
  Clock, 
  FileCheck,
  Send,
  AlertTriangle,
  Gavel,
  CheckCircle2,
  Lock
} from 'lucide-react';
import { cn } from '../lib/utils';

const kanbanData = {
  ready: [
    { id: '1', cases: 'A 2401198', name: 'Estate of Robert Chase', delay: '2j' }
  ],
  filed: [
    { id: '2', cases: 'B 1984221', name: 'Apex Industrial LLC', date: 'Filed 12/05' }
  ],
  hearing: [
    { id: '3', cases: 'C 8829103', name: 'Sarah Jenkins', date: 'Audience 24/05' }
  ],
  signed: [
    { id: '4', cases: 'A 2309912', name: 'Vance Family Trust', amount: '$42,500' }
  ]
};

function KanbanCard({ item, type }: { item: any, type: string }) {
  return (
    <div className="p-3 bg-stone-950 border border-stone-800 rounded-lg cursor-grab active:cursor-grabbing hover:border-stone-600 transition-colors">
      <div className="flex justify-between items-start mb-2">
        <span className="text-xs font-mono text-stone-400">{item.cases}</span>
        {type === 'ready' && <span className="text-[10px] text-emerald-400 bg-emerald-500/10 px-1.5 py-0.5 rounded">Prêt</span>}
        {type === 'hearing' && <span className="text-[10px] text-amber-500 bg-amber-500/10 px-1.5 py-0.5 rounded flex items-center gap-1"><AlertTriangle className="w-3 h-3" /> Imminent</span>}
      </div>
      <h4 className="text-sm font-medium text-stone-200 mb-2">{item.name}</h4>
      <div className="flex justify-between items-center text-xs text-stone-500">
        <span>{item.date || item.delay || item.amount}</span>
        {type === 'signed' && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500" />}
      </div>
    </div>
  );
}

export function Legal() {
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex flex-col h-full overflow-hidden"
    >
      {/* Top Banner (Counsel Comm-Link & Deadlines) */}
      <div className="bg-stone-900 border-b border-stone-800 p-6 flex justify-between items-center shrink-0">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100 flex items-center gap-3">
            L'Assemblage Légal <Scale className="w-6 h-6 text-emerald-500" />
          </h1>
          <p className="text-sm text-stone-500 mt-1">Courroie de transmission judiciaire et suivi des motions.</p>
        </div>
        
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-3 px-4 py-2 bg-stone-950 border border-stone-800 rounded-lg">
            <Clock className="w-4 h-4 text-rose-500 animate-pulse" />
            <div>
              <p className="text-xs font-medium text-stone-300">Deadlines Prescription</p>
              <p className="text-xs text-rose-500/90 font-mono">1 dossier &lt; 30 jours (Case #7712)</p>
            </div>
          </div>
          
          <button className="flex items-center gap-2 bg-stone-100 hover:bg-white text-stone-950 px-4 py-2 rounded-lg text-sm font-medium transition-colors">
            <Lock className="w-4 h-4" />
            Générer Bundle Légal
          </button>
        </div>
      </div>

      {/* Kanban Board */}
      <div className="flex-1 overflow-x-auto p-6 bg-stone-950">
        <div className="flex gap-6 h-full min-w-max">
          
          {/* Col 1 */}
          <div className="w-72 flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-stone-900/50">
              <h3 className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <FileCheck className="w-4 h-4 text-emerald-500" />
                Ready for Legal
              </h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.ready.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.ready.map(item => <KanbanCard key={item.id} item={item} type="ready" />)}
            </div>
          </div>

          {/* Col 2 */}
          <div className="w-72 flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-stone-900/50">
              <h3 className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <Send className="w-4 h-4 text-indigo-400" />
                Motion Filed
              </h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.filed.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.filed.map(item => <KanbanCard key={item.id} item={item} type="filed" />)}
            </div>
          </div>

          {/* Col 3 */}
          <div className="w-72 flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-amber-500/5">
              <h3 className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <Gavel className="w-4 h-4 text-amber-500" />
                Hearing Scheduled
              </h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.hearing.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.hearing.map(item => <KanbanCard key={item.id} item={item} type="hearing" />)}
            </div>
          </div>

          {/* Col 4 */}
          <div className="w-72 flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-emerald-500/5">
              <h3 className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                Order Signed
              </h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.signed.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto relative">
               <div className="absolute inset-0 bg-emerald-500/5 pointer-events-none" />
              {kanbanData.signed.map(item => <KanbanCard key={item.id} item={item} type="signed" />)}
            </div>
          </div>

        </div>
      </div>
    </motion.div>
  );
}
