/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import Header from './components/Header';
import Hero from './components/Hero';
import Process from './components/Process';
import Guarantee from './components/Guarantee';
import IntakeForm from './components/IntakeForm';
import Footer from './components/Footer';
import { Toaster } from 'react-hot-toast';
import { useSEO } from './hooks/useSEO';

export default function App() {
  useSEO({
    title: 'Ohio & Kentucky Asset Recovery Specialists',
    description: 'Ali Real Estate Bana LLC audits foreclosure records to recover surplus funds for homeowners. 100% secure and attorney-mandated process.',
  });

  return (
    <div className="bg-surface text-on-surface font-body selection:bg-primary/20 min-h-screen flex flex-col">
      <Toaster position="top-right" />
      <Header />
      <main className="flex-grow">
        <Hero />
        <Process />
        <Guarantee />
        <IntakeForm />
      </main>
      <Footer />
    </div>
  );
}
