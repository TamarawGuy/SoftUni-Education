class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if self.price <= money and self.owner == None:
            self.owner = owner
            change = money - self.price
            print(f"Successfully bought a {self.type}. Change: {change:.2f}")
        elif self.price > money:
            print("Sorry, not enough money")
        elif self.owner != None:
            print('Car already sold')
        
    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"
        
    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owner by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"