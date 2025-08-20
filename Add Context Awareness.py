# Repository: python-chatbot
# New Feature: Add context awareness to responses

context = {}

def chatbot():
    """Simple rule-based chatbot with context awareness."""
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("You: ").lower()
        if "name" in user_input:
            context["name"] = user_input.split("is")[-1].strip()
            print(f"Chatbot: Nice to meet you, {context['name']}!")
        elif "weather" in user_input:
            location = context.get("location", "your area")
            print(f"Chatbot: The weather in {location} is sunny today.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand.")

# Example usage
chatbot()
