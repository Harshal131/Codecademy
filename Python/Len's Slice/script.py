# To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
# pepperoni
# pineapple
# cheese
# sausage
# olives
# anchovies
# mushrooms

toppings=['pepperoni','pineapple','cheese','sausage','olives','anchoives','mushrooms']

# To keep track of how much each kind of pizza slice costs, create a list called prices that holds:
# 2
# 6
# 1
# 3
# 2
# 7
# 2

prices=[2,6,1,3,2,7,2]

# Find the length of the toppings list and store it in a variable called num_pizzas.

num_pizzas=len(toppings)

# Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.

print("We sell "+str(num_pizzas)+" kinds of pizza!")

# Use zip to combine the two lists into a list called pizzas

pizzas=list(zip(toppings,prices))
print(pizzas)

# Sort pizzas so that the pizzas with the lowest prices are at the start of the list.
pizzas.sort()

# Store the first element of pizzas in a variable called cheapest_pizza.

cheapest_pizza=pizzas[0]

# A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”Get the last item of the pizzas list and store it in a variable called priciest_pizza.

priciest_pizza=pizzas[-1]

# Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.

three_cheapest=pizzas[0:3]
print(three_cheapest)

# our boss wants you to do some research on $2 slices.Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.

num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)