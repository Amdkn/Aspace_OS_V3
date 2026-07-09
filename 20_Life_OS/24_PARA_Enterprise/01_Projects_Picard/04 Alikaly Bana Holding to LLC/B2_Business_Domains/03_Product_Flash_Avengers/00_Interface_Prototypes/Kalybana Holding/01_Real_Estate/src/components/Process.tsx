import { FileSearch, Scale, CircleDollarSign } from 'lucide-react';

export default function Process() {
  return (
    <section className="py-32 bg-surface">
      <div className="max-w-7xl mx-auto px-6">
        <div className="mb-20">
          <h2 className="text-3xl font-headline font-bold text-on-surface mb-4">The Recovery Process</h2>
          <div className="h-1 w-20 bg-primary"></div>
        </div>
        <div className="grid md:grid-cols-3 gap-12">
          {/* Step 1 */}
          <div className="relative p-8 bg-surface-container-lowest clinical-shadow rounded-xl border-l-4 border-primary">
            <div className="text-primary/20 text-6xl font-bold absolute top-4 right-6 select-none font-headline">01</div>
            <div className="mb-6 inline-flex items-center justify-center w-12 h-12 bg-primary/5 text-primary rounded-lg">
              <FileSearch className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-headline font-bold text-on-surface mb-4">Free Audit</h3>
            <p className="text-secondary leading-relaxed font-body">
              Our analysts check court records to confirm the exact amount of your unclaimed funds. Precise, legal verification at no cost.
            </p>
          </div>

          {/* Step 2 */}
          <div className="relative p-8 bg-surface-container-lowest clinical-shadow rounded-xl border-l-4 border-primary">
            <div className="text-primary/20 text-6xl font-bold absolute top-4 right-6 select-none font-headline">02</div>
            <div className="mb-6 inline-flex items-center justify-center w-12 h-12 bg-primary/5 text-primary rounded-lg">
              <Scale className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-headline font-bold text-on-surface mb-4">Legal Shield</h3>
            <p className="text-secondary leading-relaxed font-body">
              If funds are confirmed, we mandate and pay a local attorney to build your case file. We handle the litigation entirely.
            </p>
          </div>

          {/* Step 3 */}
          <div className="relative p-8 bg-surface-container-lowest clinical-shadow rounded-xl border-l-4 border-primary">
            <div className="text-primary/20 text-6xl font-bold absolute top-4 right-6 select-none font-headline">03</div>
            <div className="mb-6 inline-flex items-center justify-center w-12 h-12 bg-primary/5 text-primary rounded-lg">
              <CircleDollarSign className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-headline font-bold text-on-surface mb-4">Payment</h3>
            <p className="text-secondary leading-relaxed font-body">
              You receive your check. We only take our commission (30%) if we are successful. If you don't get paid, we don't get paid.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
