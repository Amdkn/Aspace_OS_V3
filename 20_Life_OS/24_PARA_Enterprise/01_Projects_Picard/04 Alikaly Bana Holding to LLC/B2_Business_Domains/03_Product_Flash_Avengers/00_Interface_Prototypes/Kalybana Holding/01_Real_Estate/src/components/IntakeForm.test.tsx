import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import IntakeForm from './IntakeForm';
import { Toaster } from 'react-hot-toast';

describe('IntakeForm Component', () => {
  it('renders correctly', () => {
    render(
      <>
        <Toaster />
        <IntakeForm />
      </>
    );
    expect(screen.getByText(/Start Your Recovery Audit/i)).toBeDefined();
  });

  it('validates required fields', async () => {
    render(
      <>
        <Toaster />
        <IntakeForm />
      </>
    );
    
    const submitBtn = screen.getByRole('button', { name: /Submit Audit Request/i });
    fireEvent.click(submitBtn);

    // HTML5 validation or Zod toast
    // Note: Since I'm using HTML5 'required', the form won't submit.
    expect(screen.getByPlaceholderText(/e.g. John/i)).toBeRequired();
  });
});
