import gradio as gr
import PrivateAPIKey
import webapp_functions
import openai

chat = [["hi!", "hey"]]
conversations = webapp_functions.list_md_files()
openai.api_key = PrivateAPIKey.OpenaiAPIKey

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    chat_selection = gr.Dropdown(choices= conversations)
    chatbot = gr.Chatbot(value=chat)
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(webapp_functions.respond, [msg, chatbot,chat_selection], [msg, chatbot])
    chat_selection.change(fn = webapp_functions.change_chat, inputs = chat_selection, outputs=chatbot)

demo.launch(server_name="0.0.0.0")
