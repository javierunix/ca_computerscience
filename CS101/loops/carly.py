hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Create a variable to sum up all prices and set it to 0
total_price = 0

# 2. Loop over prices and add to total price
for item in prices:
    total_price += item

# 3. Calculate average price
average_price = total_price / len(prices)

# 4.
print("Average Haircut Price:", average_price)

# 5. Use list comprehension to make a list, which as each element in prices minus 5
new_prices = [item - 5 for item in prices]

# 6.
print(new_prices)

# 7. Create a variable and set it to 0
total_revenue = 0

# 8. 
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i] # add to total_revenue price of cut multiplied by number of people.

print("Total Revenue:", total_revenue)

# 9. Print average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# 10. Store in a list the cuts under 30
cuts_under_30 = [] # new empty list
for i in range(len(hairstyles)):
    if prices[i] < 30:
        cuts_under_30.append(hairstyles[i]) # append element to new list if price is under 30

print(cuts_under_30)
