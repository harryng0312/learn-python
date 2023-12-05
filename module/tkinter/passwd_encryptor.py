import tkinter as tk
from tkinter import ttk

from module.tkinter import controllers, models, views

class App(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        return

    def __init_windows(self) -> None:
        # set wd size
        self.geometry(f"{400}x{200}")
        # set wd position at center of screen
        center_x = int(self.winfo_screenwidth()/2 - self.winfo_width()/2)
        center_y = int(self.winfo_screenheight()/2 - self.winfo_height()/2)
        self.geometry(f"+{center_x}+{center_y}")
        return

    def __init_app(self) -> None:
        self.title("Encryptor")
        # create Model
        model: models.PasswordFormModel = models.PasswordFormModel()
        # create View
        view: views.PasswordFormView = views.PasswordFormView(self)
        # create Controller
        controller: controllers.PasswordFormController = controllers.PasswordFormController(model=model, view=view)
        view.controller = controller

        return

    def start(self) -> None:
        self.__init_app()
        self.__init_windows()
        self.mainloop()
        return
    
    # end class
    pass



if __name__ == "__main__":
    app = App()
    app.start()
    pass