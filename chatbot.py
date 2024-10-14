import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name?', ['I am a chatbot, and what is your name', 'My name is Chatbot, and what is your name']],
    ['my name is (.*)', ['heyhi %1. wassup']],
    ['good|pretty good|cool', ['Feeling ready to chat!']],
    ['how are you?', ['I am very well, thankyou!', 'I am just a bot, but I am doing great!']],
    ['what is chatbot?', ['chatbot is python program to help you']],
    ['I need your help|can you help me', ['how can I help you']],
    ['what is python?', ['Python is a simple, versatile programming language known for its simplicity and readability, used in web development, automation, data analysis and machine learning']],
    ['what is java?', ['Java is object oriented programming language']],
    ['who create you?|who is your creator?|who creates you?', ['I was created by Open AI, using advanced machine learning techniques and natural language processing']],
    ['are you robot', ['Yes I am a robot']],
    ['bye', ['Goodbye!', 'Have a great day!']],
]

reflections = {
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    'i\'d': 'you would',
    'i\'ve': 'you have',
    'i\'ll': 'you will',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was',
    'you\'ve': 'I have',
    'you\'ll': 'I will',
    'your': 'my',
    'yours': 'mine',
    'me': 'you',
}

chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hi! I am a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    start_chat()
    