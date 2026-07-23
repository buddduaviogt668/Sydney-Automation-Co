import { useMutation, useQuery } from "@tanstack/react-query";
import type { UseQueryOptions } from "@tanstack/react-query";
import { customFetch } from "../custom-fetch";
import type { ErrorType } from "../custom-fetch";

type AwaitedInput<T> = PromiseLike<T> | T;
type Awaited<O> = O extends AwaitedInput<infer T> ? T : never;
type SecondParameter<T extends (...args: never) => unknown> = Parameters<T>[1];

import type {
  HealthStatus,
  ChatRequest,
  ChatResponse,
  CreateBookingInput,
  Booking,
  CheckoutSessionInput,
  CheckoutSession,
  CaptureLeadInput,
  Lead,
} from "./api.schemas";

// ---------------------------------------------------------------------------
// Health Check
// ---------------------------------------------------------------------------

export const getHealthCheckUrl = () => `/api/healthz`;

export const healthCheck = async (options?: RequestInit): Promise<HealthStatus> => {
  return customFetch<HealthStatus>(getHealthCheckUrl(), { ...options, method: "GET" });
};

export const getHealthCheckQueryKey = () => [`/api/healthz`] as const;

export function useHealthCheck<
  TData = Awaited<ReturnType<typeof healthCheck>>,
  TError = ErrorType<unknown>,
>(options?: {
  query?: UseQueryOptions<Awaited<ReturnType<typeof healthCheck>>, TError, TData>;
  request?: SecondParameter<typeof customFetch>;
}) {
  const queryOptions = {
    queryKey: options?.query?.queryKey ?? getHealthCheckQueryKey(),
    queryFn: ({ signal }: { signal: AbortSignal }) => healthCheck({ signal, ...options?.request }),
    ...options?.query,
  };
  const query = useQuery(queryOptions) as import("@tanstack/react-query").UseQueryResult<TData, TError> & { queryKey: import("@tanstack/react-query").QueryKey };
  return { ...query, queryKey: queryOptions.queryKey };
}

// ---------------------------------------------------------------------------
// Send Chat Message
// ---------------------------------------------------------------------------

export const getSendChatMessageUrl = () => `/api/chat`;

export const sendChatMessage = async (
  data: ChatRequest,
  options?: RequestInit,
): Promise<ChatResponse> => {
  return customFetch<ChatResponse>(getSendChatMessageUrl(), {
    ...options,
    method: "POST",
    headers: { "Content-Type": "application/json", ...options?.headers },
    body: JSON.stringify(data),
  });
};

export const getSendChatMessageMutationKey = () => [`/api/chat`] as const;

export function useSendChatMessage(options?: {
  mutation?: Parameters<typeof useMutation>[0];
  request?: SecondParameter<typeof customFetch>;
}) {
  const mutationKey = getSendChatMessageMutationKey();
  const { mutation: mutationOptions, request: requestOptions } = options ?? {};
  const mutationFn = (data: ChatRequest) => sendChatMessage(data, requestOptions);
  return useMutation({ ...mutationOptions, mutationKey, mutationFn });
}

// ---------------------------------------------------------------------------
// Create Booking
// ---------------------------------------------------------------------------

export const getCreateBookingUrl = () => `/api/bookings`;

export const createBooking = async (
  data: CreateBookingInput,
  options?: RequestInit,
): Promise<Booking> => {
  return customFetch<Booking>(getCreateBookingUrl(), {
    ...options,
    method: "POST",
    headers: { "Content-Type": "application/json", ...options?.headers },
    body: JSON.stringify(data),
  });
};

export const getCreateBookingMutationKey = () => [`/api/bookings`] as const;

export function useCreateBooking(options?: {
  mutation?: Parameters<typeof useMutation>[0];
  request?: SecondParameter<typeof customFetch>;
}) {
  const mutationKey = getCreateBookingMutationKey();
  const { mutation: mutationOptions, request: requestOptions } = options ?? {};
  const mutationFn = (data: CreateBookingInput) => createBooking(data, requestOptions);
  return useMutation({ ...mutationOptions, mutationKey, mutationFn });
}

// ---------------------------------------------------------------------------
// Get Booking
// ---------------------------------------------------------------------------

export const getBookingUrl = (id: string) => `/api/bookings/${id}`;

export const getBooking = async (
  id: string,
  options?: RequestInit,
): Promise<Booking> => {
  return customFetch<Booking>(getBookingUrl(id), { ...options, method: "GET" });
};

export const getGetBookingQueryKey = (id: string) => [`/api/bookings/${id}`] as const;

export function useGetBooking(
  id: string,
  options?: {
    query?: UseQueryOptions<Awaited<ReturnType<typeof getBooking>>, ErrorType<unknown>>;
    request?: SecondParameter<typeof customFetch>;
  },
) {
  const queryOptions = {
    queryKey: options?.query?.queryKey ?? getGetBookingQueryKey(id),
    queryFn: ({ signal }: { signal: AbortSignal }) => getBooking(id, { signal, ...options?.request }),
    enabled: !!id,
    ...options?.query,
  };
  return useQuery(queryOptions) as import("@tanstack/react-query").UseQueryResult<Awaited<ReturnType<typeof getBooking>>, ErrorType<unknown>> & { queryKey: import("@tanstack/react-query").QueryKey };
}

// ---------------------------------------------------------------------------
// Create Checkout Session (Stripe)
// ---------------------------------------------------------------------------

export const getCreateCheckoutSessionUrl = () => `/api/checkout-sessions`;

export const createCheckoutSession = async (
  data: CheckoutSessionInput,
  options?: RequestInit,
): Promise<CheckoutSession> => {
  return customFetch<CheckoutSession>(getCreateCheckoutSessionUrl(), {
    ...options,
    method: "POST",
    headers: { "Content-Type": "application/json", ...options?.headers },
    body: JSON.stringify(data),
  });
};

export const getCreateCheckoutSessionMutationKey = () => [`/api/checkout-sessions`] as const;

export function useCreateCheckoutSession(options?: {
  mutation?: Parameters<typeof useMutation>[0];
  request?: SecondParameter<typeof customFetch>;
}) {
  const mutationKey = getCreateCheckoutSessionMutationKey();
  const { mutation: mutationOptions, request: requestOptions } = options ?? {};
  const mutationFn = (data: CheckoutSessionInput) => createCheckoutSession(data, requestOptions);
  return useMutation({ ...mutationOptions, mutationKey, mutationFn });
}

// ---------------------------------------------------------------------------
// Capture Lead
// ---------------------------------------------------------------------------

export const getCaptureLeadUrl = () => `/api/leads`;

export const captureLead = async (
  data: CaptureLeadInput,
  options?: RequestInit,
): Promise<Lead> => {
  return customFetch<Lead>(getCaptureLeadUrl(), {
    ...options,
    method: "POST",
    headers: { "Content-Type": "application/json", ...options?.headers },
    body: JSON.stringify(data),
  });
};

export const getCaptureLeadMutationKey = () => [`/api/leads`] as const;

export function useCaptureLead(options?: {
  mutation?: Parameters<typeof useMutation>[0];
  request?: SecondParameter<typeof customFetch>;
}) {
  const mutationKey = getCaptureLeadMutationKey();
  const { mutation: mutationOptions, request: requestOptions } = options ?? {};
  const mutationFn = (data: CaptureLeadInput) => captureLead(data, requestOptions);
  return useMutation({ ...mutationOptions, mutationKey, mutationFn });
}
