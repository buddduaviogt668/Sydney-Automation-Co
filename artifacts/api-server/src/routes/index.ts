import { Router, type IRouter } from "express";
import healthRouter from "./health";
import chatRouter from "./chat";
import bookingsRouter from "./bookings";
import leadsRouter from "./leads";
import stripeRouter from "./stripe";

const router: IRouter = Router();

router.use(healthRouter);
router.use(chatRouter);
router.use(bookingsRouter);
router.use(leadsRouter);
router.use(stripeRouter);

export default router;
