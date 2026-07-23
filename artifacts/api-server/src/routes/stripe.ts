import { Router, type IRouter } from "express";
import { eq } from "drizzle-orm";
import { CreateCheckoutSessionBody } from "@workspace/api-zod";
import { db } from "@workspace/db";
import { bookingsTable } from "@workspace/db/schema";
import Stripe from "stripe";

const router: IRouter = Router();

router.post("/checkout-sessions", async (req, res) => {
  try {
    const parsed = CreateCheckoutSessionBody.safeParse(req.body);
    if (!parsed.success) {
      res.status(400).json({ error: "Invalid request body", details: parsed.error.issues });
      return;
    }

    const { bookingId } = parsed.data;

    const [booking] = await db
      .select()
      .from(bookingsTable)
      .where(eq(bookingsTable.id, Number(bookingId)));

    if (!booking) {
      res.status(404).json({ error: "Booking not found" });
      return;
    }

    const stripeSecretKey = process.env.STRIPE_SECRET_KEY;
    if (!stripeSecretKey) {
      res.status(500).json({ error: "Stripe not configured" });
      return;
    }

    const stripe = new Stripe(stripeSecretKey);

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price_data: {
            currency: "aud",
            product_data: {
              name: `Service Call Deposit - ${booking.serviceType}`,
              description: `Booking for ${booking.suburb}. George will call within 2 hours to confirm.`,
            },
            unit_amount: 22000, // $220 AUD in cents = $200 + GST
          },
          quantity: 1,
        },
      ],
      mode: "payment",
      success_url: `${process.env.APP_URL || "http://localhost:5173"}/book/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.APP_URL || "http://localhost:5173"}/book`,
      customer_email: booking.email,
      metadata: {
        bookingId: String(booking.id),
        serviceType: booking.serviceType,
        suburb: booking.suburb,
      },
    });

    await db
      .update(bookingsTable)
      .set({ stripeSessionId: session.id, status: "checkout_created" })
      .where(eq(bookingsTable.id, booking.id));

    res.json({ url: session.url!, sessionId: session.id });
  } catch (error) {
    console.error("Create checkout session error:", error);
    res.status(500).json({ error: "Failed to create checkout session" });
  }
});

export default router;
