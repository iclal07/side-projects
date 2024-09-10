import gradio as gr

# Initialize the conversation history
def chatbot_response(user_input, history):
    # Generate a simple response (replace this with your actual chatbot logic)
    response = "I'm sorry to hear that." if "neck pain" in user_input.lower() else "I'm good, you?"

    # Append user input and bot response to the history
    history.append((user_input, response))

    return history, ""

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>Chat with AI</h1>")

    # Create a component for displaying the chat history
    chatbox = gr.State([])  # Empty state to store chat history

    # Display the chat messages in a custom layout
    with gr.Column():
        chat_display = gr.HTML("<div id='chat-container' style='height: 300px; overflow-y: auto;'></div>")

    # Input field for the user to type messages
    with gr.Row():
        user_input = gr.Textbox(label="", placeholder="Type your message here...", show_label=False)
        send_button = gr.Button("Submit")

    # Update the chatbox when the button is clicked
    def update_chat(user_input, chatbox):
        chatbox, _ = chatbot_response(user_input, chatbox)
        # Create HTML formatted chat history
        chat_html = ""
        for user_msg, bot_msg in chatbox:
            chat_html += f"<div style='text-align: right;'><div style='display: inline-block; background-color: #CFC3FF; padding: 8px; border-radius: 8px; margin: 5px; color: black;'>{user_msg}</div></div>"
            chat_html += f"<div style='text-align: left;'><div style='display: inline-block; background-color: #FFFFFF; padding: 8px; border-radius: 8px; margin: 5px; color: black;'>{bot_msg}</div></div>"
        return chat_html, chatbox

    send_button.click(
        fn=update_chat,
        inputs=[user_input, chatbox],
        outputs=[chat_display, chatbox]
    )

    # Custom CSS for the layout
    demo.css = """
        #chat-container {
            font-family: 'Arial', sans-serif;
            background-color: #f0f0ff;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        .gradio-container .input_text {
            background-color: #e8e8ff;
        }
        .gradio-container .input_text textarea {
            color: #333;
            border: 2px solid #ddd;
            border-radius: 5px;
        }
        .gradio-container .button {
            background-color: #7f7fff;
            color: white;
            border-radius: 5px;
        }
    """

demo.launch()
