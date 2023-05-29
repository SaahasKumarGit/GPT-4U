import os
import random
import time
import openai

def list_md_files():
    return [f for f in os.listdir() if os.path.isfile(os.path.join( f)) and f != "README.md" and f.endswith('.txt')]

def change_chat(new_chat_name):
    with open(new_chat_name, 'r') as file:
        lines = file.readlines()
    
        # Strip newline characters from each line
        lines = [line.strip() for line in lines]
        
        # Group lines into question-answer pairs
        chat = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]
        return chat

def respond(message, chat_history, chatName):
        file = open(chatName, 'r')
        lines = file.read()
        file.close()

        with open(chatName, 'a') as fOpen:
            lines+=message
            fOpen.write(message + '\n')
            OpenAPIMessage = [{"role" : "system", "content": lines}]
            response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = OpenAPIMessage)

            bot_message = response["choices"][0]["message"]["content"]
            chat_history.append([message, bot_message])
            fOpen.write(bot_message + '\n')
        return "", chat_history
