import React, { useState } from 'react';
import { motion } from 'motion/react';
import { 
  Lock, 
  Link as LinkIcon, 
  Copy, 
  Eye, 
  FileSignature, 
  CheckCircle2,
  Send,
  Wand2
} from 'lucide-react';
import { cn } from '../lib/utils';

const kanbanData = {
  audit: [
    { id: '1', cases: 'A 2403702', name: 'Estate of Robert Chase' }
  ],
  sent: [
    { id: '2', cases: 'B 1984221', name: 'Apex Industrial LLC' }
  ],
  opened: [
    { id: '3', cases: 'C 8829103', name: 'Sarah Jenkins', views: 3 }
  ],
  signed: [
    { id: '4', cases: 'A 2401198', name: 'Michael T. Vance' }
  ]
};

function KanbanCard({ item, type }: { item: any, type: string }) {
  return (
    <div className="p-3 bg-stone-950 border border-stone-800 rounded-lg cursor-grab active:cursor-grabbing hover:border-stone-600 transition-colors">
      <div className="flex justify-between items-start mb-2">
        <span className="text-xs font-mono text-stone-400">{item.cases}</span>
      </div>
      <h4 className="text-sm font-medium text-stone-200 mb-2">{item.name}</h4>
      <div className="flex justify-between items-center text-xs">
        {type === 'opened' && <span className="text-emerald-400 flex items-center gap-1"><Eye className="w-3 h-3" /> {item.views} vues</span>}
        {type === 'signed' && <span className="text-emerald-500 font-medium flex items-center gap-1"><CheckCircle2 className="w-3 h-3" /> DocuSign OK</span>}
      </div>
    </div>
  );
}

