import gradio as gr
import webapp_functions
import openai

chat = [["This is you!", "This is the assistant!"]]
conversations = webapp_functions.list_md_files()

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        with gr.Accordion(label= "Settings", open= False):
            with gr.Row():
                with gr.Column(scale = 1):
                    modelSelection = gr.Dropdown(label="Model", choices= ["GPT 3.5 Turbo", "GPT 4"])
                with gr.Column(scale = 1):
                    apiKey = gr.Textbox(label="OpenAI API Key")
        with gr.Accordion(label= "Analytics", open= False):
            analytics = gr.Gallery()
    chat_selection = gr.Dropdown(choices= conversations, allow_custom_value=True, label="Chat Selection")
    chatbot = gr.Chatbot(value=chat)
    msg = gr.Textbox(label="Prompt") 

    msg.submit(webapp_functions.respond, [msg, chatbot,chat_selection, modelSelection, apiKey], [msg, chatbot])
    chat_selection.change(fn = webapp_functions.change_chat, inputs = chat_selection, outputs=chatbot)

demo.launch(server_name="0.0.0.0")
