import json
import random
import os.path
import datetime

# Load the Bible verses and accompanying paragraphs from a JSON file
with open('verse.json', 'r') as file:
    data = json.load(file)

# Create a function to generate a random verse and its accompanying paragraph based on the user's input
def generate_response(feeling):
    if feeling in data:
        verse = random.choice(data[feeling])
        return f"{verse['verse']}\n\n{verse['explanation']}"
    else:
        verse = random.choice(data['promises of God'])
        return f"{verse['verse']}\n\n{verse['explanation']}"


# Create a function to handle the user's input and generate a response based on the user's input
def chatbot_response(feeling):
    feeling = feeling.lower().strip()
    response = generate_response(feeling)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('chat_history.txt', 'a') as file:
        file.write(f"{timestamp} - User: {feeling}\n")
        file.write(f"{timestamp} - Chatbot: {response}\n\n")
    return response

# Create a function to store the chat history in a file
def store_chat_history():
    with open('chat_history.txt', 'r') as file:
        chat_history = file.read()
    return chat_history

# Create a function to handle the user's input and provide a default response if the input doesn't match any specific keyword or phrase
def handle_default_response(feeling):
    response = generate_response('promises of God')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('chat_history.txt', 'a') as file:
        file.write(f"{timestamp} - User: {feeling}\n")
        file.write(f"{timestamp} - Chatbot: {response}\n\n")
    return response

# Test the chatbot
while True:
    user_input = input("How are you feeling today? ")
    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'history':
        print(store_chat_history())
    elif user_input:
        response = chatbot_response(user_input)
        print(response)
    else:
        response = handle_default_response(user_input)
        print(response)
