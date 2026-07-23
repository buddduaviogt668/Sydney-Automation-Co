import { Link, useLocation } from "wouter";
import { Phone, Menu, X } from "lucide-react";
import { useState } from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [location] = useLocation();

  return (
    <div className="min-h-screen bg-white text-gray-900">
      <header className="sticky top-0 z-40 border-b border-gray-200 bg-white/95 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
          <Link href="/" className="flex items-center gap-2">
            <span className="text-lg font-bold tracking-tight text-gray-900">
              Sydney Automation Co.
            </span>
          </Link>

          <nav className="hidden items-center gap-6 md:flex">
            <Link
              href="/chat"
              className={`text-sm font-medium transition-colors hover:text-amber-600 ${location === "/chat" ? "text-amber-600" : "text-gray-600"}`}
            >
              AI Chat
            </Link>
            <Link
              href="/book"
              className="inline-flex items-center gap-2 rounded-lg bg-amber-600 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-amber-700"
            >
              Book Now
            </Link>
            <a
              href="tel:0422469739"
              className="inline-flex items-center gap-1.5 text-sm font-medium text-gray-600 transition-colors hover:text-amber-600"
            >
              <Phone className="h-4 w-4" />
              0422 469 739
            </a>
          </nav>

          <button
            className="md:hidden"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {mobileOpen && (
          <div className="border-t border-gray-200 bg-white px-4 py-4 md:hidden">
            <div className="flex flex-col gap-3">
              <Link href="/chat" onClick={() => setMobileOpen(false)} className="text-sm font-medium text-gray-600">
                AI Chat
              </Link>
              <Link href="/book" onClick={() => setMobileOpen(false)} className="rounded-lg bg-amber-600 px-4 py-2 text-center text-sm font-semibold text-white">
                Book Now
              </Link>
              <a href="tel:0422469739" className="text-sm font-medium text-gray-600">
                Call 0422 469 739
              </a>
            </div>
          </div>
        )}
      </header>

      <main>{children}</main>

      <footer className="border-t border-gray-200 bg-gray-50">
        <div className="mx-auto max-w-6xl px-4 py-8">
          <div className="grid gap-8 md:grid-cols-3">
            <div>
              <h3 className="mb-2 text-sm font-bold text-gray-900">Sydney Automation Co.</h3>
              <p className="text-sm text-gray-600">
                Accredited Clipsal C-Bus and Signify Dynalite specialist in Sydney.
                George Skarmoutsos — fixing what others can't.
              </p>
            </div>
            <div>
              <h3 className="mb-2 text-sm font-bold text-gray-900">Services</h3>
              <ul className="space-y-1 text-sm text-gray-600">
                <li>C-Bus Repair & Programming</li>
                <li>Dynalite Repair & Programming</li>
                <li>DALI Fault Finding</li>
                <li>Emergency Lighting</li>
                <li>Smart Home Automation</li>
              </ul>
            </div>
            <div>
              <h3 className="mb-2 text-sm font-bold text-gray-900">Contact</h3>
              <ul className="space-y-1 text-sm text-gray-600">
                <li>
                  <a href="tel:0422469739" className="hover:text-amber-600">0422 469 739</a>
                </li>
                <li>Sydney Metro Area</li>
                <li>
                  <Link href="/book" className="hover:text-amber-600">Book a Service Call</Link>
                </li>
              </ul>
            </div>
          </div>
          <div className="mt-8 border-t border-gray-200 pt-4 text-center text-xs text-gray-500">
            George Skarmoutsos T/A Sydney Automation Co. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}
