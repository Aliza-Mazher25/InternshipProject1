"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - Batch 2026

A simple rule-based chatbot that responds to predefined user inputs
using a dictionary (hash map) lookup instead of an if-elif ladder.

Architecture: IPO Model
  INPUT   -> Sanitization & Normalization (lower + strip)
  PROCESS -> Intent Matching via dictionary .get()
  OUTPUT  -> Response Generation (with fallback for unknown input)
"""

# -----------------------------
# KNOWLEDGE BASE (5+ intents)
# -----------------------------
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "how are you": "I'm just a program, but I'm running smoothly! How about you?",
    "what is your name": "I'm RuleBot, a simple rule-based AI chatbot.",
    "what can you do": "I can chat using predefined rules. Try saying hello, asking my name, or saying bye!",
    "help": "You can try: hello, hi, how are you, what is your name, what can you do, thanks, bye.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome! Happy to help.",
}

# Exit commands that break the loop
EXIT_COMMANDS = {"bye", "exit", "quit"}

FALLBACK_RESPONSE = "I do not understand. Type 'help' to see what I can respond to."


def sanitize(raw_input: str) -> str:
    """Phase 1: Input & Sanitization - normalize case and strip whitespace."""
    return raw_input.lower().strip()


def get_response(clean_input: str) -> str:
    """Phase 2: Process - intent matching using dictionary lookup (.get())."""
    return responses.get(clean_input, FALLBACK_RESPONSE)


def run_chatbot():
    """Phase 3: The Heartbeat - continuous loop until exit/kill command."""
    print("RuleBot: Hello! I'm a rule-based chatbot. Type 'bye' to exit.")

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        # Exit strategy - clean break command
        if clean_input in EXIT_COMMANDS:
            print("RuleBot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)
        print(f"RuleBot: {reply}")


if __name__ == "__main__":
    run_chatbot()
