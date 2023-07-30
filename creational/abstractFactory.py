class WidgetFactory():
    def __init__(self) -> None:
        self._widgetFactory = [Adblock("adBlock", "www.playstore.com/adblock"), MetaMask("MetaMask", "www.playstore.com/metamask"), BlockSite("BlockSite", "www.playstore.com/blocksite")]
        
    @property
    def widgets(self):
        return self._widgetFactory

class Widget():
    def __init__(self, name, store_link) -> None:
        self.name = name
        self.store_link = store_link
        
    def getLink(self):
        return self.store_link
    

class Adblock(Widget):
    def __init__(self, name, store_link) -> None:
        super().__init__(name, store_link)
        
    def getLink(self):
        return super().getLink()
    

class MetaMask(Widget):
    def __init__(self, name, store_link) -> None:
        super().__init__(name, store_link)
        
    def getLink(self):
        return super().getLink()


class BlockSite(Widget):
    def __init__(self, name, store_link) -> None:
        super().__init__(name, store_link)
    
    def getLink(self):
        return super().getLink()