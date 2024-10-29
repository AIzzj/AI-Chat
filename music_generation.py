class MusicGenerator:
    def __init__(self, model):
        self.model = model

    def generate(self, description: str, duration: int):
        # 使用模型生成音乐
        music = self.model.generate(description, duration)
        return music 