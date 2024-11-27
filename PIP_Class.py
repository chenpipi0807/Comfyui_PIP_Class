from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import os
import numpy as np

class PIPClass:
    @classmethod
    def INPUT_TYPES(cls):
        # 获取models目录下的所有子目录作为模型选项
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
    CATEGORY = "PIP 图像分类"
    FUNCTION = "classify_image"

    def __init__(self, model_path="PIP_ClassV1"):
        # 获取当前脚本的目录
        current_dir = os.path.dirname(__file__)
        full_model_path = os.path.join(current_dir, "models", model_path)

        # 打印模型路径以调试
        print(f"Loading model from: {full_model_path}")

        # 加载模型和预处理器
        self.model = ViTForImageClassification.from_pretrained(full_model_path)
        self.processor = ViTImageProcessor.from_pretrained(full_model_path)
        
        # 手动设置id2label（如果需要）
        self.model.config.id2label = {
            "0": "动漫",
            "1": "非人",
            "2": "真人"
        }

    def preprocess_image(self, image):
        # 中心裁剪
        width, height = image.size
        new_size = min(width, height)
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        image = image.crop((left, top, right, bottom))
        
        # 调整大小到224x224
        image = image.resize((224, 224), Image.LANCZOS)
        
        # 预处理
        inputs = self.processor(images=image, return_tensors="pt")
        return inputs

    def classify_image(self, image, model_path=""):
        # 确保输入是一个三维张量
        if image.dim() == 4:
            image = image.squeeze(0)  # 去除批次维度

        # 确保图像数据在0-1范围内
        image = image.float() / 255.0 if image.dtype == torch.uint8 else image.float()
        image = torch.clamp(image, 0, 1)

        # 转换为PIL图像
        image_np = (image.cpu().numpy() * 255).astype(np.uint8)
        image = Image.fromarray(image_np, mode='RGB')

        # 预处理图像
        inputs = self.preprocess_image(image)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        
        # 获取预测标签
        predicted_label = self.model.config.id2label.get(str(predicted_class_idx), "未知")

        # 获取每个类别的分数详情
        scores = torch.nn.functional.softmax(logits, dim=-1).squeeze().tolist()
        detailed_scores = " | ".join([f"{self.model.config.id2label[str(i)]}: {score:.2f}" for i, score in enumerate(scores)])
        
        return predicted_label, detailed_scores

# 包含所有要导出的节点的字典，以及它们的名称
NODE_CLASS_MAPPINGS = {
    "PIPClass": PIPClass
}

# 包含节点的友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPClass": "PIP 图像分类"
}