export function SalesSanctum() {
  const [copiedLink, setCopiedLink] = useState(false);
  const [copiedScript, setCopiedScript] = useState(false);
  
  const mockLink = 'alykaly.com/vault/x7k9p2';
  const mockScript = `Bonjour [Nom], votre audit officiel concernant les fonds du comté de Hamilton est prêt. Accédez à votre coffre-fort sécurisé ici : ${mockLink}. Code PIN : [Année de naissance].`;

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex flex-col h-full overflow-hidden"
    >
      {/* Top Banner */}
      <div className="bg-stone-900 border-b border-stone-800 p-6 flex justify-between items-center shrink-0">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100 flex items-center gap-3">
            Sales Sanctum <Lock className="w-6 h-6 text-indigo-400" />
          </h1>
          <p className="text-sm text-stone-500 mt-1">Contrôle des Demo Vaults et suivi des conversions asynchrones.</p>
        </div>
      </div>

      <div className="flex-1 p-6 flex flex-col lg:flex-row gap-6 min-h-0 bg-stone-950">
        
        {/* Kanban Board */}
        <div className="flex-1 flex gap-4 overflow-x-auto min-w-0">
          {/* Col 1 */}
          <div className="flex-1 min-w-[250px] flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-stone-900/50">
              <h3 className="text-sm font-medium text-stone-300">Audit Préparé</h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.audit.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.audit.map(item => <KanbanCard key={item.id} item={item} type="audit" />)}
            </div>
          </div>

          {/* Col 2 */}
          <div className="flex-1 min-w-[250px] flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-stone-900/50">
              <h3 className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <Send className="w-4 h-4 text-stone-500" /> Lien Envoyé
              </h3>
              <span className="text-xs font-mono bg-stone-800 text-stone-400 px-1.5 py-0.5 rounded">{kanbanData.sent.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.sent.map(item => <KanbanCard key={item.id} item={item} type="sent" />)}
            </div>
          </div>

          {/* Col 3 */}
          <div className="flex-1 min-w-[250px] flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-indigo-500/10 border-b-indigo-500/20">
              <h3 className="text-sm font-medium text-indigo-400 flex items-center gap-2">
                <Eye className="w-4 h-4" /> Vault Ouvert
              </h3>
              <span className="text-xs font-mono bg-indigo-500/20 text-indigo-300 px-1.5 py-0.5 rounded">{kanbanData.opened.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto">
              {kanbanData.opened.map(item => <KanbanCard key={item.id} item={item} type="opened" />)}
            </div>
          </div>

          {/* Col 4 */}
          <div className="flex-1 min-w-[250px] flex flex-col h-full bg-stone-900 border border-stone-800 rounded-xl overflow-hidden relative">
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-emerald-900/10 via-stone-900/0 to-stone-900/0 pointer-events-none" />
            <div className="p-3 border-b border-stone-800 flex justify-between items-center bg-emerald-500/10 border-b-emerald-500/20 relative z-10">
              <h3 className="text-sm font-medium text-emerald-400 flex items-center gap-2">
                <FileSignature className="w-4 h-4" /> Signature Récupérée
              </h3>
              <span className="text-xs font-mono bg-emerald-500/20 text-emerald-300 px-1.5 py-0.5 rounded">{kanbanData.signed.length}</span>
            </div>
            <div className="flex-1 p-3 space-y-3 overflow-y-auto relative z-10">
              {kanbanData.signed.map(item => <KanbanCard key={item.id} item={item} type="signed" />)}
            </div>
          </div>
        </div>

        {/* Magic Link Generator */}
        <div className="w-full lg:w-80 flex flex-col gap-4">
          <div className="bg-stone-900 border border-stone-800 rounded-xl p-5">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2 mb-4">
              <Wand2 className="w-4 h-4 text-indigo-400" />
              Magic Link Generator
            </h3>
            
            <div className="space-y-4">
              <div>
                <label className="text-xs text-stone-400 block mb-1.5">Case ID</label>
                <select className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 px-3 text-sm text-stone-200 outline-none focus:border-indigo-500/50 appearance-none font-mono">
                  <option>A 2403702 - Robert Chase</option>
                  <option>B 1984221 - Apex Industrial</option>
                </select>
              </div>

              <div className="pt-2">
                <button className="w-full relative group overflow-hidden rounded-md p-[1px]">
                  <span className="absolute inset-0 bg-gradient-to-r from-indigo-500 to-emerald-500 rounded-md opacity-70 group-hover:opacity-100 transition-opacity" />
                  <div className="relative bg-stone-950 px-4 py-2 rounded-md flex items-center justify-center gap-2">
                    <span className="text-sm font-medium text-stone-100">Générer Coffre-Fort</span>
                  </div>
                </button>
              </div>

              <div className="pt-4 border-t border-stone-800">
                <label className="text-xs text-stone-500 block mb-1.5">Lien Unique Crypté</label>
                <div className="flex bg-stone-950 border border-stone-800 rounded-md overflow-hidden">
                  <div className="px-3 py-2 text-xs font-mono text-indigo-400 flex-1 flex items-center truncate">
                    <LinkIcon className="w-3 h-3 mr-2 text-stone-600 shrink-0" />
                    {mockLink}
                  </div>
                  <button 
                    onClick={() => {
                      navigator.clipboard.writeText(mockLink);
                      setCopiedLink(true);
                      setTimeout(() => setCopiedLink(false), 2000);
                    }}
                    className="p-2 border-l border-stone-800 hover:bg-stone-800 text-stone-400 transition-colors"
                  >
                    {copiedLink ? <CheckCircle2 className="w-4 h-4 text-emerald-500" /> : <Copy className="w-4 h-4" />}
                  </button>
                </div>
              </div>

            </div>
          </div>

          <div className="bg-stone-900 border border-stone-800 rounded-xl p-5 flex flex-col flex-1">
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-sm font-display font-semibold text-stone-100">Script SMS d'envoi</h3>
              <button 
                onClick={() => {
                  navigator.clipboard.writeText(mockScript);
                  setCopiedScript(true);
                  setTimeout(() => setCopiedScript(false), 2000);
                }}
                className="text-xs text-emerald-400 hover:text-emerald-300 font-medium flex items-center gap-1"
              >
                {copiedScript ? 'Copié !' : 'Copier text'} <Copy className="w-3 h-3" />
              </button>
            </div>
            <div className="bg-stone-950 border border-stone-800 rounded-md p-3 text-xs text-stone-400 leading-relaxed font-mono flex-1 whitespace-pre-wrap">
              {mockScript}
            </div>
          </div>
        </div>

      </div>
    </motion.div>
  );
}
