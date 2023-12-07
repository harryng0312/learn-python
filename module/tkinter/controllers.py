from __future__ import annotations
import tkinter as tk
from module.tkinter.models import PasswordFormModel
from module.tkinter.views import PasswordFormView

class PasswordFormController(object):
    
    def __init__(self, model: PasswordFormModel, view: PasswordFormView) -> None:
    # def __init__(self, model: PasswordFormModel, view) -> None:
        self.model = model
        self.view = view
        return
    
    def init_view(self) -> None:
        self.view.init_view(self.model)
        print(f"model in controller:{id(self.model)}")
        return

    def encrypt_passwd(self) -> None:
        return
    
    def btn_encrypt_passwd(self, evt:tk.Event) -> None:
        print(f"model in event:{id(self.model)}")
        import json
        attributes = vars(self.model)
        serialized_dict = {}
        for key, value in attributes.items():
            if isinstance(value, tk.StringVar):
                serialized_dict[key] = value.get()
        print(f"model:{json.dumps(obj=serialized_dict)}")
        return

    pass