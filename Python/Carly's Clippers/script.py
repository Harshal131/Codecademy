hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

total_price=0

# Iterate through the prices list and add each price to the variable total_price.

for i in prices:
  total_price+=i

# After your loop, create a variable called average_price that is the total_price divided by the number of prices.

average_price=total_price/len(prices)
print(average_price)

# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

new_prices=[i-5 for i in prices]
print(new_prices)

# Use a for loop to create a variable i that goes from 0 to len(hairstyles).Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.

total_revenue=0
for i in range(len(hairstyles)):
  total_revenue+=prices[i]*last_week[i]
print(total_revenue)
average_daily_revenue=total_revenue/7
print(average_daily_revenue)

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

cuts_under_30=[hairstyles[i] for i in range(len(new_prices)-1) if i<30  ]
print(cuts_under_30)