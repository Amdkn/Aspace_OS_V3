import React, { useState } from 'react';
import { motion } from 'motion/react';
import { 
  BookOpen, 
  Search, 
  Copy, 
  MessageSquare, 
  SearchCode, 
  ShieldAlert, 
  Library
} from 'lucide-react';
import { cn } from '../lib/utils';

const categories = [
  { id: 'scripts', name: 'Scripts (Call & SMS)', icon: MessageSquare },
  { id: 'osint', name: 'Protocoles OSINT', icon: SearchCode },
  { id: 'objections', name: 'Objection Handling', icon: ShieldAlert },
  { id: 'compliance', name: 'Compliance (Ohio ORC)', icon: Library },
];

const mockDoc = `Bonjour [Nom], c'est [Votre Prénom] du service d'audit de Alykaly. 
Je vous appelle car notre système vient de lever une alerte sur le dossier lié à [Adresse de la propriété / Nom du défunt]. 

Il semble qu'il y ait des fonds d'un montant de [Montant] dollars détenus par le tribunal du comté de Hamilton qui vous reviennent de droit, mais ils sont sur le point d'être confisqués par l'État.

Notre cabinet avance 100% des frais légaux pour sécuriser cet argent avant la prescription locale. Avez-vous 5 minutes pour d'abord confirmer votre identité ?`;

export function Knowledge() {
  const [activeCat, setActiveCat] = useState('scripts');
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(mockDoc);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex h-full"
    >
      {/* Sidebar: Taxonomy */}
      <div className="w-64 bg-stone-900 border-r border-stone-800 flex flex-col h-full shrink-0">
        <div className="p-5 border-b border-stone-800">
          <h2 className="text-lg font-display font-semibold text-stone-100 flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-emerald-500" />
            SOP Library
          </h2>
          <p className="text-xs text-stone-500 mt-1">Standard Operating Procedures</p>
        </div>
        <div className="flex-1 p-3 space-y-1">
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCat(cat.id)}
              className={cn(
                "w-full flex items-center gap-3 px-3 py-2 rounded-md text-sm font-medium transition-colors",
                activeCat === cat.id 
                  ? "bg-stone-800 text-stone-200" 
                  : "text-stone-400 hover:text-stone-300 hover:bg-stone-800/50"
              )}
            >
              <cat.icon className="w-4 h-4" />
              {cat.name}
            </button>
          ))}
        </div>
      </div>

      {/* Main Content: Document Editor / Viewer */}
      <div className="flex-1 bg-stone-950 flex flex-col h-full overflow-hidden relative">
        
        {/* Spotlight Search */}
        <div className="absolute top-6 right-8 w-64 z-10">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-stone-500" />
            <input 
              type="text" 
              placeholder="Search (Ctrl+K)"
              className="w-full bg-stone-900 border border-stone-800 rounded-lg py-2 pl-9 pr-4 text-sm text-stone-300 focus:border-emerald-500/50 outline-none backdrop-blur-sm"
            />
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-12 max-w-4xl">
          <div className="mb-8">
            <div className="text-xs text-emerald-500 font-mono mb-2">SCR-001 • Updated 12 May 2026</div>
            <h1 className="text-3xl font-display font-bold text-stone-100 mb-4">Script Initial de Traque (Cold Call)</h1>
            <p className="text-stone-400 text-sm">Ce script est utilisé lors du tout premier contact avec un prospect OSINT "Ready to Call". Il établit l'urgence sans vendre de prestation.</p>
          </div>

          <div className="relative group">
            {/* Click to copy button */}
            <button 
              onClick={handleCopy}
              className="absolute top-4 right-4 p-2 bg-stone-800 text-stone-300 hover:bg-stone-700 rounded-md transition-all opacity-0 group-hover:opacity-100 flex items-center gap-2 border border-stone-700 shadow-md z-10"
            >
              {copied ? <span className="text-xs text-emerald-400">Copié !</span> : <span className="text-xs">Copier exact</span>}
              <Copy className={cn("w-4 h-4", copied ? "text-emerald-400" : "")} />
            </button>

            {/* Document Content */}
            <div className="bg-[#111827] border border-stone-800 rounded-xl p-8 pr-20 text-stone-300 text-lg leading-relaxed font-sans shadow-inner">
              {mockDoc.split('\n\n').map((paragraph, i) => (
                <p key={i} className="mb-6 last:mb-0">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>
          
          {/* Workflow attachment */}
          <div className="mt-8 p-4 border border-dashed border-stone-800 rounded-lg flex items-center justify-between">
            <div className="flex items-center gap-3">
              <ShieldAlert className="w-5 h-5 text-amber-500" />
              <div>
                <p className="text-sm font-medium text-stone-300">Si Objection : "Prouvez-le moi / C'est une arnaque"</p>
                <p className="text-xs text-stone-500">Pivoter immédiatement vers l'audit gratuit.</p>
              </div>
            </div>
            <button className="text-xs font-medium text-stone-400 hover:text-stone-200 transition-colors">
              Voir la réponse (OBJ-02)
            </button>
          </div>

        </div>
      </div>
    </motion.div>
  );
}
