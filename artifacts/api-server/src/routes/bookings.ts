import { Router, type IRouter } from "express";
import { CreateBookingBody } from "@workspace/api-zod";
import { eq } from "drizzle-orm";
import { db } from "@workspace/db";
import { bookingsTable } from "@workspace/db/schema";

const router: IRouter = Router();

router.post("/bookings", async (req, res) => {
  try {
    const parsed = CreateBookingBody.safeParse(req.body);
    if (!parsed.success) {
      res.status(400).json({ error: "Invalid request body", details: parsed.error.issues });
      return;
    }

    const data = parsed.data;

    const [booking] = await db
      .insert(bookingsTable)
      .values({
        name: data.name,
        email: data.email,
        phone: data.phone,
        address: data.address,
        suburb: data.suburb,
        serviceType: data.serviceType,
        description: data.description || "",
        preferredDate: data.preferredDate,
      })
      .returning();

    res.status(201).json(booking);
  } catch (error) {
    console.error("Create booking error:", error);
    res.status(500).json({ error: "Failed to create booking" });
  }
});

router.get("/bookings", async (_req, res) => {
  try {
    const bookings = await db.select().from(bookingsTable);
    res.json(bookings);
  } catch (error) {
    console.error("List bookings error:", error);
    res.status(500).json({ error: "Failed to list bookings" });
  }
});

router.get("/bookings/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const [booking] = await db
      .select()
      .from(bookingsTable)
      .where(eq(bookingsTable.id, Number(id)));

    if (!booking) {
      res.status(404).json({ error: "Booking not found" });
      return;
    }

    res.json(booking);
  } catch (error) {
    console.error("Get booking error:", error);
    res.status(500).json({ error: "Failed to get booking" });
  }
});

export default router;
