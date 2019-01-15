#Len's slice project

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
price =[2, 6, 1, 3, 2, 7, 2]
num_pizzas= len(toppings)
print("We sell " + str(num_pizzas) + " kinds of pizzas!")
pizzas = zip(price, toppings)
print(list(pizzas))
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
cheapest_three = pizzas[0:3]
print(cheapest_three)
num_two_dollar_slices = pric	e.count(2)
print(num_two_dollar_slices)