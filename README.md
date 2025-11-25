# Task-8-python
# Simple Rule-Based Chatbot using Python

This project is a very simple chatbot built using **if-elif-else**
statements in Python.

## 🔥 Features

-   Responds to basic greetings
-   Provides simple rule-based replies
-   Loops until the user enters `bye`
-   Demonstrates basic NLP idea using keyword matching

## 📌 Code Used

``` python
print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

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
```

## 🚀 How to Run

1.  Save the code in a file named `chatbot.py`
2.  Open terminal and run:

```{=html}
<!-- -->
```
    python chatbot.py

## 🎯 Outcome

You will understand: - Basic NLP structure - Rule-based
decision-making - Interactive console programs in Python
