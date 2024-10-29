from transformers import AutoTokenizer, AutoModelForCausalLM

class ChatAssistant:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

    def generate_response(self, message: str) -> str:
        inputs = self.tokenizer(message, return_tensors="pt")
        inputs = inputs.to(self.model.device)
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True) 