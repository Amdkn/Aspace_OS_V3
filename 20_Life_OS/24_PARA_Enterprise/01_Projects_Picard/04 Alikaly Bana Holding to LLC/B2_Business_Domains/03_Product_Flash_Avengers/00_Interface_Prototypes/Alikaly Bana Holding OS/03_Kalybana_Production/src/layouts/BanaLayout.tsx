import { Outlet } from 'react-router-dom';
import Header from '@/components/bana/Header';
import Footer from '@/components/bana/Footer';

export default function BanaLayout() {
  return (
    <div className="min-h-screen flex flex-col font-body bg-surface text-on-surface selection:bg-primary/20" data-theme="light">
      <Header />
      <main className="flex-grow pt-[72px]">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}
