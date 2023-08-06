from tkinter import *
from creational.singleton import Singleton
from creational.builder import TabBuilder
import widgetwindow
import tabwindow
import walletwindow
import findwindow


class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()
        self.openWidgetsButton = Button(self, text="open widget window", command=self.createWindowWidgets)
        self.openWidgetsButton.pack(expand=True)
        self.addTabButton = Button(self, text="create tab", command=self.createTab)
        self.addTabButton.pack(expand=True)

        self.payment = Button(self, text="Payment", command=self.openPayments)
        self.payment.pack(expand=True)
        
        self.find = Button(self, text="Find Cats", command=self.findWidget)
        self.find.pack(expand=True)

    def findWidget(self):
        global findWindow
        findWindow = findwindow.Extra()

    def createWindowWidgets(self):
        global extraWindow
        print('hellp')
        extraWindow = widgetwindow.Extra()
    
    def createTab(self):
        tab = TabBuilder().withLinks("www.google.com").withThumbnail("gooogle").withPhotos("googlePhoto").build()
        self.tabs.append(tab)
        
    def openPayments(self):
        global payments
        payments = walletwindow.Extra() 
        
    
    def __init__(self, screenName: str = None, baseName: str = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str = None) -> None:
        pass