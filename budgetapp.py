class Category:
    def __init__(self, name):
        self.name = name 
        self.ledger = []
        
    def __str__(self):
        title = self.name.center(30, "*")
        lines = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item["amount"]:.2f}".rjust(7)
            lines += f"{desc}{amt}\n"
        total_line = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{lines}{total_line}"
            
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfter to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()   
    
def create_spend_chart(categories):
    print("Percentage spent by category")
    total_spent = sum(-item["amount"] for cat in categories for item in cat.ledger if item["amount"] < 0)
    
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        percentage = int(spent / total_spent * 100) // 10
        # print(percentage)
        
    display = "" 
    for i in range(100, -1, -10):
        if percentage == i and percentage != 0:
            display = (str(i).rjust(3) + "|" + "o")
            # print(display)
        else:
            display = (str(i).rjust(3) + "|")
            
        print(display)
        
    print(" " * 4 + "-"  + "---"* len(categories))
    
    # for 

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
cars = Category("Cars")

create_spend_chart([food, clothing, cars])