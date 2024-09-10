import gradio as gr

# Initialize the conversation history
def chatbot_response(user_input, history):
    # Generate a simple response (replace this with your actual chatbot logic)
    response = "I'm sorry to hear that." if "neck pain" in user_input.lower() else "I'm good, you?"

    # Append user input and bot response to the history
    history.append(("You", user_input))
    history.append(("Bot", response))

    # Generate the HTML content to show messages in bubbles with the desired style
    chat_html = ""
    for user, message in history:
        if user == "You":
            # User messages in purple bubble
            chat_html += f"<div style='text-align: right; margin: 10px;'><div style='display: inline-block; background-color: #CFC3FF; color: black; padding: 10px; border-radius: 10px; max-width: 60%; word-wrap: break-word;'>{message}</div></div>"
        else:
            # Bot messages in white bubble
            chat_html += f"<div style='text-align: left; margin: 10px;'><div style='display: inline-block; background-color: #FFFFFF; color: black; padding: 10px; border-radius: 10px; max-width: 60%; word-wrap: break-word;'>{message}</div></div>"
    
    return chat_html, history

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>Chat with AI</h1>")

    # Chat history state
    chatbox = gr.State([])

    # Chat container with a thicker purple border and wider layout
    with gr.Column(elem_id="chat-container", scale=1, min_width=600):
        chat_display = gr.HTML("<div id='chat-content' style='height: 400px; background-color: white; border: 4px solid #CFC3FF; padding: 10px; border-radius: 10px; overflow-y: auto;'></div>")

    # Input and buttons at the bottom in a row
    with gr.Row():
        user_input = gr.Textbox(label="", placeholder="Type your message here...", show_label=False, lines=1)
    
    with gr.Row():
        send_button = gr.Button("Submit")
        clear_button = gr.Button("Clear")

    # Function to update the chat
    def update_chat(user_input, chatbox):
        chat_html, updated_history = chatbot_response(user_input, chatbox)
        return chat_html, updated_history, ""

    # Function to clear the chat
    def clear_chat():
        return "", []

    send_button.click(
        fn=update_chat,
        inputs=[user_input, chatbox],
        outputs=[chat_display, chatbox, user_input]
    )

    clear_button.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chat_display, chatbox]
    )

    # Custom CSS for consistent design
    demo.css = """
        #chat-container {
            font-family: 'Arial', sans-serif;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            height: 400px;
            overflow-y: auto;
            border: 4px solid #CFC3FF;
            margin-bottom: 10px;
            width: 600px;  /* Adjusted width for wider chat area */
        }
        .gradio-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .gradio-container .input_text {
            width: 100%;
            padding: 5px;
        }
        .gradio-container .button {
            background-color: #7f7fff;
            color: white;
            border-radius: 5px;
            padding: 8px 20px;
            margin: 0 5px;
        }
    """

demo.launch()
