### **Repository 8: Chatbot**
```python
# Repository: python-chatbot
# Description: A simple rule-based chatbot.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def chatbot():
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("You: ").lower()
        if "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "hola" in user_input:  # Spanish
            print("Chatbot: ¡Hola!")
        elif "bonjour" in user_input:  # French
            print("Chatbot: Bonjour!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand.")
# Example usage
chatbot()
