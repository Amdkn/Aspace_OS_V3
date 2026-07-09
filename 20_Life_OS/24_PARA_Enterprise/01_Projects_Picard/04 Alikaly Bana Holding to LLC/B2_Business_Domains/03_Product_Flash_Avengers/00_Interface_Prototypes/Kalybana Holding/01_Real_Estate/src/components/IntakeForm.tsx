import { useState } from 'react';
import { useAuditRequest } from '../hooks/useAuditRequest';
import { Loader2 } from 'lucide-react';

export default function IntakeForm() {
  const { submitAudit, isSubmitting } = useAuditRequest();
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    propertyAddress: '',
    caseNumber: '',
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const success = await submitAudit(formData);
    if (success) {
      setFormData({ firstName: '', lastName: '', propertyAddress: '', caseNumber: '' });
    }
  };

  return (
    <section className="py-32 bg-surface" id="intake">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-headline font-bold text-on-surface mb-4">Start Your Recovery Audit</h2>
          <p className="text-secondary font-body">Fill out the secure ledger below to initiate a manual record check.</p>
        </div>
        <form 
          onSubmit={handleSubmit}
          className="space-y-8 bg-surface-container-lowest p-8 md:p-12 rounded-xl clinical-shadow border border-outline-variant/20"
        >
          <div className="grid md:grid-cols-2 gap-8">
            <div className="space-y-2">
              <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">First Name</label>
              <input
                required
                disabled={isSubmitting}
                className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body disabled:opacity-50"
                placeholder="e.g. John"
                type="text"
                value={formData.firstName}
                onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
              />
            </div>
            <div className="space-y-2">
              <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Last Name</label>
              <input
                required
                disabled={isSubmitting}
                className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body disabled:opacity-50"
                placeholder="e.g. Doe"
                type="text"
                value={formData.lastName}
                onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
              />
            </div>
          </div>
          <div className="space-y-2">
            <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Property Address</label>
            <input
              required
              disabled={isSubmitting}
              className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body disabled:opacity-50"
              placeholder="Full address of the foreclosed property"
              type="text"
              value={formData.propertyAddress}
              onChange={(e) => setFormData({ ...formData, propertyAddress: e.target.value })}
            />
          </div>
          <div className="space-y-2">
            <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Case Number (Optional)</label>
            <input
              disabled={isSubmitting}
              className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body disabled:opacity-50"
              placeholder="Enter if known (e.g. 2023-CV-1234)"
              type="text"
              value={formData.caseNumber}
              onChange={(e) => setFormData({ ...formData, caseNumber: e.target.value })}
            />
          </div>
          <div className="pt-4">
            <button
              disabled={isSubmitting}
              className="w-full bg-primary text-on-primary py-5 rounded-xl font-headline font-bold text-lg hover:bg-primary-container transition-all shadow-lg shadow-primary/10 active:scale-[0.98] disabled:opacity-50 flex items-center justify-center gap-3"
              type="submit"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Processing...
                </>
              ) : (
                'Submit Audit Request'
              )}
            </button>
            <p className="mt-6 text-center text-xs font-label text-secondary/60 leading-relaxed italic">
              "By submitting this form, a secure footprint is generated to initiate your audit. Your information is protected by attorney-client privilege during the investigation."
            </p>
          </div>
        </form>
      </div>
    </section>
  );
}
