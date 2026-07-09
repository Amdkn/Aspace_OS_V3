import { CheckCircle2, Shield } from 'lucide-react';

export default function Guarantee() {
  return (
    <section className="py-24 bg-surface-container-low">
      <div className="max-w-7xl mx-auto px-6">
        <div className="bg-surface-container-lowest p-10 md:p-16 rounded-xl clinical-shadow flex flex-col md:flex-row items-center gap-12">
          <div className="flex-1">
            <h2 className="text-4xl font-headline font-bold text-on-surface mb-6">Zero-Risk Guarantee</h2>
            <p className="text-lg text-secondary mb-8 font-body">
              We operate on a pure contingency basis. Our success is directly tied to yours. We assume all financial liability for the recovery effort.
            </p>
            <ul className="space-y-4">
              <li className="flex items-center gap-4 text-on-surface font-semibold font-body">
                <CheckCircle2 className="w-6 h-6 text-primary fill-primary/20" />
                No credit card requested.
              </li>
              <li className="flex items-center gap-4 text-on-surface font-semibold font-body">
                <CheckCircle2 className="w-6 h-6 text-primary fill-primary/20" />
                No filing fees or processing costs.
              </li>
              <li className="flex items-center gap-4 text-on-surface font-semibold font-body">
                <CheckCircle2 className="w-6 h-6 text-primary fill-primary/20" />
                We absorb 100% of attorney costs if the case fails.
              </li>
            </ul>
          </div>
          <div className="w-full md:w-1/3">
            <div className="aspect-square bg-primary/5 rounded-3xl flex items-center justify-center border-2 border-dashed border-primary/20">
              <div className="text-center">
                <Shield className="w-16 h-16 text-primary mx-auto mb-4 fill-primary/20" />
                <div className="font-headline font-bold text-primary text-xl">Fully Protected</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
