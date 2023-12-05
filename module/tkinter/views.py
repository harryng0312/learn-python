import tkinter as tk
from tkinter import Misc, ttk
from tkinter.scrolledtext import ScrolledText

from module.tkinter import controllers

class PasswordFormView(ttk.Frame):
    def __init__(self, master: Misc | None = None, **kw) -> None:
        super().__init__(master, **kw)
        self.__init_view()
        return

    def __add_controls(self) -> None:
        style = ttk.Style(master=self.master)
        # style.theme_use("default")
        # Create style used by default for all Frames
        style.configure(style='ThemedFrame.TFrame', padding=10)
        # add frame
        self.config(style="ThemedFrame.TFrame")
        # create layout
        self.grid(row=7, column=2, padx=10, pady=10)
        # frm.pack(expand=True)
        # add controls
        lb_client_pub_key = ttk.Label(master=self, text="Client Public Key")
        lb_client_pub_key_val = ttk.Label(master=self, text="")
        lb_server_pub_key = ttk.Label(master=self, text="Server Public Key")
        txt_server_pub_key = ScrolledText(master=self, width=36, height=4)
        # txt_server_pub_key.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        btn_enc = ttk.Button(master=self, text="Click Me")

        lb_client_pub_key.grid(row=0, column=0)
        lb_client_pub_key_val.grid(row=0, column=1)
        lb_server_pub_key.grid(row=1, column=0)
        txt_server_pub_key.grid(row=1, column=1)
        btn_enc.grid(row=2, column=1)
        
        # self.pack()
        # bind events
        # add        
        return
    
    def __init_view(self) -> None:
        self.__add_controls()
        return


    @property
    def controller(self) -> controllers:
        return self.__controller
    
    @controller.setter
    def controller(self, controller: controller):
        self.__controller = controller
        return

    # end class
    pass