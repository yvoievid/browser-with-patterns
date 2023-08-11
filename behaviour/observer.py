from abc import ABC, abstractmethod


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


class Subscriber(ABC):
    @abstractmethod
    def update(subject: Publisher) -> None:
        pass
        

    
class TabPublisher():
    def __init__(self, subscribers, mainState) -> None:
        self.subscribers = subscribers
        self.mainState = mainState
    
    def subscribe(self):
        pass