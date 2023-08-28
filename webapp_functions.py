import os
import random
import time
import openai
import json

# Code to list all files with the extension .txt.
# Used for gradio to list all conversations from conversation dropdown.
# Returns an array with each entry being the filename including the .txt extension
def list_md_files():
    
    #Finds all chats that end with the extension .chat
    conversations = [filename for filename in os.listdir() if filename != "README.md" and filename.endswith('.chat')]
    
    # Strips the .chat extension from each file
    for i in range (len(conversations)):
        conversations[i] = conversations[i][:-5]

    return conversations

# Returns a list containing question-answer pairs of the chat 
# to the chatbot, so it can render it.
# If the file is not found, it creates a new file.
# DO NOT INCLUDE THE .chat EXTENSION!!!
# The file will not be created here, if the file does not exist, it will
# create it later when responding
def change_chat(new_chat_name):

    # Opens the chat
    try:    
        new_chat_name += ".chat"
        file = open(new_chat_name, 'r+')
        file.seek(0)

        #Turns the .chat file into an array of prompts/responses
        messages = file.read().split("---endresponse---")
        
        #Turns the array into an array of question-answer pairs
        pair_list = []
        for i in range(0, len(messages)-1, 2):
            pair_list.append([messages[i], messages[i+1]])
        print(pair_list)

        file.close()
        
        return pair_list
    
    # If the file does not exist, return an empty chat
    except FileNotFoundError as error:
        return []
    

# Given the setings, uses the openai api to generate a bot response
# If the chatName does not exist, it is created
def respond(message, chat_history, chatName, modelSelection, apiKey, temperature):

        # Reads the conversation
        chatName += ".chat"
        file = open(chatName, 'a+')
        file.seek(0)
        lines = file.read()
        lines = lines.replace("---endresponse---", "")
        
        # Sets up the prompt
        openai.api_key = apiKey
        lines+=message
        OpenAPIMessage = [{"role" : "system", "content": lines}]

        # Generates the response using the openai api
        # if the key is invalid, 
        response = ""
        try:
            if(modelSelection == "GPT 4"): 
                response = openai.ChatCompletion.create(model = "gpt-4", messages = OpenAPIMessage, temperature = temperature) ["choices"][0]["message"]["content"]
            else:
                response = openai.ChatCompletion.create(model = "gpt-3.5-turbo-16k", messages = OpenAPIMessage, temperature = temperature) ["choices"][0]["message"]["content"]
        except openai.error.AuthenticationError:
                response = "Invalid OpenAI API key."

        # Appends the prompt/response to the chat_history to the file
        # and appends it to chat history to be rendered by chatbot
        chat_history.append([message, response])
        file.write(message + "---endresponse---\n")
        file.write(response + "---endresponse---\n")
        
        file.close()
        return "", chat_history