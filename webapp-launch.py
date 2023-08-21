import gradio as gr
import webapp_functions
import openai


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        with gr.Tab(label="Chat"):
            chat_selection = gr.Dropdown(choices= webapp_functions.list_md_files(),value = "Main Chat" , allow_custom_value=True, label="Chat Selection")
            chatbot = gr.Chatbot(value=webapp_functions.change_chat("Main Chat"))
            msg = gr.Textbox(label="Prompt")  
        with gr.Tab(label= "Settings"):
            modelSelection = gr.Dropdown(label="Model", choices= ["GPT 3.5 Turbo - 16k", "GPT 4"])
            apiKey = gr.Textbox(label="OpenAI API Key")
            temperature = gr.Slider(minimum=0, maximum=1, value=0.7, label="Temperature",step=0.1, interactive=True)
        with gr.Tab(label= "Analytics"):
            usageGraph = gr.LinePlot()
            analytics = gr.DataFrame()


    msg.submit(webapp_functions.respond, [msg, chatbot,chat_selection, modelSelection, apiKey, temperature], [msg, chatbot])
    chat_selection.change(fn = webapp_functions.change_chat, inputs = chat_selection, outputs=chatbot)

demo.launch(server_name="0.0.0.0")
