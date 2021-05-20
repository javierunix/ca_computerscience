# create toppings list

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# crate prices list
prices = [2, 6, 1, 3, 2, 7, 2]

# count number of ocurrences of 2 in prices
num_two_dollar_slices = prices.count(2)


# find the length of the topping list and store in a variable called num_pizzas
num_pizzas = len(toppings)

# print a string
print("We sell %i different kinds of pizza!" %num_pizzas)

# convert toppings and prices into a two dimensional list called pizza_and_prices

pizza_and_prices = [] # new empty_list

for i in range(num_pizzas): # iterate over the previous list
    pizza_and_prices.append([toppings[i], prices[i]]) # add a sublist in every iteration
    
#print(pizza_and_prices)

# sort pizza by price, in increasing price
pizza_and_prices_sorted = sorted(pizza_and_prices, key=lambda x: x[1]) # sort using the second element of the sublist as key.

# store the first element in a variable
cheapest_pizza = pizza_and_prices_sorted[0]

# store the priciest pizza in a variable
priciest_pizza = pizza_and_prices_sorted[-1]

# remove last element from sorted list
pizza_and_prices_sorted.remove(pizza_and_prices_sorted[-1])

# add new pizza to list
peppers = ["peppers", 2.5] # new pizza
pizza_and_prices_sorted.append(peppers) # add new element

pizza_and_prices_sorted = sorted(pizza_and_prices_sorted, key=lambda x: x[1]) # we have to sort again the list, since the last element has been added unsorted

# slice the list and store the 3 lowest cost pizza in a list called three_cheapest

three_cheapest = [] # new_list
for i in range(3):
    three_cheapest.append(pizza_and_prices_sorted[0]) # add the cheapest pizza to the new list
    pizza_and_prices_sorted.remove(pizza_and_prices_sorted[0]) # remove the cheapest once have been added
    
print(pizza_and_prices_sorted)
print(three_cheapest)
