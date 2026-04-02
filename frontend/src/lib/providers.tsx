'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useState } from 'react';

export function Providers({ children }: { children: React.ReactNode }) {
  const [client] = useState(() => new QueryClient({
    defaultOptions: {
      queries: { staleTime: 1000 * 60 * 5, refetchOnWindowFocus: false, retry: 1 },
    },
  }));

  // WebSocket for real-time monitoring
  return (
    <QueryClientProvider client={client}>
      {children}
    </QueryClientProvider>
  );
}
