class BankAccount:
    ROI = 10.5  
    
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")

    def Deposit(self):
        value = int(input("Enter amount to deposit: "))
        self.Amount += value
        print("Amount deposited successfully.")

    def Withdraw(self):
        value = int(input("Enter amount to withdraw: "))
        if value > self.Amount:
            print("Insufficient balance!")
        else:
            self.Amount -= value
            print("Amount withdrawn successfully.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


obj1 = BankAccount("Ashutosh", 1000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest:", obj1.CalculateInterest())

print()

obj2 = BankAccount("Ashu", 2000)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest:", obj2.CalculateInterest())
