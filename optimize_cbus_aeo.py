import os
import re

def optimize_cbus_aeo():
    """Inject FAQ schema and AEO optimization into C-Bus troubleshooting guides"""
    
    # FAQ Schema for Featured Snippets
    faq_schema = """
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "What causes C-Bus lights to get stuck on?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "C-Bus lights stuck on are typically caused by a faulty dimmer module, a programming error, or a network communication issue. The most common cause is a failing power supply that disrupts network communication."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Why is my C-Bus keypad flashing pink or red?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "A flashing pink or red indicator on your C-Bus keypad usually indicates a network burden issue or a failing power supply. This is a sign that your system needs immediate attention to prevent further damage."
          }}
        }},
        {{
          "@type": "Question",
          "name": "What is C-Bus network burden and how do I fix it?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Network burden occurs when too many devices are communicating on the C-Bus network simultaneously, causing delays and communication errors. Fix it by reducing network load, upgrading power supplies, or adding a network repeater."
          }}
        }},
        {{
          "@type": "Question",
          "name": "How do I know if my C-Bus power supply is failing?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Signs of a failing C-Bus power supply include flickering lights, unresponsive keypads, and indicators flashing on switches. If you notice these symptoms, have your power supply tested immediately."
          }}
        }},
        {{
          "@type": "Question",
          "name": "What are C-Bus ghost messages and why do my lights turn on randomly?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Ghost messages occur when faulty units send random commands on the C-Bus network, causing lights to turn on or off without user input. This can be caused by electrical interference, corrupted programming, or a faulty module."
          }}
        }}
      ]
    }}
    </script>
    """
    
    # AEO optimization: Inject direct answers and structured content
    aeo_optimization = """
    <div style="background: rgba(77,166,255,0.1); border: 1px solid rgba(77,166,255,0.3); padding: 20px; margin: 30px 0; border-radius: 8px;">
        <h3 style="color: #4da6ff; margin-top: 0;">Quick Answer</h3>
        <p style="margin: 0; color: #a8c0e0;">This guide provides step-by-step troubleshooting for C-Bus faults. If basic troubleshooting doesn't resolve your issue, contact Sydney Automation Co. for expert diagnosis and repair.</p>
    </div>
    """
    
    directory = "/home/ubuntu/Sydney-Automation-Co/blog"
    count = 0
    
    for filename in os.listdir(directory):
        # Target C-Bus troubleshooting guides only
        if filename.startswith("cbus-") and filename.endswith(".html"):
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Inject FAQ schema in head
                if faq_schema not in content and "</head>" in content:
                    head_end = content.find("</head>")
                    content = content[:head_end] + faq_schema + content[head_end:]
                
                # Inject AEO optimization after h2 Introduction
                if aeo_optimization not in content and "<h2>Introduction</h2>" in content:
                    intro_end = content.find("<h2>Introduction</h2>") + len("<h2>Introduction</h2>")
                    next_p_end = content.find("</p>", intro_end) + len("</p>")
                    content = content[:next_p_end] + aeo_optimization + content[next_p_end:]
                
                if content != original_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                pass
    
    print(f"✓ Optimized {count} C-Bus guides with FAQ schema and AEO triggers for Google Featured Snippets and AI search")

if __name__ == "__main__":
    optimize_cbus_aeo()
