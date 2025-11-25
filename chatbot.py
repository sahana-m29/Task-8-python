# Simple Rule-Based Chatbot using if-else

print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()   # convert to lowercase for easy matching

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Chatbot: I'm just a program, but I'm working great!")

    elif user == "your name":
        print("Chatbot: I am a simple rule-based chatbot created using Python.")

    elif user == "what can you do":
        print("Chatbot: I can reply to simple messages using if-else rules!")

    elif "weather" in user:
        print("Chatbot: I can't check the weather yet, but I hope it's nice outside!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
