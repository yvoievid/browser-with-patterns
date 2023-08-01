from abc import ABC, abstractmethod


class Wallet(ABC):
    @abstractmethod
    def pay():
        pass

class ApplePay(Wallet):
    def __init__(self) -> None:
        pass
    
    def pay(self):
        print("paying with apple pay....")
        


class GoogleWallet(Wallet):
    def __init__(self) -> None:
        pass
    
    def pay(self):
        print("paying with google wallet...")
        
        

class GoogleWalletToApplePayAdapter():
    def __init__(self) -> None:
        self.applePayWallet = ApplePay()
        pass
    
    def payWithApplePay(self):
        self.applePayWallet.pay()