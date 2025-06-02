import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1!"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing fine!", "I'm doing great. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it"]
    ],
    [
        r"what is your name ?",
        ["I'm a Python chatbot created by you!"]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye!"]
    ]
]

# Chatbot फ़ंक्शन
def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# चैटबॉट चलाएँ
chatbot()