import time


class atm_file:

    def __init__(self):
        self.ids = []
        self.pins = []
        self.atms = []
        self.home_page()

    def choice_page(self,id):
        print("Select your Option")
        print("1.Withdraw\n2.Balance\n3.Deposit\n4.Exit")
        option = int(input("Enter Your Option: "))
        if option == 1:
            self.withdraw(id)

        elif option == 2:
            self.balance(id)

        elif option == 3:
            self.deposit(id)

        elif option == 4:
            exit()
        else:
            self.home_page()

    def home_page(self):
        id = input("Enter The Id: ")
        pin = input("Enter The Pin: ")
        if id == "admin" and pin == "admin":
            self.new_user()

        elif int(id) == self.ids[int(id)] and int(pin) == self.pins[int(id)]:
            self.choice_page(int(id))

        else:
            self.home_page()

    def withdraw(self, id):
        withdraw_amt = int(input("Enter The Withdraw Amount: "))
        if withdraw_amt <= self.atms[id]:
            self.atms[id] = self.atms[id] - withdraw_amt
            print("The Balance Amt is ", self.atms[id])
            time.sleep(5)
            self.choice_page(id)
        else:
            print("Insufficient Balance!!")
            time.sleep(5)
            self.withdraw(id)

    def balance(self,id):
        print("================== Balance Report ===================")
        print("Id         : ",id)
        print("Balance    : ",self.atms[id])
        print("=====================================================")
        time.sleep(5)
        self.choice_page(id)

    def deposit(self,id):
        deposit_amt = int(input("Enter the Deposit Amount: "))
        self.atms[id] = self.atms[id] + deposit_amt
        time.sleep(5)
        self.choice_page(id)

    def new_user(self):
        new_id = int(input("Enter Your New Id: "))
        new_pin = int(input("Enter Your New Pin: "))
        new_amt = int(input("Enter your new Amount: "))
        self.ids.append(new_id)
        self.pins.append(new_pin)
        self.atms.append(new_amt)
        print("User Created Successfully!!")
        time.sleep(5)
        self.home_page()
