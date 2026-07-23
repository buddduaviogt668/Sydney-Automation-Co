import { useState } from "react";
import { Link, useLocation } from "wouter";
import { ArrowLeft, Check } from "lucide-react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { useCreateBooking, useCreateCheckoutSession } from "@workspace/api-client-react";
import type { Booking, CheckoutSession } from "@workspace/api-client-react";

const bookingSchema = z.object({
  name: z.string().min(1, "Name is required"),
  email: z.string().email("Valid email required"),
  phone: z.string().min(8, "Valid phone number required"),
  address: z.string().min(1, "Address is required"),
  suburb: z.string().min(1, "Suburb is required"),
  serviceType: z.string().min(1, "Select a service"),
  description: z.string().optional(),
  preferredDate: z.string().min(1, "Preferred date is required"),
});

type BookingFormData = z.infer<typeof bookingSchema>;

const serviceTypes = [
  "C-Bus Repair",
  "C-Bus Programming",
  "Dynalite Repair",
  "Dynalite Programming",
  "DALI Fault Finding",
  "Emergency Lighting",
  "Other",
];

export default function Book() {
  const [, navigate] = useLocation();
  const [step, setStep] = useState(1);
  const bookingMutation = useCreateBooking();
  const checkoutMutation = useCreateCheckoutSession();

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<BookingFormData>({
    resolver: zodResolver(bookingSchema),
    defaultValues: { description: "" },
  });

  const selectedService = watch("serviceType");

  const onSubmit = (data: BookingFormData) => {
    bookingMutation.mutate(data, {
      onSuccess: (booking: Booking) => {
        checkoutMutation.mutate(
          { bookingId: String(booking.id) },
          {
            onSuccess: (session: CheckoutSession) => {
              window.location.href = session.url;
            },
            onError: () => {
              navigate("/book/success");
            },
          },
        );
      },
    });
  };

  return (
    <div className="min-h-[calc(100vh-57px)] bg-gray-50 px-4 py-8">
      <div className="mx-auto max-w-lg">
        <div className="mb-6 flex items-center gap-3">
          <Link href="/" className="text-gray-400 hover:text-gray-600">
            <ArrowLeft className="h-5 w-5" />
          </Link>
          <h1 className="text-xl font-bold text-gray-900">Book a Service Call</h1>
        </div>

        {/* Progress */}
        <div className="mb-8 flex items-center gap-2">
          {[1, 2, 3].map((s) => (
            <div key={s} className="flex items-center gap-2">
              <div
                className={`flex h-8 w-8 items-center justify-center rounded-full text-sm font-semibold ${
                  step >= s ? "bg-amber-600 text-white" : "bg-gray-200 text-gray-500"
                }`}
              >
                {step > s ? <Check className="h-4 w-4" /> : s}
              </div>
              {s < 3 && <div className={`h-0.5 w-12 ${step > s ? "bg-amber-600" : "bg-gray-200"}`} />}
            </div>
          ))}
        </div>

        <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
          <form onSubmit={handleSubmit(onSubmit)}>
            {/* Step 1: Service Type */}
            {step === 1 && (
              <div>
                <h2 className="mb-4 text-lg font-semibold text-gray-900">What do you need?</h2>
                <div className="space-y-2">
                  {serviceTypes.map((type) => (
                    <label
                      key={type}
                      className={`flex cursor-pointer items-center gap-3 rounded-lg border p-3 transition-colors ${
                        selectedService === type
                          ? "border-amber-500 bg-amber-50"
                          : "border-gray-200 hover:border-gray-300"
                      }`}
                    >
                      <input
                        type="radio"
                        value={type}
                        {...register("serviceType")}
                        className="sr-only"
                      />
                      <div
                        className={`flex h-4 w-4 items-center justify-center rounded-full border-2 ${
                          selectedService === type ? "border-amber-500" : "border-gray-300"
                        }`}
                      >
                        {selectedService === type && <div className="h-2 w-2 rounded-full bg-amber-500" />}
                      </div>
                      <span className="text-sm font-medium text-gray-900">{type}</span>
                    </label>
                  ))}
                </div>
                {errors.serviceType && (
                  <p className="mt-2 text-xs text-red-600">{errors.serviceType.message}</p>
                )}
                <button
                  type="button"
                  onClick={() => setStep(2)}
                  disabled={!selectedService}
                  className="mt-6 w-full rounded-lg bg-amber-600 py-3 text-sm font-semibold text-white transition-colors hover:bg-amber-700 disabled:opacity-50"
                >
                  Next
                </button>
              </div>
            )}

            {/* Step 2: Job Details */}
            {step === 2 && (
              <div>
                <h2 className="mb-4 text-lg font-semibold text-gray-900">Job Details</h2>
                <div className="space-y-4">
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Address</label>
                    <input
                      {...register("address")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="123 Example St"
                    />
                    {errors.address && <p className="mt-1 text-xs text-red-600">{errors.address.message}</p>}
                  </div>
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Suburb</label>
                    <input
                      {...register("suburb")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="Mosman"
                    />
                    {errors.suburb && <p className="mt-1 text-xs text-red-600">{errors.suburb.message}</p>}
                  </div>
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Preferred Date</label>
                    <input
                      type="date"
                      {...register("preferredDate")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                    />
                    {errors.preferredDate && <p className="mt-1 text-xs text-red-600">{errors.preferredDate.message}</p>}
                  </div>
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Describe the issue (optional)</label>
                    <textarea
                      {...register("description")}
                      rows={3}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="Lights flickering, C-Bus interface not responding, etc."
                    />
                  </div>
                </div>
                <div className="mt-6 flex gap-3">
                  <button
                    type="button"
                    onClick={() => setStep(1)}
                    className="flex-1 rounded-lg border border-gray-300 py-3 text-sm font-semibold text-gray-700 transition-colors hover:bg-gray-50"
                  >
                    Back
                  </button>
                  <button
                    type="button"
                    onClick={() => setStep(3)}
                    className="flex-1 rounded-lg bg-amber-600 py-3 text-sm font-semibold text-white transition-colors hover:bg-amber-700"
                  >
                    Next
                  </button>
                </div>
              </div>
            )}

            {/* Step 3: Contact Info */}
            {step === 3 && (
              <div>
                <h2 className="mb-4 text-lg font-semibold text-gray-900">Your Details</h2>
                <div className="space-y-4">
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Full Name</label>
                    <input
                      {...register("name")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="George Skarmoutsos"
                    />
                    {errors.name && <p className="mt-1 text-xs text-red-600">{errors.name.message}</p>}
                  </div>
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Email</label>
                    <input
                      type="email"
                      {...register("email")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="george@example.com"
                    />
                    {errors.email && <p className="mt-1 text-xs text-red-600">{errors.email.message}</p>}
                  </div>
                  <div>
                    <label className="mb-1 block text-sm font-medium text-gray-700">Phone</label>
                    <input
                      type="tel"
                      {...register("phone")}
                      className="w-full rounded-lg border border-gray-300 px-3 py-2.5 text-sm focus:border-amber-500 focus:outline-none"
                      placeholder="0422 469 739"
                    />
                    {errors.phone && <p className="mt-1 text-xs text-red-600">{errors.phone.message}</p>}
                  </div>
                </div>

                <div className="mt-6 rounded-lg bg-amber-50 p-4">
                  <p className="text-sm text-gray-700">
                    <strong>$200+GST deposit</strong> required to lock in your booking. George will call you within 2 hours to confirm.
                  </p>
                </div>

                <div className="mt-6 flex gap-3">
                  <button
                    type="button"
                    onClick={() => setStep(2)}
                    className="flex-1 rounded-lg border border-gray-300 py-3 text-sm font-semibold text-gray-700 transition-colors hover:bg-gray-50"
                  >
                    Back
                  </button>
                  <button
                    type="submit"
                    disabled={bookingMutation.isPending || checkoutMutation.isPending}
                    className="flex-1 rounded-lg bg-amber-600 py-3 text-sm font-semibold text-white transition-colors hover:bg-amber-700 disabled:opacity-50"
                  >
                    {bookingMutation.isPending || checkoutMutation.isPending
                      ? "Processing..."
                      : "Pay $200 Deposit & Book"}
                  </button>
                </div>
              </div>
            )}
          </form>
        </div>

        <p className="mt-4 text-center text-xs text-gray-500">
          Service calls are $200+GST upfront + $50/hr+GST (3hr min) on the day.
        </p>
      </div>
    </div>
  );
}
