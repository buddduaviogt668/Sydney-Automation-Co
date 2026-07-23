
// SAC Diagnostic Chatbot
(function() {
    // 1. Inject Styles
    const style = document.createElement('style');
    style.innerHTML = `
        #sac-chat-widget {
            position: fixed;
            bottom: 24px;
            right: 24px;
            z-index: 9999;
            font-family: 'Barlow', sans-serif;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 16px;
        }
        #sac-chat-bubble {
            width: 60px;
            height: 60px;
            background: #f07020;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(240, 112, 32, 0.4);
            cursor: pointer;
            pointer-events: auto;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
        }
        #sac-chat-bubble:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 16px rgba(240, 112, 32, 0.6);
        }
        #sac-chat-bubble svg {
            width: 32px;
            height: 32px;
            fill: #fff;
        }
        .sac-chat-badge {
            position: absolute;
            top: -4px;
            right: -4px;
            background: #2ecc71;
            color: #fff;
            font-size: 11px;
            font-weight: bold;
            border-radius: 10px;
            padding: 2px 6px;
            border: 2px solid #0e1f3d;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-5px);}
            60% {transform: translateY(-3px);}
        }
        #sac-chat-window {
            width: 350px;
            max-width: calc(100vw - 48px);
            height: 500px;
            max-height: calc(100vh - 120px);
            background: #0d1e3c;
            border: 1px solid #2a4a80;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            pointer-events: auto;
            transform: translateY(20px);
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            visibility: hidden;
            overflow: hidden;
        }
        #sac-chat-window.open {
            transform: translateY(0);
            opacity: 1;
            visibility: visible;
        }
        #sac-chat-header {
            background: linear-gradient(135deg, #1e3a66 0%, #0d1e3c 100%);
            padding: 16px 20px;
            border-bottom: 1px solid #2a4a80;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .sac-chat-title {
            color: #fff;
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 20px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .sac-chat-status {
            width: 8px;
            height: 8px;
            background: #2ecc71;
            border-radius: 50%;
            display: inline-block;
        }
        .sac-chat-close {
            color: #a8c0e0;
            cursor: pointer;
            font-size: 24px;
            line-height: 1;
            transition: color 0.2s;
        }
        .sac-chat-close:hover {
            color: #f07020;
        }
        #sac-chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .sac-msg {
            max-width: 85%;
            padding: 12px 16px;
            border-radius: 12px;
            font-size: 14px;
            line-height: 1.5;
            animation: fadeIn 0.3s ease-out;
        }
        .sac-msg.bot {
            background: #1a3060;
            color: #f0f4ff;
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }
        .sac-msg.user {
            background: #f07020;
            color: #fff;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
        }
        .sac-options {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: -8px;
            animation: fadeIn 0.3s ease-out;
        }
        .sac-option-btn {
            background: rgba(255,255,255,0.05);
            border: 1px solid #2a4a80;
            color: #a8c0e0;
            padding: 10px 16px;
            border-radius: 8px;
            font-family: 'Barlow', sans-serif;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
        }
        .sac-option-btn:hover {
            background: rgba(240, 112, 32, 0.1);
            border-color: #f07020;
            color: #fff;
        }
        .sac-action-btn {
            background: #f07020;
            color: #fff !important;
            padding: 12px 20px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            text-decoration: none;
            display: block;
            margin-top: 10px;
            box-shadow: 0 4px 10px rgba(240, 112, 32, 0.3);
            transition: background 0.2s;
        }
        .sac-action-btn:hover {
            background: #ff8533;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Scrollbar styles for chat */
        #sac-chat-messages::-webkit-scrollbar {
            width: 6px;
        }
        #sac-chat-messages::-webkit-scrollbar-track {
            background: rgba(0,0,0,0.1);
        }
        #sac-chat-messages::-webkit-scrollbar-thumb {
            background: #2a4a80;
            border-radius: 3px;
        }
    `;
    document.head.appendChild(style);

    // 2. Create HTML Structure
    const container = document.createElement('div');
    container.id = 'sac-chat-widget';
    container.innerHTML = `
        <div id="sac-chat-window">
            <div id="sac-chat-header">
                <div class="sac-chat-title">
                    <span class="sac-chat-status"></span>
                    Diagnostic Assistant
                </div>
                <div class="sac-chat-close">&times;</div>
            </div>
            <div id="sac-chat-messages">
                <!-- Messages go here -->
            </div>
        </div>
        <div id="sac-chat-bubble">
            <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/><path d="M7 9h10v2H7zm0-3h10v2H7zm0 6h7v2H7z"/></svg>
            <div class="sac-chat-badge">1</div>
        </div>
    `;
    document.body.appendChild(container);

    // 3. Logic & State
    const chatWindow = document.getElementById('sac-chat-window');
    const chatBubble = document.getElementById('sac-chat-bubble');
    const closeBtn = document.querySelector('.sac-chat-close');
    const messagesContainer = document.getElementById('sac-chat-messages');
    const badge = document.querySelector('.sac-chat-badge');
    
    let chatOpen = false;
    let initialMessageSent = false;

    function toggleChat() {
        chatOpen = !chatOpen;
        if (chatOpen) {
            chatWindow.classList.add('open');
            badge.style.display = 'none'; // hide badge when opened
            if (!initialMessageSent) {
                startConversation();
                initialMessageSent = true;
            }
        } else {
            chatWindow.classList.remove('open');
        }
    }

    chatBubble.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    function addMessage(text, sender = 'bot', delay = 0) {
        return new Promise(resolve => {
            setTimeout(() => {
                const msg = document.createElement('div');
                msg.className = `sac-msg ${sender}`;
                msg.innerHTML = text;
                messagesContainer.appendChild(msg);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
                resolve();
            }, delay);
        });
    }

    function addOptions(options) {
        return new Promise(resolve => {
            setTimeout(() => {
                const optsContainer = document.createElement('div');
                optsContainer.className = 'sac-options';
                
                options.forEach(opt => {
                    const btn = document.createElement('button');
                    btn.className = 'sac-option-btn';
                    btn.textContent = opt.text;
                    btn.onclick = () => {
                        // Remove options
                        optsContainer.remove();
                        // Add user message
                        addMessage(opt.text, 'user').then(() => {
                            // Execute callback
                            opt.action();
                        });
                    };
                    optsContainer.appendChild(btn);
                });
                
                messagesContainer.appendChild(optsContainer);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
                resolve();
            }, 300);
        });
    }

    // 4. Conversation Flow
    async function startConversation() {
        await addMessage("Hi there! 👋 I'm the SAC diagnostic assistant.");
        await addMessage("Are you experiencing an issue with your automation system?", 'bot', 600);
        
        addOptions([
            { text: "Yes, I need help with C-Bus", action: handleCBus },
            { text: "Yes, I need help with Dynalite", action: handleDynalite },
            { text: "Just looking around", action: () => addMessage("No worries! Feel free to browse. If you need expert help, just click the 📞 Call Now button at the top.", 'bot', 500) }
        ]);
    }

    async function handleCBus() {
        await addMessage("I can help with C-Bus. What seems to be the main issue?", 'bot', 500);
        addOptions([
            { text: "Lights are stuck ON/OFF", action: () => suggestBooking("stuck lights") },
            { text: "Keypad buttons aren't responding", action: () => suggestBooking("unresponsive keypad") },
            { text: "System is completely dead", action: () => suggestBooking("dead system") }
        ]);
    }
    
    async function handleDynalite() {
        await addMessage("I can help with Dynalite. What seems to be the main issue?", 'bot', 500);
        addOptions([
            { text: "Antumbra keypad flashing", action: () => suggestBooking("flashing keypad") },
            { text: "Presets aren't working", action: () => suggestBooking("broken presets") },
            { text: "Network comms error", action: () => suggestBooking("network fault") }
        ]);
    }

    async function suggestBooking(issue) {
        await addMessage(`Ah, a ${issue}. That's a very common symptom of an underlying network or hardware fault.`, 'bot', 600);
        await addMessage("General electricians usually can't fix this without the official manufacturer software.", 'bot', 800);
        await addMessage("Our lead accredited specialist, George, can run a full diagnostic to isolate and repair this permanently.", 'bot', 1200);
        
        await new Promise(r => setTimeout(r, 600));
        
        const bookingMsg = document.createElement('div');
        bookingMsg.className = `sac-msg bot`;
        bookingMsg.innerHTML = `
            Let's get this sorted for you.
            <a href="/book-service.html" class="sac-action-btn">📅 View Availability & Book</a>
        `;
        messagesContainer.appendChild(bookingMsg);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
})();
