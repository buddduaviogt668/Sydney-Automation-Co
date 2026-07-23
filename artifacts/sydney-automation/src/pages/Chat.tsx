import { useState, useRef, useEffect } from "react";
import { Link } from "wouter";
import { Send, Loader2, ArrowLeft } from "lucide-react";
import { useSendChatMessage } from "@workspace/api-client-react";
import type { ChatMessage, ChatResponse } from "@workspace/api-client-react";

export default function Chat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatMutation = useSendChatMessage();

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim() || chatMutation.isPending) return;

    const userMessage: ChatMessage = { role: "user", content: input.trim() };
    const updatedMessages = [...messages, userMessage];
    setMessages(updatedMessages);
    setInput("");

    chatMutation.mutate(
      { messages: updatedMessages },
      {
        onSuccess: (data: ChatResponse) => {
          setMessages((prev) => [...prev, { role: "assistant", content: data.message }]);
        },
        onError: () => {
          setMessages((prev) => [
            ...prev,
            { role: "assistant", content: "Something went wrong. Please try again or call George on 0422 469 739." },
          ]);
        },
      },
    );
  };

  return (
    <div className="flex h-[calc(100vh-57px)] flex-col">
      <div className="flex items-center gap-3 border-b border-gray-200 bg-white px-4 py-3">
        <Link href="/" className="text-gray-400 hover:text-gray-600">
          <ArrowLeft className="h-5 w-5" />
        </Link>
        <div>
          <h1 className="text-sm font-semibold text-gray-900">AI Chat</h1>
          <p className="text-xs text-gray-500">Ask about C-Bus, Dynalite, or any lighting issue</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto bg-gray-50 px-4 py-6">
        <div className="mx-auto max-w-2xl">
          {messages.length === 0 && (
            <div className="text-center">
              <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-amber-100">
                <span className="text-2xl">💡</span>
              </div>
              <h2 className="mb-2 text-lg font-semibold text-gray-900">Lighting Automation Expert</h2>
              <p className="mb-6 text-sm text-gray-500">
                Ask George's AI anything about C-Bus, Dynalite, DALI, or lighting automation faults.
              </p>
              <div className="flex flex-wrap justify-center gap-2">
                {[
                  "My C-Bus is unresponsive",
                  "Dynalite LED blinking codes",
                  "DALI driver fault",
                  "How much does a callout cost?",
                ].map((q) => (
                  <button
                    key={q}
                    onClick={() => {
                      setInput(q);
                    }}
                    className="rounded-full border border-gray-200 bg-white px-4 py-2 text-sm text-gray-600 transition-colors hover:border-amber-300 hover:text-amber-600"
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((msg, i) => (
            <div key={i} className={`mb-4 flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
              <div
                className={`max-w-[80%] rounded-xl px-4 py-3 text-sm leading-relaxed ${
                  msg.role === "user"
                    ? "bg-amber-600 text-white"
                    : "bg-white text-gray-900 shadow-sm border border-gray-200"
                }`}
              >
                {msg.content}
              </div>
            </div>
          ))}

          {chatMutation.isPending && (
            <div className="mb-4 flex justify-start">
              <div className="flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm text-gray-500 shadow-sm">
                <Loader2 className="h-4 w-4 animate-spin" />
                George's AI is thinking...
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className="border-t border-gray-200 bg-white px-4 py-4">
        <div className="mx-auto flex max-w-2xl gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Describe your lighting issue..."
            className="flex-1 rounded-lg border border-gray-300 px-4 py-3 text-sm focus:border-amber-500 focus:outline-none"
            disabled={chatMutation.isPending}
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || chatMutation.isPending}
            className="rounded-lg bg-amber-600 px-4 py-3 text-white transition-colors hover:bg-amber-700 disabled:opacity-50"
          >
            <Send className="h-4 w-4" />
          </button>
        </div>
        <div className="mx-auto mt-3 max-w-2xl text-center">
          <Link href="/book" className="text-sm font-medium text-amber-600 hover:underline">
            Book a service call — $200+GST deposit
          </Link>
        </div>
      </div>
    </div>
  );
}
