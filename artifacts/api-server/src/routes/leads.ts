import { Router, type IRouter } from "express";
import { CaptureLeadBody } from "@workspace/api-zod";
import { db } from "@workspace/db";
import { leadsTable } from "@workspace/db/schema";

const router: IRouter = Router();

router.post("/leads", async (req, res) => {
  try {
    const parsed = CaptureLeadBody.safeParse(req.body);
    if (!parsed.success) {
      res.status(400).json({ error: "Invalid request body", details: parsed.error.issues });
      return;
    }

    const { email, source } = parsed.data;

    const [lead] = await db
      .insert(leadsTable)
      .values({ email, source: source || "exit-intent-popup" })
      .returning();

    res.status(201).json(lead);
  } catch (error) {
    console.error("Capture lead error:", error);
    res.status(500).json({ error: "Failed to capture lead" });
  }
});

export default router;
