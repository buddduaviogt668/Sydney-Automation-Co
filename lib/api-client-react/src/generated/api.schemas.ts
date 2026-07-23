export interface HealthStatus {
  status: string;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface ChatRequest {
  messages: ChatMessage[];
  serviceContext?: string;
}

export interface ChatResponse {
  message: string;
  role: string;
}

export interface CreateBookingInput {
  name: string;
  email: string;
  phone: string;
  address: string;
  suburb: string;
  serviceType: string;
  description?: string;
  preferredDate: string;
}

export interface Booking {
  id: number;
  name: string;
  email: string;
  phone: string;
  address: string;
  suburb: string;
  serviceType: string;
  description?: string;
  preferredDate: string;
  depositAmount: number;
  stripeSessionId?: string;
  status: string;
  createdAt: string;
}

export interface CheckoutSessionInput {
  bookingId: string;
}

export interface CheckoutSession {
  url: string;
  sessionId: string;
}

export interface CaptureLeadInput {
  email: string;
  source?: string;
}

export interface Lead {
  id: number;
  email: string;
  source?: string;
  createdAt: string;
}
