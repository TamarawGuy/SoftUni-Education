class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        self.ordered = True
        result = f"You ordered pizza {self.name} prepared with "
        for i, q in self.ingredients.items():
            result += f"{i}: {q}, "

        result += f"and the price will be {self.price}lv."
        return result


