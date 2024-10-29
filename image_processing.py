class ImageProcessor:
    def __init__(self, model):
        self.model = model

    def process(self, image_path: str):
        # 图像处理逻辑
        processed_image = self.model.process(image_path)
        return processed_image 