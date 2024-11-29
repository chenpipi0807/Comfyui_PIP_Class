---
PIPClass 图像分类节点
PIPClass是一个基于ViT（Vision Transformer）模型的Python类，专为图像分类设计。它不仅可以快速识别图像中的内容，还能提供详细的分类得分，帮助用户更好地理解模型的判断依据。
PIP_ClassV1 模型是基于ViT-B/16预训练模型，在动漫、非人类（动物/场景/几何图形）、真人、三个类别上进行全量微调训练。
该模型在300张各类图片中做过批量测试，准确率大约90%。

我寻思独乐了不如众乐乐，完了我就整了个能加载大多数VIT模型的玩意出来，反正这玩意结构也差不太多，好像现在还没人这么整呢，至少我没发现。
当然如果你微调了vit模型又懒得写节点，那你直接用这玩意也行。
理论上你知道要把模型文件夹胡楞个的扔进models里就行了

### 主要功能
1. **图像分类**：利用预训练的ViT模型，PIPClass可以准确地对输入的图像进行分类，返回最可能的类别。
2. **自定义模型路径**：用户可以指定模型路径来加载自定义的训练模型，增加了模型的灵活性和适用范围。
3. **图像预处理**：自动对输入的图像进行中心裁剪和调整大小，确保图像符合模型的输入要求，从而提高分类的准确性（目前尺寸为224x224）。

![微信截图_20241129125450](https://github.com/user-attachments/assets/dcc69b73-49f0-41f1-9da8-4f820c8e40f7)

![微信截图_20241127163951](https://github.com/user-attachments/assets/448b6580-2ce2-406d-a9c8-4c5395e64ebf)
![微信截图_20241127163939](https://github.com/user-attachments/assets/fe666fa8-fa74-48d5-98fc-fb5c6dc3fbed)
![微信截图_20241127163900](https://github.com/user-attachments/assets/9fdc51fd-914d-4c41-a03e-801cf60daaba)
![微信截图_20241129111714](https://github.com/user-attachments/assets/d21e7365-bda2-42aa-8ddc-6fd9f10c8a8c)

### 重要更新
11/29. **VIT模型加载**
新增了对于三方图像分类模型的加载，你只需要在models下 git clone https://huggingface.co/Falconsai/nsfw_image_detection（示例，亲测有效）
确保你的文件结构类似这样：
- `Comfyui_PIP_Class/models/*:.
├─nsfw_image_detection
│      .gitattributes
│      config.json
│      model.safetensors
│      optimizer.pt
│      preprocessor_config.json
│      pytorch_model.bin
│      README.md
│
└─PIP_ClassV1
        all_results.json
        config.json
        model.safetensors
        preprocessor_config.json
        training_args.bin
`


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
