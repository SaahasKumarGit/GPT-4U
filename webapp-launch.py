import gradio as gr
import random
import time
import os


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

def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

chat = [["hi!", "hey"]]
conversations = list_md_files()

with gr.Blocks() as demo:
    chat_selection = gr.Dropdown(choices= conversations)
    chatbot = gr.Chatbot(value=chat)
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    chat_selection.change(fn = change_chat, inputs = chat_selection, outputs=chatbot)

demo.launch()
