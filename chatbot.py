### **Repository 8: Chatbot**
```python
# Repository: python-chatbot
# Description: A simple rule-based chatbot.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def chatbot():
    print("Chatbot: Hello! How can I assist you?")
    corpus = ["hello", "how are you", "goodbye"]
    vectorizer = TfidfVectorizer().fit(corpus)
    while True:
        user_input = input("You: ").lower()
        vec = vectorizer.transform([user_input])
        similarities = cosine_similarity(vec, vectorizer.transform(corpus))
        best_match = corpus[similarities.argmax()]
        if best_match == "hello":
            print("Chatbot: Hi there!")
        elif best_match == "goodbye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand.")
# Example usage
chatbot()
