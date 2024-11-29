from .PIP_Class import PIPClass
from .PIP_Class_Advanced import PIPClassAdvanced

NODE_CLASS_MAPPINGS = {
    "PIPClass": PIPClass,
    "PIPClassAdvanced": PIPClassAdvanced
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPClass": "PIP 图像分类",
    "PIPClassAdvanced": "PIP 图像分类高级版"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 
