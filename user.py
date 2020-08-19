class User:		
    def __init__(self, name, balance):
        self.name = name
        self.account_balance = balance
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        if(self.account_balance - amount) < 0:
            print("insufficient funds in the account")
        else:    
            self.account_balance -= amount


    def display_user_balance(self):
        print(f"{self.name}'s balance: {self.account_balance}")

    

hanson = User("Hanson",0)
tony = User("Tony",0)
rogers = User("Captin",0)


hanson.make_deposit(600)
hanson.make_deposit(400)
hanson.make_deposit(1020)
hanson.make_withdraw(650)
hanson.display_user_balance()

tony.make_deposit(1000)
tony.make_deposit(1000)
tony.make_withdraw(500)
tony.make_withdraw(600)
tony.display_user_balance()

rogers.make_deposit(3000)
rogers.make_withdraw(2000)
rogers.make_withdraw(500)
rogers.make_withdraw(600)
rogers.display_user_balance()

