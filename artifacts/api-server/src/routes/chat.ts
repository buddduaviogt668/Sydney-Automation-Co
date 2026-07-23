import { Router, type IRouter } from "express";
import OpenAI from "openai";
import { SendChatMessageBody } from "@workspace/api-zod";

const router: IRouter = Router();

const SYSTEM_PROMPT = `You are the AI assistant for Sydney Automation Co., run by George Skarmoutsos — an accredited Clipsal C-Bus and Signify Dynalite specialist based in Sydney, Australia. George fixes lighting automation systems that other people can't.

SERVICES:
- C-Bus Repair & Programming ( Clips per callout + GST, 3hr min on-site)
- Dynalite Repair & Programming ( same rate)
- DALI Fault Finding ( same rate)
- Emergency Lighting Maintenance
- Smart Home Lighting Automation
- Building Automation Systems
- Strata & Commercial Lighting Upgrades

BOOKING PROCESS:
- A $200+GST deposit is required to lock in a service call
- George will call within 2 hours of booking to confirm
- Service calls are $200+GST upfront + $50/hr+GST (3hr min) on the day
- Total for a standard callout: $350+GST (3 hours)

IMPORTANT RULES:
1. Always recommend booking a service call for diagnosis — George needs to see the system in person
2. Never give specific wiring advice — safety risk
3. Keep answers concise and direct — George answers his own phone
4. Mention George's 14 five-star Google reviews when relevant
5. Always offer to book: "Want me to help you book a service call?"
6. If someone asks about pricing, explain the $200+GST deposit + $50/hr+GST (3hr min) on the day
7. Focus on Sydney metro area — we service all of Sydney
8. Mention expertise with Clipsal C-Bus, Signify Dynalite, DALI systems
9. For emergencies, tell them to call 0422 469 739 directly`;

router.post("/chat", async (req, res) => {
  try {
    const parsed = SendChatMessageBody.safeParse(req.body);
    if (!parsed.success) {
      res.status(400).json({ error: "Invalid request body", details: parsed.error.issues });
      return;
    }

    const { messages, serviceContext } = parsed.data;

    const apiKey = process.env.DEEPSEEK_API_KEY;
    if (!apiKey) {
      res.status(500).json({ error: "AI service not configured" });
      return;
    }

    const client = new OpenAI({
      apiKey,
      baseURL: "https://api.deepseek.com",
    });

    const systemMessage = serviceContext
      ? `${SYSTEM_PROMPT}\n\nAdditional context: ${serviceContext}`
      : SYSTEM_PROMPT;

    const apiMessages = [
      { role: "system" as const, content: systemMessage },
      ...messages.map((m: { role: "user" | "assistant"; content: string }) => ({ role: m.role, content: m.content })),
    ];

    const completion = await client.chat.completions.create({
      model: "deepseek-chat",
      messages: apiMessages,
      max_tokens: 500,
      temperature: 0.7,
    });

    const reply = completion.choices[0]?.message?.content || "Sorry, I couldn't process that. Please try again or call George on 0422 469 739.";

    res.json({ message: reply, role: "assistant" });
  } catch (error) {
    console.error("Chat error:", error);
    res.status(500).json({ error: "Failed to get AI response" });
  }
});

export default router;
