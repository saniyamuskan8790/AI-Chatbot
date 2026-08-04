def show_welcome():
    print("Welcome to AI ChatBot!")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

def get_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I am fine. Thank you!",
        "what is your name": "I am an AI ChatBot.",
        "who created you": "I was created using Python.",
        "python": "Python is a popular programming language.",
        "thank you": "You're welcome!",
    }

    return responses.get(user_input.lower(),
                         "Sorry, I don't understand that.")

def chatbot():
    show_welcome()

    while True:
        user = input("You: ").lower()

        if user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        print("Bot:", get_response(user))


chatbot()