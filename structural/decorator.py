class Notifier():
    def __init__(self) -> None:
        pass
    
    def notify():
        print("notifying")
        pass
    
    
class NotifierDecorator(Notifier):
    
    _notifier: Notifier = None
    
    def __init__(self, notifier) -> None:
        self._notifier = notifier


    def notify(self):
        self._notifier.notify()
    

    

class SlackNotifier(NotifierDecorator):
    def __init__(self, notifier) -> None:
        super().__init__(notifier)
        
    
    def notify(self):
        return super().notify()
    