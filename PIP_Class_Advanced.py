from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import os
import json
import numpy as np

class PIPClassAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        current_dir = os.path.dirname(__file__)
        models_dir = os.path.join(current_dir, "models")
        model_options = [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]

        return {
            "required": {
                "image": ("IMAGE", {}),
            },
            "optional": {
                "model_path": (model_options, {"default": model_options[0] if model_options else ""})
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("分类标签", "分类详情")
    CATEGORY = "PIP 图像分类高级版"
    FUNCTION = "classify_image"

    def __init__(self, model_path="PIP_ClassV1"):
        current_dir = os.path.dirname(__file__)
        models_dir = os.path.join(current_dir, "models")
        full_model_path = os.path.join(models_dir, model_path)

        print(f"Loading model from: {full_model_path}")

        self.model = ViTForImageClassification.from_pretrained(full_model_path)
        self.processor = ViTImageProcessor.from_pretrained(full_model_path)

        # 从config.json读取id2label
        config_path = os.path.join(full_model_path, "config.json")
        with open(config_path, 'r') as f:
            config = json.load(f)
            self.model.config.id2label = config.get("id2label", {})

    def preprocess_image(self, image):
        width, height = image.size
        new_size = min(width, height)
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        image = image.crop((left, top, right, bottom))
        image = image.resize((224, 224), Image.LANCZOS)
        inputs = self.processor(images=image, return_tensors="pt")
        return inputs

    def classify_image(self, image, model_path=""):
        if model_path:
            current_dir = os.path.dirname(__file__)
            models_dir = os.path.join(current_dir, "models")
            full_model_path = os.path.join(models_dir, model_path)
            self.model = ViTForImageClassification.from_pretrained(full_model_path)
            self.processor = ViTImageProcessor.from_pretrained(full_model_path)

            # 从config.json读取id2label
            config_path = os.path.join(full_model_path, "config.json")
            with open(config_path, 'r') as f:
                config = json.load(f)
                self.model.config.id2label = config.get("id2label", {})

        if image.dim() == 4:
            image = image.squeeze(0)

        image = image.float() / 255.0 if image.dtype == torch.uint8 else image.float()
        image = torch.clamp(image, 0, 1)

        image_np = (image.cpu().numpy() * 255).astype(np.uint8)
        image = Image.fromarray(image_np, mode='RGB')

        inputs = self.preprocess_image(image)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        
        predicted_label = self.model.config.id2label.get(str(predicted_class_idx), "未知")

        scores = torch.nn.functional.softmax(logits, dim=-1).squeeze().tolist()
        detailed_scores = " | ".join([f"{self.model.config.id2label[str(i)]}: {score:.2f}" for i, score in enumerate(scores)])
        
        return predicted_label, detailed_scores