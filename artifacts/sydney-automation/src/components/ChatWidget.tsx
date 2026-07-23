import { useState, useRef, useEffect } from "react";
import { MessageCircle, X, Send, Loader2 } from "lucide-react";
import { useSendChatMessage } from "@workspace/api-client-react";
import type { ChatMessage, ChatResponse } from "@workspace/api-client-react";

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
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
            { role: "assistant", content: "Sorry, something went wrong. Call George on 0422 469 739." },
          ]);
        },
      },
    );
  };

  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 right-6 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-amber-600 text-white shadow-lg transition-transform hover:scale-110"
        aria-label="Open AI Chat"
      >
        <MessageCircle className="h-6 w-6" />
      </button>
    );
  }

  return (
    <div className="fixed bottom-6 right-6 z-50 flex w-[360px] flex-col rounded-xl border border-gray-200 bg-white shadow-2xl" style={{ maxHeight: "500px" }}>
      <div className="flex items-center justify-between rounded-t-xl bg-amber-600 px-4 py-3">
        <div>
          <h3 className="text-sm font-semibold text-white">Chat with George's AI</h3>
          <p className="text-xs text-amber-100">Lighting automation expert</p>
        </div>
        <button onClick={() => setIsOpen(false)} className="text-white hover:text-amber-100" aria-label="Close chat">
          <X className="h-5 w-5" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-4" style={{ minHeight: "280px", maxHeight: "340px" }}>
        {messages.length === 0 && (
          <div className="text-center text-sm text-gray-500">
            <p className="mb-2">Ask about C-Bus, Dynalite, or any lighting automation issue.</p>
            <p className="text-xs text-gray-400">George's AI assistant is here to help.</p>
          </div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`mb-3 flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-[80%] rounded-lg px-3 py-2 text-sm ${
                msg.role === "user"
                  ? "bg-amber-600 text-white"
                  : "bg-gray-100 text-gray-900"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        {chatMutation.isPending && (
          <div className="flex justify-start">
            <div className="flex items-center gap-1 rounded-lg bg-gray-100 px-3 py-2 text-sm text-gray-500">
              <Loader2 className="h-3 w-3 animate-spin" />
              Thinking...
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="border-t border-gray-200 p-3">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Describe your issue..."
            className="flex-1 rounded-lg border border-gray-300 px-3 py-2 text-sm focus:border-amber-500 focus:outline-none"
            disabled={chatMutation.isPending}
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || chatMutation.isPending}
            className="rounded-lg bg-amber-600 px-3 py-2 text-white transition-colors hover:bg-amber-700 disabled:opacity-50"
          >
            <Send className="h-4 w-4" />
          </button>
        </div>
        <div className="mt-2 text-center">
          <a href="/book" className="text-xs font-medium text-amber-600 hover:underline">
            Book a service call — $200 deposit
          </a>
        </div>
      </div>
    </div>
  );
}
