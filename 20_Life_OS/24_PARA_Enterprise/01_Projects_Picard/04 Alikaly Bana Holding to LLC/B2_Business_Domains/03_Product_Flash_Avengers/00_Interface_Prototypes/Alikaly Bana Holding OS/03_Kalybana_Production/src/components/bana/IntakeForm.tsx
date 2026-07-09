import { useState } from 'react';

export default function IntakeForm() {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setIsSubmitting(true);
    
    const formData = new FormData(e.currentTarget);
    const data = Object.fromEntries(formData.entries());

    try {
      const webhookUrl = import.meta.env.VITE_N8N_WEBHOOK_URL;
      if (webhookUrl) {
        await fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            source: 'BANA_INTAKE',
            timestamp: new Date().toISOString(),
            payload: data
          })
        });
      } else {
        // Dev fallback simulation
        await new Promise(r => setTimeout(r, 800));
        console.warn('VITE_N8N_WEBHOOK_URL is missing. Simulating request.', data);
      }
      setIsSuccess(true);
      (e.target as HTMLFormElement).reset();
      
      // Reset success message after 5 seconds
      setTimeout(() => setIsSuccess(false), 5000);
    } catch (error) {
      console.error('Submission failed', error);
      alert('An error occurred during submission. Please try again or contact support.');
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section className="py-32 bg-surface" id="intake">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-headline font-bold text-on-surface mb-4">Start Your Recovery Audit</h2>
          <p className="text-secondary font-body">Fill out the secure ledger below to initiate a manual record check.</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-8 bg-surface-container-lowest p-8 md:p-12 rounded-xl clinical-shadow border border-outline-variant/20 relative overflow-hidden">
          
          {isSuccess && (
            <div className="absolute inset-0 bg-primary/95 z-10 flex flex-col items-center justify-center text-on-primary p-8 text-center backdrop-blur-sm transition-all">
              <div className="w-16 h-16 border-4 border-on-primary rounded-full flex items-center justify-center mb-4">
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <h3 className="text-2xl font-headline font-bold mb-2">Audit Request Secured</h3>
              <p className="font-body opacity-90 max-w-md">Your footprint has been logged. Our analysts will review the records and contact you shortly.</p>
            </div>
          )}

          <div className="grid md:grid-cols-2 gap-8">
            <div className="space-y-2">
              <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">First Name</label>
              <input
                required
                name="firstName"
                className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body"
                placeholder="e.g. John"
                type="text"
              />
            </div>
            <div className="space-y-2">
              <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Last Name</label>
              <input
                required
                name="lastName"
                className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body"
                placeholder="e.g. Doe"
                type="text"
              />
            </div>
          </div>
          <div className="space-y-2">
            <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Property Address</label>
            <input
              required
              name="propertyAddress"
              className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body"
              placeholder="Full address of the foreclosed property"
              type="text"
            />
          </div>
          <div className="space-y-2">
            <label className="font-label text-xs font-bold uppercase tracking-widest text-secondary">Case Number (Optional)</label>
            <input
              name="caseNumber"
              className="w-full bg-surface-container-low border-none rounded-md px-4 py-4 focus:ring-2 focus:ring-primary/40 focus:outline-none transition-all placeholder:text-outline-variant font-body"
              placeholder="Enter if known (e.g. 2023-CV-1234)"
              type="text"
            />
          </div>
          <div className="pt-4">
            <button
              disabled={isSubmitting}
              className={`w-full bg-primary text-on-primary py-5 rounded-xl font-headline font-bold text-lg hover:bg-primary-container transition-all shadow-lg shadow-primary/10 active:scale-[0.98] ${isSubmitting ? 'opacity-80 cursor-wait' : ''}`}
              type="submit"
            >
              {isSubmitting ? 'Connecting to Secure Server...' : 'Submit Audit Request'}
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
