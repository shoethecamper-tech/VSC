import random

# Welcome message
print("Hello! I am a smarter chatbot. Type 'quit' to exit.")

# Memory for user's name
user_name = ""

# Predefined random responses
random_responses = [
    "That sounds interesting!",
    "Tell me more!",
    "Wow, really?",
    "I never thought of that.",
    "Cool!"
]

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Chatbot: Goodbye!")
        break

    # Remember user's name
    elif "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip().title()
        print(f"Chatbot: Nice to meet you, {user_name}!")

    # Greetings
    elif "hello" in user_input or "hi" in user_input:
        if user_name:
            print(f"Chatbot: Hi {user_name}! How are you?")
        else:
            print("Chatbot: Hi there! What's your name?")

    # Asking how chatbot is
    elif "how are you" in user_input:
        print("Chatbot: I'm just code, but I'm feeling awesome!")

    # Bye
    elif "bye" in user_input:
        print("Chatbot: See you later!")
    
    # Random responses for anything else
    else:
        print("Chatbot:", random.choice(random_responses))