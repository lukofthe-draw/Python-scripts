# Define a list of responses
responses = [
    "Hello!",
    "How are you?",
    "I'm sorry, I didn't understand your input.",
    "I'm a chatbot!",
    "I like to chat with people."
]

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a message: ")
    # Check for specific keywords in the user input
    if "hello" in user_input.lower():
        print(responses[0])
    elif "how are you" in user_input.lower():
        print(responses[1])
    elif "chatbot" in user_input.lower():
        print(responses[3])
    else:
        print(responses[2])


##############
#variants
##############
import random

# Define a list of responses
responses = [
    "Hello!",
    "How are you?",
    "I'm sorry, I didn't understand your input.",
    "I'm a chatbot!",
    "I like to chat with people."
]

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a message: ")
    # Check for specific keywords in the user input
    if "hello" in user_input.lower():
        print(responses[0])
    elif "how are you" in user_input.lower():
        print(responses[1])
    elif "chatbot" in user_input.lower():
        print(responses[3])
    else:
        # Respond with a random response from the list
        print(random.choice(responses))


###
# Define a dictionary of responses
responses = {
    "hello": "Hello!",
    "how are you": "I'm doing well, thank you!",
    "chatbot": "Yes, I am a chatbot!",
    "default": "I'm sorry, I didn't understand your input."
}

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a message: "


##### model using the natural language toolkit library
import nltk

# Define a list of predefined responses
responses = [
    "Hello!",
    "How are you?",
    "I'm sorry, I didn't understand your input.",
    "I'm a chatbot!",
    "I like to chat with people."
]

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a message: ")
    # Tokenize the user input
    tokens = nltk.word_tokenize(user_input)
    # Extract the part of speech tags for each token
    pos_tags = nltk.pos_tag(tokens)
    # Check for specific keywords in the part of speech tags
    if any(tag[1] == "NNP" for tag in pos_tags):
        print(responses[0])
    elif any(tag[1] == "PRP" for tag in pos_tags):
        print(responses[1])
    else:
        # Respond with a random response from the list
        print(random.choice(responses))


####
#using chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot("My Chatbot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on a large dataset
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a message: ")
    # Generate a response from the chatbot
    response = chatbot.get_response(user
