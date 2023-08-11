from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def updateTheme(self, color) -> None:
        pass


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        pass
    
    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber) -> None:
        pass
    
    @abstractmethod
    def notifySubscribers(self) -> None:
        pass
 
    @abstractmethod
    def mainBussinessLogic(self) -> None:
        pass

    
class TabPublisher(Publisher):
    def __init__(self, subscribers: [] = []) -> None:
        self.subscribers:[] = subscribers
    
    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber: Subscriber) -> None:
        pass
    
    def notifySubscribers(self, color = "black") -> None:
        for i in self.subscribers:
            i.updateTheme(color)
        

    def mainBussinessLogic(self) -> None:
        pass