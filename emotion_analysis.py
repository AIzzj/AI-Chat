from transformers import AutoTokenizer, AutoModelForSequenceClassification

class EmotionAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("tae898/emoberta-large")
        self.model = AutoModelForSequenceClassification.from_pretrained("tae898/emoberta-large")

    def analyze(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        return self.model.config.id2label[outputs.logits.argmax().item()] 