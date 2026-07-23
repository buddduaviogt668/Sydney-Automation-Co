import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from '@/components/ui/toaster';
import { TooltipProvider } from '@/components/ui/tooltip';
import Layout from '@/components/Layout';
import ChatWidget from '@/components/ChatWidget';
import ExitIntentPopup from '@/components/ExitIntentPopup';
import Home from '@/pages/Home';
import Chat from '@/pages/Chat';
import Book from '@/pages/Book';
import BookSuccess from '@/pages/BookSuccess';
import NotFound from '@/pages/not-found';
import { Route, Switch, Router as WouterRouter } from 'wouter';

const queryClient = new QueryClient();

function Router() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/chat" component={Chat} />
      <Route path="/book" component={Book} />
      <Route path="/book/success" component={BookSuccess} />
      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <WouterRouter base={import.meta.env.BASE_URL.replace(/\/$/, '')}>
          <Layout>
            <Router />
          </Layout>
          <ChatWidget />
          <ExitIntentPopup />
        </WouterRouter>
        <Toaster />
      </TooltipProvider>
    </QueryClientProvider>
  );
}

export default App;
