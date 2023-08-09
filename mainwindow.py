from tkinter import *
from creational.singleton import Singleton
from creational.builder import TabBuilder
from structural.bridge import *
from behaviour.iterator import *
import widgetwindow
import tabwindow
import walletwindow
import findwindow


class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()
        self.tabs = TabsCollection()
        self.openWidgetsButton = Button(self, text="open widget window", command=self.createWindowWidgets)
        self.openWidgetsButton.grid(row=0, column=0)
        
        self.addTabButton = Button(self, text="create tab", command=self.createTab)
        self.addTabButton.grid(row=0, column=1)

        self.payment = Button(self, text="Payment", command=self.openPayments)
        self.payment.grid(row=0, column=2)
        
        self.find = Button(self, text="Find Cats", command=self.findWidget)
        self.find.grid(row=0, column=3)
        
        self.yotubeWidget = Button(self, text="Facebook", command=self.openFacebook)
        self.yotubeWidget.grid(row=1, column=3)
        
        self.facebookWidget = Button(self, text="Youtube", command=self.openYoutube)
        self.facebookWidget.grid(row=1, column=4)
        
        
    def openFacebook(self):
        global facebookTab
        facebookFunctionality = FacebookCall()
        widget =  FacebookMainPageApp(facebookFunctionality)
        facebookTab = tabwindow.Tab("facebook", widget)
    
    def openYoutube(self):
        global youtube
        youtubeFunctionality = YoutubeCall()
        widget = YoutubeMainPageApp(youtubeFunctionality)
        youtube = tabwindow.Tab("youtube", widget)
        
    def findWidget(self):
        global findWindow
        findWindow = findwindow.Extra()

    def createWindowWidgets(self):
        global extraWindow
        extraWindow = widgetwindow.Extra()
    
    def createTab(self):
        tab = TabBuilder().withLinks("www.google.com").withThumbnail("gooogle").withPhotos("googlePhoto").build()
        self.tabs.add_item(tab)
        
    def openPayments(self):
        global payments
        payments = walletwindow.Extra() 
        
    
    def __init__(self, screenName: str = None, baseName: str = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str = None) -> None:
        pass