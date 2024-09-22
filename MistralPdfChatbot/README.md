# Mistral LLM Fine-Tuned Chatbot

Bu proje, PDF dosyalarından metin çıkararak Mistral LLM modelini fine-tuning yapıp, kullanıcının girdilerine yanıt verebilen bir chatbot oluşturmayı amaçlamaktadır. Proje, Gradio tabanlı bir arayüz kullanarak etkileşimli bir sohbet deneyimi sunar.

## İçindekiler

- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Klasör Yapısı](#klasör-yapısı)
- [Proje Dosyalarının Açıklamaları](#proje-dosyalarının-açıklamaları)
- [Projenin Çalıştırılması](#projenin-çalıştırılması)
  - [1. Gereksinimleri Kurun](#1-gereksinimleri-kurun)
  - [2. PDF Dosyalarını Hazırlayın](#2-pdf-dosyalarını-hazırlayın)
  - [3. PDF Metinlerini Çıkarın ve İşleyin](#3-pdf-metinlerini-çıkarın-ve-işleyin)
  - [4. Chatbot Arayüzünü Başlatın](#4-chatbot-arayüzünü-başlatın)
  - [5. Chatbot ile Etkileşim Kurun](#5-chatbot-ile-etkileşim-kurun)
- [Modülerlik ve Genişletilebilirlik](#modülerlik-ve-genişletilebilirlik)

## Gereksinimler

Projenin çalışabilmesi için aşağıdaki Python kütüphanelerinin kurulması gerekmektedir:

- `transformers`
- `datasets`
- `torch`
- `pdfplumber`
- `gradio`

## Kurulum

Gerekli Python kütüphanelerini yüklemek için, terminal veya komut satırında aşağıdaki komutu çalıştırın:

```
pip install -r requirements.txt
```

## Klasör Yapısı
Projenin dizin yapısı şu şekildedir:

```
mistral_chatbot_project/
│
├── data/
│   └── pdf_files/           # Eğitilecek PDF dosyalarının olduğu dizin
│
├── src/
│   ├── __init__.py          # Python package tanımlama dosyası
│   ├── pdf_to_text.py       # PDF dosyalarını metne çeviren kodlar
│   ├── data_preprocessing.py# Metin verisini işleme ve hazırlama kodları
│   ├── model_training.py    # Modelin eğitim ve fine-tuning kodları
│   └── chatbot_interface.py # Chatbot arayüzü kodları
│
├── requirements.txt         # Gerekli Python paketlerinin listesi
└── README.md                # Proje hakkında bilgi
```

## Proje Dosyalarının Açıklamaları
data/pdf_files/: Eğitim için kullanılacak PDF dosyalarının bulunduğu dizin.
src/__init__.py: Python paket yapısı tanımlama dosyası.
src/pdf_to_text.py: PDF dosyalarını metne çeviren modül.
src/data_preprocessing.py: Çıkarılan metinleri işleyen ve eğitim için hazırlayan modül.
src/model_training.py: Eğitimi ve fine-tuning işlemini gerçekleştiren modül.
src/chatbot_interface.py: Gradio tabanlı chatbot arayüzünü sağlayan modül.
requirements.txt: Proje için gerekli Python kütüphanelerini listeleyen dosya.
README.md: Proje hakkında bilgi ve kullanım talimatlarını içeren dosya.
Projenin Çalıştırılması
Projenin çalıştırılması için aşağıdaki adımları takip edin:

### 1. Gereksinimleri Kurun
Proje dizininde terminal veya komut satırında aşağıdaki komutu çalıştırarak gerekli bağımlılıkları yükleyin:

```
pip install -r requirements.txt
```

### 2. PDF Dosyalarını Hazırlayın
Eğitmek istediğiniz PDF dosyalarını data/pdf_files/ dizinine yerleştirin.

### 3. PDF Metinlerini Çıkarın ve İşleyin
PDF dosyalarından metin çıkarmak ve veriyi hazırlamak için model_training.py dosyasını çalıştırın:

```
python src/model_training.py
```

Bu dosya, PDF dosyalarını okur, metni çıkarır, veriyi işler ve Mistral LLM modelini fine-tuning yaparak eğitir. Eğitilen model mistral_fine_tuned_model dizinine kaydedilir.

### 4. Chatbot Arayüzünü Başlatın
Model eğitimi tamamlandıktan sonra, chatbot arayüzünü başlatmak için aşağıdaki komutu çalıştırın:

```
python src/chatbot_interface.py
```
Bu komut, Gradio arayüzünü başlatır ve web tarayıcınızda etkileşimli bir chatbot açılır.

### 5. Chatbot ile Etkileşim Kurun
Gradio arayüzü açıldıktan sonra, kullanıcı mesajlarını yazabileceğiniz bir metin kutusu ve gönder butonu göreceksiniz. Mesajınızı yazın ve "Submit" butonuna tıklayın. Model, mesajınıza uygun bir yanıt oluşturacak ve yanıtı sohbet geçmişine ekleyecektir.

## Modülerlik ve Genişletilebilirlik
Bu proje modüler yapısıyla kolayca genişletilebilir ve özelleştirilebilir. Yeni PDF dosyaları ekleyip modeli yeniden eğitebilir veya chatbot arayüzünü değiştirerek kullanıcı deneyimini geliştirebilirsiniz.
