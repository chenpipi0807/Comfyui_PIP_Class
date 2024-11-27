---
PIPClass 图像分类节点
PIPClass是一个基于ViT（Vision Transformer）模型的Python类，专为图像分类设计。它不仅可以快速识别图像中的内容，还能提供详细的分类得分，帮助用户更好地理解模型的判断依据。
PIP_ClassV1 模型是基于ViT-B/16预训练模型，在动漫、非人类、真人、三个类别上进行全量微调训练。

### 主要功能
1. **图像分类**：利用预训练的ViT模型，PIPClass可以准确地对输入的图像进行分类，返回最可能的类别。
2. **自定义模型路径**：用户可以指定模型路径来加载自定义的训练模型，增加了模型的灵活性和适用范围。
3. **图像预处理**：自动对输入的图像进行中心裁剪和调整大小，确保图像符合模型的输入要求，从而提高分类的准确性（目前尺寸为224x224）。
![微信截图_20241127163951](https://github.com/user-attachments/assets/448b6580-2ce2-406d-a9c8-4c5395e64ebf)
![微信截图_20241127163939](https://github.com/user-attachments/assets/fe666fa8-fa74-48d5-98fc-fb5c6dc3fbed)
![微信截图_20241127163900](https://github.com/user-attachments/assets/9fdc51fd-914d-4c41-a03e-801cf60daaba)

### 使用方法
- **输入参数**：
  - `image`: 需要分类的图像，类型为IMAGE。
  - `model_path` (可选): 指定使用的模型路径，默认为"PIP_ClassV1"。
- **输出结果**：
  - `分类标签`: 返回图像的预测类别标签。
  - `分类详情`: 显示每个类别的得分详情，帮助用户理解模型的分类决策。

### 使用方法

PIP_ClassV1 模型是基于ViT-B/16预训练模型，在动漫、非人类、真人、三个类别上进行全量微调训练。

模型下载链接：
通过百度网盘分享的文件：model.safetensors
链接：https://pan.baidu.com/s/1cdMSZvlBhBccyDuYWL81gg?pwd=pip6 
提取码：pip6 
--来自百度网盘超级会员V5的分享

模型路径：
Comfyui_PIP_Class/models/PIP_ClassV1/模型

通过以上功能和简单的参数配置，PIPClass能够为用户提供强大且直观的图像分类服务。
