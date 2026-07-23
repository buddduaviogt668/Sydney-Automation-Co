import { useState, useEffect, useCallback } from "react";
import { X } from "lucide-react";
import { useCaptureLead } from "@workspace/api-client-react";

export default function ExitIntentPopup() {
  const [show, setShow] = useState(false);
  const [email, setEmail] = useState("");
  const [dismissed, setDismissed] = useState(false);
  const leadMutation = useCaptureLead();

  const handleMouseLeave = useCallback(
    (e: MouseEvent) => {
      if (dismissed) return;
      if (e.clientY <= 0 && !show) {
        setShow(true);
      }
    },
    [dismissed, show],
  );

  useEffect(() => {
    const wasDismissed = sessionStorage.getItem("exit-popup-dismissed");
    if (wasDismissed) {
      setDismissed(true);
      return;
    }

    document.addEventListener("mouseleave", handleMouseLeave);
    return () => document.removeEventListener("mouseleave", handleMouseLeave);
  }, [handleMouseLeave]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim()) return;

    leadMutation.mutate(
      { email: email.trim(), source: "exit-intent-popup" },
      {
        onSuccess: () => {
          setEmail("");
          setShow(false);
          setDismissed(true);
          sessionStorage.setItem("exit-popup-dismissed", "true");
        },
      },
    );
  };

  const handleDismiss = () => {
    setShow(false);
    setDismissed(true);
    sessionStorage.setItem("exit-popup-dismissed", "true");
  };

  if (!show) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
      <div className="relative mx-4 w-full max-w-md rounded-xl bg-white p-6 shadow-2xl">
        <button
          onClick={handleDismiss}
          className="absolute right-3 top-3 text-gray-400 hover:text-gray-600"
          aria-label="Close"
        >
          <X className="h-5 w-5" />
        </button>

        <h2 className="mb-2 text-lg font-bold text-gray-900">
          Don't leave with a faulty system.
        </h2>
        <p className="mb-4 text-sm text-gray-600">
          Drop your email and we'll send you a free fault-finding checklist for C-Bus and Dynalite systems.
        </p>

        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="your@email.com"
            required
            className="rounded-lg border border-gray-300 px-4 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
          />
          <button
            type="submit"
            disabled={leadMutation.isPending}
            className="rounded-lg bg-amber-600 px-4 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-amber-700 disabled:opacity-50"
          >
            {leadMutation.isPending ? "Sending..." : "Send me the checklist"}
          </button>
        </form>

        <p className="mt-3 text-center text-xs text-gray-400">
          No spam. Unsubscribe anytime.
        </p>
      </div>
    </div>
  );
}
