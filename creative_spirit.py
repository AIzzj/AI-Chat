from emotion_analysis import EmotionAnalyzer
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 初始化情感分析模块
emotion_tokenizer = AutoTokenizer.from_pretrained("tae898/emoberta-large")
emotion_model = AutoModelForSequenceClassification.from_pretrained("tae898/emoberta-large").cuda()
emotion_analyzer = EmotionAnalyzer(emotion_model, emotion_tokenizer)

# 使用情感分析模块
emotion = emotion_analyzer.analyze("This is a test text.")
