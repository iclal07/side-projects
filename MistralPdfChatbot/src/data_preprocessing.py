from datasets import Dataset

def prepare_dataset(texts):
    # Metinleri Hugging Face Dataset formatına dönüştür
    dataset = Dataset.from_dict({"text": texts})
    return dataset

if __name__ == "__main__":
    from pdf_to_text import extract_texts_from_folder
    texts = extract_texts_from_folder("../data/pdf_files/")
    dataset = prepare_dataset(texts)
    print(dataset)
