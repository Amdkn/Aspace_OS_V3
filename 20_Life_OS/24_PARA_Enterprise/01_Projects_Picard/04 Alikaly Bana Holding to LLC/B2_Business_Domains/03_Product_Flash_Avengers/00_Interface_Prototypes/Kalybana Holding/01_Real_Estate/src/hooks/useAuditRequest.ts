import { useState } from 'react';
import { supabase } from '../lib/supabase';
import { AuditRequest } from '../types';
import { z } from 'zod';
import { toast } from 'react-hot-toast';

export const AuditSchema = z.object({
  firstName: z.string().min(2, 'Prénom requis'),
  lastName: z.string().min(2, 'Nom requis'),
  propertyAddress: z.string().min(5, 'Adresse valide requise'),
  caseNumber: z.string().optional(),
});

export function useAuditRequest() {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const submitAudit = async (data: AuditRequest) => {
    setIsSubmitting(true);
    const loadingToast = toast.loading('Transmission sécurisée en cours...');

    try {
      // Logic validation
      AuditSchema.parse(data);

      if (supabase) {
        const { error } = await supabase
          .from('audit_requests')
          .insert([{ ...data, status: 'PENDING' }]);
        
        if (error) throw error;
      } else {
        // Simulation pour le local host si Supabase non configuré
        await new Promise(resolve => setTimeout(resolve, 1500));
        console.log('Mock submission:', data);
      }

      toast.success('Demande d\'audit reçue. Un agent vous contactera sous 24h.', { id: loadingToast });
      return true;
    } catch (err: any) {
      const message = err instanceof z.ZodError 
        ? err.errors[0].message 
        : 'Erreur lors de la transmission. Veuillez réessayer.';
      
      toast.error(message, { id: loadingToast });
      return false;
    } finally {
      setIsSubmitting(false);
    }
  };

  return { submitAudit, isSubmitting };
}
