import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"how are you", 
        ["I'm good, how about you?", "Doing well, thanks!"]
    ],
    [
        r"(.*) your name", 
        ["I'm a chatbot! You can call me ChatBot."]
    ],
    [
        r"what can you do", 
        ["I can chat with you, answer basic questions, and make your day better!"]
    ],
    [
        r"bye|goodbye", 
        ["Goodbye! Have a great day!", "See you later!"]
    ]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()
