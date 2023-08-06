from abc import ABC, abstractmethod


class MainPageApp():
    def __init__(self, app) -> None:
        self.app = app
    
    def open(self):
        return self.app.call()
    

class YoutubeMainPageApp(MainPageApp):
    def open(self):
        return self.app.call()
        
class FacebookMainPageApp(MainPageApp):
    def open(self):
        return self.app.call()
        
        
class AppCall(ABC):
    @abstractmethod
    def call(self):
        pass
        
        
class YoutubeCall(AppCall):
    def call(self):
        return "Opening Youtube"
    

class FacebookCall(AppCall):
    def call(self):
        return "Opening Facebook"