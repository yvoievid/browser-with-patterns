from abc import ABC, abstractmethod
from behaviour.iterator import *

class TabBuilder(ABC):
    def __init__(self) -> None:
        self.tab = Tab()
        pass
    

    def withThumbnail(self, thumbnail):
        self.thumbnail = thumbnail
        return self
    

    def withPhotos(self, photos):
        self.photos = photos
        return self


    def withLinks(self, links):
        self.links = links
        return self


    def build(self):
        return self.tab
    
    