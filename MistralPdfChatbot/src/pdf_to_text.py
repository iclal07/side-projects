import pdfplumber
import os

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_texts_from_folder(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            text = pdf_to_text(file_path)
            texts.append(text)
    return texts

if __name__ == "__main__":
    folder_path = "../data/pdf_files/"
    all_texts = extract_texts_from_folder(folder_path)
    print(all_texts)
