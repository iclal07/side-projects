from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from data_preprocessing import prepare_dataset

def train_model(dataset):
    model_name = "mistralai/Mistral-7B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Verileri tokenize et
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Eğitim ayarları
    training_args = TrainingArguments(
        output_dir="../mistral_results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=2,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Eğitici tanımlama
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets,
    )

    # Eğitimi başlat
    trainer.train()

    # Eğitilen modeli kaydet
    model.save_pretrained("../mistral_fine_tuned_model")
    tokenizer.save_pretrained("../mistral_fine_tuned_model")

if __name__ == "__main__":
    from pdf_to_text import extract_texts_from_folder
    texts = extract_texts_from_folder("../data/pdf_files/")
    dataset = prepare_dataset(texts)
    train_model(dataset)
