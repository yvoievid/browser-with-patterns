from tkinter import *
from creational.singleton import Singleton
import widgetwindow
class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()
        
        self.button = Button(self, text="open widget window", command=self.create_window_widgets)
        self.button.pack(expand=True)
        
    def create_window_widgets(self):
        global extraWindow
        extraWindow = widgetwindow.Extra()
        
        
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        pass