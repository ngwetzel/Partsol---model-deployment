from transformers import pipeline

# Load the Hugging Face model and tokenizer
model_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
