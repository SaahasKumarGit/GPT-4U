import gradio as gr
import random
import time

conversations = ["Morning", "Evening"]

chat = [["Hi!", "Hey"]]

def change_chat(new_chat_name):
      chat = [[new_chat_name, "good"]]
      return chat

def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

with gr.Blocks() as demo:
    chat_selection = gr.Dropdown(choices= conversations)
    chatbot = gr.Chatbot(value=chat)
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    chat_selection.change(fn = change_chat, inputs = chat_selection, outputs=chatbot)

demo.launch()
