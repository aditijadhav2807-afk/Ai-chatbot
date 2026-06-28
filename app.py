print("=" * 40)
print("🤖 Welcome to AI Chatbot")
print("=" * 40)

name = input("Enter your name: ")

print(f"\nHello {name}! I am your AI Chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")
    elif user == "how are you":
        print("Bot: I am doing great! Thanks for asking.")
    elif user == "your name":
        print("Bot: My name is AI Chatbot.")
    elif user == "help":
        print("Bot: You can ask me about my name or say hello.")
    elif user == "bye":
        print(f"Bot: Goodbye, {name}! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
