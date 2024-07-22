class ATM:
    def __init__(self):
        self.balance=0
        self.history=[]
    def check_balance(self):
        print(f"Your Balance is Rs {self.balance}")
    def Deposit(self):
        amt=int(input("Enter The Amount You Want to Deposit: "))
        self.balance +=amt
        self.history.append(f"Deposited Rs {amt}")
        print(f"Amount of Rs {amt} has been deposited Sucessfully")
    def Withdraw(self):
        amt=int(input("Enter The Amount You Want to Withdraw: "))
        if self.balance>=amt:
            self.balance -=amt
            self.history.append(f"Withdrawn Rs {amt}")
            print(f"Amount of Rs {amt} has been WithDrawn Sucessfully")
        else:
            print("Insufficient Balance")
    def Transaction_History(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("The Transaction History is: ")
            for i in self.history:
                print(i)
def person():
    p=ATM()
    while True:
        print("\nATM Interface: ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Exit")     
        choice = int(input("Choose an option: "))
        if choice == 1:
            p.check_balance()
        elif choice == 2:
            p.Deposit()
        elif choice == 3:
            p.Withdraw()
        elif choice == 4:
            p.Transaction_History()
        elif choice == 5:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice, please try again.")
person()
print("Visit Again..")

    

    