import { Link } from "wouter";
import { Zap, Lightbulb, AlertTriangle, Shield, Star, ChevronRight } from "lucide-react";

const services = [
  {
    icon: Zap,
    title: "C-Bus Repair & Programming",
    description: "Diagnosing and fixing Clipsal C-Bus systems — network faults, interface failures, programming errors. We fix what others can't.",
  },
  {
    icon: Lightbulb,
    title: "Dynalite Repair & Programming",
    description: "Signify Dynalite specialist. Network communication faults, bus crashes, stuck channels, surge damage. All models covered.",
  },
  {
    icon: AlertTriangle,
    title: "DALI Fault Finding",
    description: "Systematic DALI bus diagnostics. Finding failed drivers, wiring faults, and communication issues across commercial and residential installs.",
  },
  {
    icon: Shield,
    title: "Emergency Lighting",
    description: "Maintenance, testing, and compliance for emergency exit lighting systems. Annual testing and certification.",
  },
];

const reviews = [
  { name: "James M.", text: "George found a C-Bus network fault that two other electricians missed. Fixed it in an hour.", rating: 5 },
  { name: "Sarah K.", text: "Our Dynalite system was completely dead. George had it running the same day. Highly recommend.", rating: 5 },
  { name: "David L.", text: "Professional, knowledgeable, and honest. Rare to find someone who actually knows C-Bus inside out.", rating: 5 },
];

const faqs = [
  { q: "How much does a service call cost?", a: "$200+GST upfront to lock in the visit. On-site rate is $50/hr+GST with a 3-hour minimum. A standard diagnostic callout runs $350+GST total (3 hours)." },
  { q: "Do you service my area?", a: "We cover all of Sydney metro — from the CBD to the Northern Beaches, Eastern Suburbs, Western Sydney, Sutherland Shire, and everywhere in between." },
  { q: "My system is completely dead. Can you fix it?", a: "That's exactly what we specialise in. Call George on 0422 469 739 and we'll get you booked in." },
  { q: "How quickly can you come out?", a: "We aim to schedule within 1-2 business days. For urgent issues, call directly and we'll do our best to accommodate." },
];

export default function Home() {
  return (
    <div>
      {/* Hero */}
      <section className="bg-gray-900 px-4 py-16 text-white md:py-24">
        <div className="mx-auto max-w-4xl text-center">
          <p className="mb-4 text-sm font-medium uppercase tracking-widest text-amber-400">
            Sydney's C-Bus & Dynalite Specialist
          </p>
          <h1 className="mb-6 text-4xl font-bold leading-tight md:text-5xl">
            We Fix Lighting Automation Systems
            <br />
            <span className="text-amber-400">That Other People Can't</span>
          </h1>
          <p className="mb-8 max-w-2xl mx-auto text-lg text-gray-300">
            Accredited Clipsal C-Bus and Signify Dynalite specialist. George Skarmoutsos —
            14 five-star Google reviews. Fast, direct, zero fuss.
          </p>
          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link
              href="/book"
              className="inline-flex items-center gap-2 rounded-lg bg-amber-600 px-6 py-3 text-base font-semibold text-white transition-colors hover:bg-amber-700"
            >
              Book a Service Call
              <ChevronRight className="h-4 w-4" />
            </Link>
            <a
              href="tel:0422469739"
              className="inline-flex items-center gap-2 rounded-lg border border-gray-600 px-6 py-3 text-base font-semibold text-white transition-colors hover:border-amber-400 hover:text-amber-400"
            >
              Call 0422 469 739
            </a>
          </div>
        </div>
      </section>

      {/* Social Proof */}
      <section className="border-b border-gray-200 bg-amber-50 px-4 py-6">
        <div className="mx-auto flex max-w-4xl items-center justify-center gap-2 text-sm text-gray-700">
          <div className="flex">
            {[...Array(5)].map((_, i) => (
              <Star key={i} className="h-4 w-4 fill-amber-500 text-amber-500" />
            ))}
          </div>
          <span className="font-medium">14 five-star Google reviews</span>
          <span className="text-gray-400">|</span>
          <span>Accredited specialist</span>
          <span className="text-gray-400">|</span>
          <span>Sydney wide</span>
        </div>
      </section>

      {/* Services */}
      <section className="px-4 py-16">
        <div className="mx-auto max-w-6xl">
          <h2 className="mb-2 text-center text-2xl font-bold text-gray-900">Our Services</h2>
          <p className="mb-10 text-center text-gray-600">Specialist lighting automation repair, programming, and maintenance</p>
          <div className="grid gap-6 md:grid-cols-2">
            {services.map((s) => (
              <div key={s.title} className="rounded-xl border border-gray-200 p-6 transition-shadow hover:shadow-md">
                <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-lg bg-amber-100">
                  <s.icon className="h-5 w-5 text-amber-600" />
                </div>
                <h3 className="mb-2 text-lg font-semibold text-gray-900">{s.title}</h3>
                <p className="text-sm text-gray-600">{s.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Reviews */}
      <section className="bg-gray-50 px-4 py-16">
        <div className="mx-auto max-w-6xl">
          <h2 className="mb-2 text-center text-2xl font-bold text-gray-900">What Clients Say</h2>
          <p className="mb-10 text-center text-gray-600">14 five-star reviews on Google</p>
          <div className="grid gap-6 md:grid-cols-3">
            {reviews.map((r) => (
              <div key={r.name} className="rounded-xl border border-gray-200 bg-white p-6">
                <div className="mb-3 flex">
                  {[...Array(r.rating)].map((_, i) => (
                    <Star key={i} className="h-4 w-4 fill-amber-500 text-amber-500" />
                  ))}
                </div>
                <p className="mb-3 text-sm text-gray-600">{r.text}</p>
                <p className="text-sm font-medium text-gray-900">{r.name}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQs */}
      <section className="px-4 py-16">
        <div className="mx-auto max-w-3xl">
          <h2 className="mb-2 text-center text-2xl font-bold text-gray-900">Common Questions</h2>
          <p className="mb-10 text-center text-gray-600">Everything you need to know before booking</p>
          <div className="space-y-4">
            {faqs.map((f) => (
              <div key={f.q} className="rounded-xl border border-gray-200 p-6">
                <h3 className="mb-2 text-base font-semibold text-gray-900">{f.q}</h3>
                <p className="text-sm text-gray-600">{f.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-amber-600 px-4 py-16 text-center text-white">
        <div className="mx-auto max-w-2xl">
          <h2 className="mb-4 text-2xl font-bold">Ready to Fix Your Lighting System?</h2>
          <p className="mb-6 text-amber-100">
            Book a service call. George will call you within 2 hours to confirm.
          </p>
          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link
              href="/book"
              className="inline-flex items-center gap-2 rounded-lg bg-white px-6 py-3 text-base font-semibold text-amber-700 transition-colors hover:bg-amber-50"
            >
              Book a Service Call — $200 Deposit
            </Link>
            <a
              href="tel:0422469739"
              className="inline-flex items-center gap-2 rounded-lg border border-amber-400 px-6 py-3 text-base font-semibold text-white transition-colors hover:bg-amber-700"
            >
              Or Call 0422 469 739
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}
