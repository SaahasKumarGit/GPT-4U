import os
import random
import time
import openai

def list_md_files():
    return [f for f in os.listdir() if os.path.isfile(os.path.join( f)) and f != "README.md" and f.endswith('.txt')]

def change_chat(new_chat_name):
    try:
        file = open(new_chat_name, 'r')
        lines = file.readlines()
    
        # Strip newline characters from each line
        lines = [line.strip() for line in lines]
        
        # Group lines into question-answer pairs
        chat = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]
        
        return chat
    except FileNotFoundError:
        file = open(new_chat_name, 'w+')
        chat = []
        return chat

def respond(message, chat_history, chatName, modelSelection, apiKey):
        lines = ""
        if(chatName == ""):
            chatName = "DefaultChat.txt"
            lines = ""
            chat = []
        else:
            file = open(chatName, 'r')
            lines = file.read()
            file.close()
        
        openai.api_key = apiKey


        with open(chatName, 'a') as fOpen:
            lines+=message
            OpenAPIMessage = [{"role" : "system", "content": lines}]
            try:
                response = ""
                if(modelSelection == "GPT 4"): 
                    response = openai.ChatCompletion.create(model = "gpt-4", messages = OpenAPIMessage)
                else:
                    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = OpenAPIMessage)
            except openai.error.AuthenticationError:
                bot_message = "Invalid OpenAI API key."
                print("Invalid OpenAI API key.")
                chat_history.append([message, bot_message])
                return "", chat_history
            bot_message = response["choices"][0]["message"]["content"]
            chat_history.append([message, bot_message])
            fOpen.write(message + '\n')
            fOpen.write(bot_message + '\n')
        return "", chat_history

def setAPIKey(apikey):
    openai.api_key = apikey