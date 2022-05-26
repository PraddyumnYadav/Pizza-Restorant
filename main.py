# name, price, ingredients, vegetarian
# Create Class Pizza as Instance
class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGETARIAN"
        print(f"PIZZA  = {self.name} : {self.price}$" + veg_str)
        print(", ".join(self.ingredients))
        print()


class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    price = 0

    def __init__(self, pizza_number):
        super().__init__(f"Custom{pizza_number} ", self.price, [], )
        self.pizza_number = pizza_number
        self.ask_user_for_ingredients()
        self.price = self.compute_price()

    def ask_user_for_ingredients(self):
        while True:
            ingredient = input(f"Add an ingredient for custom pizza no. {self.pizza_number} (or Press Enter to "
                               f"Finish) .\n:-> ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f'You Have {len(self.ingredients)} ingredients(): {", ".join(self.ingredients)}')

    def compute_price(self):
        length_of_ingredients = len(self.ingredients)
        price_ingredients = length_of_ingredients * self.PRICE_PER_INGREDIENT
        price = price_ingredients + self.BASE_PRICE
        return price


pizzas = [
    Pizza("4 cheeses", 8.99, ("blue cheese", "brie", "emmental", "mozzarella"), True),
    Pizza("Hawaii", 9.5, ("tomato", "pineapple", "onions")),
    Pizza("4 seasons", 11, ("eggs", "tomato", "emmental", "ham", "olive")),
    Pizza("Vegetarian", 7.8, ("mushrooms", "tomato", "onions", "bell pepper"), True),
    Pizza("Paneer Pizza", 12.98, ("tomato", "cheese", "Paneer", "Base", "Chili of Shimla"), True),
    CustomPizza(1),
    CustomPizza(2)
]


class PizzaSort:
    def pizza_sort_ingredients(self, pizza):
        return len(pizza.ingredients)

    def pizza_sort_price(self, pizza):
        return pizza.price

    def pizza_sort_alphabets(self, pizza):
        return pizza.name

    def pizza_sort_alphabets_number(self, pizza):
        return len(pizza.name)

    def price(self):
        print("--------------------- Pizzas Sorted According to Their Price --------------------")
        pizzas.sort(key=self.pizza_sort_price)
        for i in pizzas:
            i.display()

        print()

    def alphabets(self):
        print("---------------------- Pizzas Sorted According to their Alphabets --------------------")
        pizzas.sort(key=self.pizza_sort_alphabets)
        for i in pizzas:
            i.display()

        print()

    def num_alphabets(self):
        print("---------------------- Pizza Sorted According Number of Alphabets -----------------------")
        pizzas.sort(key=self.pizza_sort_alphabets_number)
        for i in pizzas:
            i.display()

        print()

    def ingredients(self):
        print("---------------------- Pizzas Sorted According to Their Ingredient List --------------------")
        pizzas.sort(key=self.pizza_sort_ingredients)
        for i in pizzas:
            i.display()


if __name__ == "__main__":
    sort_pizza = PizzaSort()
    print("How do You Want to Sort Pizza for You 1 = Price, 2 = Alphabets, 3 = Length of Alphabets, 4 = Number of "
          "Ingredients .")
    sort_input = int(input(":-> "))
    if sort_input == 1:
        sort_pizza.price()
    elif sort_input == 2:
        sort_pizza.alphabets()
    elif sort_input == 3:
        sort_pizza.num_alphabets()
    else:
        sort_pizza.ingredients()
