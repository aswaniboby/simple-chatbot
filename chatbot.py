def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I'm doing great! Thanks for asking.",
        "what is your name": "I'm a simple chatbot created using Python.",
        "bye": "Goodbye! Have a nice day!",
        "help": "You can greet me, ask my name, or have a simple conversation."
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I don't understand that yet."