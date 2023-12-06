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
        self.master.grid_rowconfigure(index=0, weight=1)
        self.master.grid_columnconfigure(index=0, weight=1)
        style = ttk.Style(master=self)
        style.theme_use("default")
        # lb_style.theme_use("default")
        # Create style used by default for all Frames
        style.configure(style='tf.TFrame', padding=(0, 5))
        lb_style = ttk.Style(master=self).configure(style='tf.TLabel')
        txt_style = ttk.Style(master=self).configure(style='tf.TEntry')
        # add frame
        self.config(style="tf.TFrame")
        # self.config(style="tf.TWidget")
        # create layout
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(index=1, weight=1)
        # self.grid_configure(ipadx=15, ipady=15, sticky="nsew")
        # self.pack(fill=tk.BOTH, expand=True)
        # frm.pack(expand=True)
        # add controls
        lb_client_pub_key = ttk.Label(master=self, style="tf.TLabel", text="Client Public Key")
        lb_client_pub_key_val = ttk.Label(master=self, style="tf.TLabel", text="")
        lb_server_pub_key = ttk.Label(master=self, style="tf.TLabel", text="Server Public Key")
        # txt_server_pub_key = ScrolledText(master=self, width=36, height=4)
        txt_server_pub_key = ttk.Entry(master=self, style="tf.TEntry")
        txt_session_id = ttk.Entry(master=self, style="tf.TEntry")
        
        # txt_server_pub_key.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        btn_enc = ttk.Button(master=self, text="Click Me")

        # layout
        lb_client_pub_key.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_client_pub_key_val.grid(row=0, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        lb_server_pub_key.grid(row=1, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        txt_server_pub_key.grid(row=1, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_session_id.grid(row=2, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        btn_enc.grid(row=5, column=1, columnspan=2, padx=(0, 5), pady=(0, 5), sticky="w")
        
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