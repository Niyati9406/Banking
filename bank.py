
import sys
class customer:
    '''Customer class with bank realted customers'''
    bankname='NiyatiBank'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        
    def deposit(self,amt):
        self.balance=self.balance + amt
        print('after deposit the balance:',self.balance)
        
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Funds..you cant perform the operation')
            sys.exit()
        else:
            self.balance=self.balance - amt
            print('after withdraw the balance:',self.balance)

                  
print('welcome to',customer.bankname)
name=input('enter your name')
t=customer(name)
while True:
    print('d-deposit\n')
    print('w-withdraw\n')
    print('e-exit')
    option=input('choose your option:')
    
    if option=='d' or option=='D':
        amt=float(input('enter the amount to deposit'))
        t.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter the amount to withdraw'))
        t.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thanks for banking')
        sys.exit()
    else:
        print('choose valid option')

                                    
                        
                  

