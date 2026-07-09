import { describe, it, expect } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from '../context/AuthContext';
import Portfolio from './Portfolio';

describe('Portfolio Component', () => {
  it('renders the loading state initially and then the headline', async () => {
    render(
      <AuthProvider>
        <BrowserRouter>
          <Portfolio />
        </BrowserRouter>
      </AuthProvider>
    );
    
    // Check for loader
    expect(screen.getByRole('status')).toBeDefined();
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).toBeNull();
    }, { timeout: 2000 });

    // Check for headline
    expect(screen.getByText(/Architecting Value in/i)).toBeDefined();
  });
});
