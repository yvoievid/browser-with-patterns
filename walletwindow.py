from tkinter import *
from structural.adapter import GoogleWallet, GoogleWalletToApplePayAdapter

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Wallet")
        self.geometry("640x480")
        self.button = Button(self, text="pay with google pay", command=self.google_pay)
        self.button.pack(expand=True)
        self.button = Button(self, text="pay with apple pay", command=self.apple_pay)
        self.button.pack(expand=True)
    
    def google_pay(self):
        wallet = GoogleWallet()
        wallet.pay()
        
        
    def apple_pay(self):
        wallet = GoogleWalletToApplePayAdapter()
        wallet.payWithApplePay()