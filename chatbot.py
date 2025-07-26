import json
import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Preprocess input
def tokenize_and_lemmatize(sentence):
    words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in words]

# Check for matching patterns
def get_response(user_input):
    user_words = tokenize_and_lemmatize(user_input)

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = tokenize_and_lemmatize(pattern)
            if set(pattern_words).intersection(user_words):
                return random.choice(intent["responses"])

    return "I'm not sure how to respond to that."

# Run chatbot
print("Chatbot is ready! Type 'quit' to stop.")
while True:
    message = input("You: ")
    if message.lower() == "quit":
        break
    response = get_response(message)
    print("Bot:", response)
