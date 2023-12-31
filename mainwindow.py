from tkinter import *
from creational.singleton import Singleton
from creational.builder import TabBuilder
from structural.bridge import *
from behaviour.iterator import *
from behaviour.observer import *
from behaviour.command import *
import widgetwindow
import tabwindow
import walletwindow
import findwindow
import moodlewindow


class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()
        self.tabs = TabsCollection()
        self.themePublisher = TabPublisher(self.tabs)
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
        
        self.moodleWindow = Button(self, text="Moodle", command=self.openMoodle)
        self.moodleWindow.grid(row=1, column=5)
        
        self.darkThemeButton = Button(self, text="Dark Theme", command=self.darkThere)
        self.darkThemeButton.grid(row=2, column=1)
        
        self.whiteThemeButton = Button(self, text="White Theme", command=self.whiteThere)
        self.whiteThemeButton.grid(row=2, column=2)
        
    def searchGoogle(self):
        searchCommand = SearchCommand(self.searchBar.get())
        searchCommand.execute()
        
    def darkThere(self):
        self.themePublisher.notifySubscribers("black")
        
    
    def whiteThere(self):
        self.themePublisher.notifySubscribers("white")

    
    def openMoodle(self):
        global moodle
        moodle = moodlewindow.Extra()
        
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