import tkinter as tk
from tkinter import scrolledtext

# ==========================================
# 1. KNOWLEDGE BASE & INTENT MAPPING (O(1))
# ==========================================
# Requirement: Dictionary with 5+ intents (Page 17)
chatbot_responses = {
    "hello": "Hi there! Welcome to DecodeLabs. How can I help you today?",
    "hi": "Hello! I am your rule-based assistant. Ask me anything from my rules list.",
    "help": "Sure! You can ask me about 'project 1', 'guardrails', or 'ipo model'.",
    "project 1": "Project 1 focuses on building a deterministic rule-based chatbot interface using structured control flow.",
    "guardrails": "AI guardrails act as a deterministic filter for probabilistic LLM outputs, ensuring compliance and safety.",
    "ipo model": "The Input-Process-Output model provides a transparent blueprint: Sanitization -> Intent Matching -> Response Generation.",
    "bye": "Goodbye! Have a productive day engineering AI solutions!"
}

# Default Fallback response for unknown queries (Page 17)
FALLBACK_RESPONSE = "I'm sorry, I do not understand that command. Please type 'help' to see what I can do."

# ==========================================
# 2. CORE LOGIC ENGINE (IPO Model)
# ==========================================
def get_bot_response(raw_input_text):
    # Phase 1: Sanitization & Normalization (Page 10)
    clean_input = raw_input_text.lower().strip()
    
    # Check for exit strategy commands manually if needed, 
    # though in a GUI closing the window handles this cleanly.
    if clean_input in ["exit", "quit", "close"]:
        return "EXIT_SIGNAL"
        
    # Phase 2 & 3: Atomic Lookup + Fallback Processing (Page 15)
    reply = chatbot_responses.get(clean_input, FALLBACK_RESPONSE)
    return reply

# ==========================================
# 3. GRAPHICAL USER INTERFACE (GUI) LAYER
# ==========================================
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DecodeLabs - Rule-Based AI Engine v1.0")
        self.root.geometry("500x570")
        self.root.configure(bg="#1e222b")
        
        # Window Header
        header = tk.Label(root, text="DETERMINISTIC LOGIC ENGINE", font=("Courier", 14, "bold"), bg="#1e222b", fg="#4af626")
        header.pack(pady=10)
        
        # Chat History Window
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=55, height=22, font=("Arial", 10))
        self.chat_display.configure(bg="#282c34", fg="#ffffff", insertbackground="white")
        self.chat_display.pack(padx=15, pady=5)
        
        # User Input Box
        self.user_entry = tk.Entry(root, width=40, font=("Arial", 11), bg="#21252b", fg="#ffffff", insertbackground="white")
        self.user_entry.pack(side=tk.LEFT, padx=(15, 5), pady=15, ipady=5)
        self.user_entry.bind("<Return>", self.process_message) # Press enter to send
        
        # Send Button
        self.send_button = tk.Button(root, text="SEND", font=("Arial", 10, "bold"), bg="#4af626", fg="#1e222b", width=10, command=self.process_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 15), pady=15, ipady=3)
        
        # Welcome message in terminal display
        self.display_message("SYSTEM", "AI Skeletal Layer initiated. Type 'hello' or 'help' to begin.")

    def display_message(self, sender, text):
        self.chat_display.configure(state='normal')
        if sender == "You":
            self.chat_display.insert(tk.END, f"👤 {sender}: {text}\n\n")
        else:
            self.chat_display.insert(tk.END, f"🤖 {sender}: {text}\n\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

    def process_message(self, event=None):
        user_text = self.user_entry.get()
        if not user_text.strip():
            return
            
        # Display user input
        self.display_message("You", user_text)
        self.user_entry.delete(0, tk.END)
        
        # Get processed response
        bot_reply = get_bot_response(user_text)
        
        # Check for program exit command
        if bot_reply == "EXIT_SIGNAL":
            self.display_message("SYSTEM", "Terminating active digital loop...")
            self.root.after(1500, self.root.destroy)
            return

        # Display Bot reply
        self.display_message("Bot", bot_reply)

# Run the Interface Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()