import React from 'react';
import { Header } from '../organisms/Header';
import { Hero } from '../organisms/Hero';
import { ServicesGrid } from '../organisms/ServicesGrid';

export const LandingPage: React.FC = () => {
  return (
    <div className="flex flex-col min-h-screen bg-zinc-50 dark:bg-black">
      <Header />
      <main className="flex-1">
        <Hero />
        <ServicesGrid />
        
        {/* Footer Minimaliste */}
        <footer className="py-12 border-t border-zinc-200 dark:border-zinc-800 bg-white dark:bg-black">
          <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
            <div className="flex flex-col items-center md:items-start gap-2">
              <span className="text-xl font-bold text-zinc-900 dark:text-zinc-50">OMK <span className="text-blue-600">Services</span></span>
              <p className="text-sm text-zinc-500">© 2026 OMK Services. Tous droits réservés.</p>
            </div>
            <div className="flex gap-6">
              <a href="#" className="text-zinc-400 hover:text-blue-600 transition-colors">LinkedIn</a>
              <a href="#" className="text-zinc-400 hover:text-blue-600 transition-colors">X</a>
              <a href="#" className="text-zinc-400 hover:text-blue-600 transition-colors">GitHub</a>
            </div>
          </div>
        </footer>
      </main>
    </div>
  );
};
