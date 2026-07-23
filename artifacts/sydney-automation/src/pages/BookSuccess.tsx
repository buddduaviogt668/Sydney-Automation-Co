import { Link } from "wouter";
import { CheckCircle, Phone, ArrowLeft } from "lucide-react";

export default function BookSuccess() {
  return (
    <div className="min-h-[calc(100vh-57px)] bg-gray-50 px-4 py-16">
      <div className="mx-auto max-w-lg text-center">
        <div className="mb-6 flex justify-center">
          <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
            <CheckCircle className="h-8 w-8 text-green-600" />
          </div>
        </div>

        <h1 className="mb-3 text-2xl font-bold text-gray-900">Booking Confirmed</h1>

        <p className="mb-2 text-lg text-gray-700">
          $200+GST deposit received.
        </p>
        <p className="mb-6 text-gray-600">
          George will call you within 2 hours to confirm your booking and discuss the details.
        </p>

        <div className="mb-8 rounded-xl border border-gray-200 bg-white p-6">
          <h2 className="mb-3 text-sm font-semibold text-gray-900">What happens next?</h2>
          <ol className="space-y-3 text-left text-sm text-gray-600">
            <li className="flex gap-3">
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-semibold text-amber-700">1</span>
              George calls you to confirm the date and discuss the issue
            </li>
            <li className="flex gap-3">
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-semibold text-amber-700">2</span>
              George arrives on-site and diagnoses the fault
            </li>
            <li className="flex gap-3">
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-semibold text-amber-700">3</span>
              On-site rate: $50/hr+GST (3hr min) on the day
            </li>
          </ol>
        </div>

        <div className="flex flex-col items-center gap-3">
          <Link
            href="/"
            className="inline-flex items-center gap-2 rounded-lg bg-amber-600 px-6 py-3 text-sm font-semibold text-white transition-colors hover:bg-amber-700"
          >
            <ArrowLeft className="h-4 w-4" />
            Back to Home
          </Link>
          <a
            href="tel:0422469739"
            className="inline-flex items-center gap-2 text-sm font-medium text-gray-600 hover:text-amber-600"
          >
            <Phone className="h-4 w-4" />
            Call George directly — 0422 469 739
          </a>
        </div>
      </div>
    </div>
  );
}
