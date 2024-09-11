# Mistral LLM Fine-Tuned Chatbot

Bu proje, PDF dosyalarından metin çıkararak Mistral LLM modelini fine-tuning yapıp bir chatbot oluşturmayı amaçlamaktadır.

## Kurulum

Gerekli kütüphaneleri yüklemek için:

'''
pip install -r requirements.txt
'''

## Kullanım

1. PDF dosyalarını `data/pdf_files/` dizinine ekleyin.
2. Eğitim için `src/model_training.py` dosyasını çalıştırın.
3. Chatbot arayüzü için `src/chatbot_interface.py` dosyasını çalıştırın.
