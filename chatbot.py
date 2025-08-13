### **Repository 8: Chatbot**
```python
# Repository: python-chatbot
# Description: A simple rule-based chatbot.

def chatbot():
    """Simple rule-based chatbot."""
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("You: ").lower()
        if "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand.")

# Example usage
chatbot()
