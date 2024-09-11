import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Fine-tuned model ve tokenizer yükleniyor
model_name = "../mistral_fine_tuned_model"  # Fine-tuned modelin kaydedildiği yol
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Modelden yanıt üretmek için fonksiyon
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Kullanıcı girdisi ve sohbet geçmişine göre yanıt dönen fonksiyon
def chatbot_response(user_input, history):
    # Modeli kullanarak yanıt üret
    response = generate_response(user_input)
    
    # Kullanıcı girdisini ve model yanıtını geçmişe ekle
    history.append(("You", user_input))
    history.append(("Bot", response))

    # Mesajları istenen stilde balonlar halinde gösterecek HTML içeriği oluştur
    chat_html = ""
    for user, message in history:
        if user == "You":
            # Kullanıcı mesajları mor balonda
            chat_html += f"<div style='text-align: right; margin: 10px;'><div style='display: inline-block; background-color: #CFC3FF; color: black; padding: 10px; border-radius: 10px; max-width: 60%; word-wrap: break-word;'>{message}</div></div>"
        else:
            # Bot mesajları beyaz balonda
            chat_html += f"<div style='text-align: left; margin: 10px;'><div style='display: inline-block; background-color: #FFFFFF; color: black; padding: 10px; border-radius: 10px; max-width: 60%; word-wrap: break-word;'>{message}</div></div>"
    
    return chat_html, history

# Gradio arayüzü oluşturma
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>Chat with AI</h1>")

    # Sohbet geçmişi durumu
    chatbox = gr.State([])

    # Sohbet kutusu daha kalın mor sınır ve geniş düzenle
    with gr.Column(elem_id="chat-container", scale=1, min_width=600):
        chat_display = gr.HTML("<div id='chat-content' style='height: 400px; background-color: white; border: 4px solid #CFC3FF; padding: 10px; border-radius: 10px; overflow-y: auto;'></div>")

    # Giriş ve düğmeleri alt sırada
    with gr.Row():
        user_input = gr.Textbox(label="", placeholder="Type your message here...", show_label=False, lines=1)
    
    with gr.Row():
        send_button = gr.Button("Submit")
        clear_button = gr.Button("Clear")

    # Sohbeti güncellemek için fonksiyon
    def update_chat(user_input, chatbox):
        chat_html, updated_history = chatbot_response(user_input, chatbox)
        return chat_html, updated_history, ""

    # Sohbeti temizlemek için fonksiyon
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

    # Tutarlı tasarım için özel CSS
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
            width: 600px;  /* Daha geniş sohbet alanı için ayarlanmış genişlik */
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
