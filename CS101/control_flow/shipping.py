weight = float(input('Introduce the weight (in pounds of the package: ')) # Define a variable called weight and set it to any number

# ********* Ground shipping ***************

# The standard shipping cost depend on the weight
if weight <= 2: # if weight is equal or less than 2 pounds
    standard_cost = 1.5 * weight + 20
elif 2 < weight <= 6: # if weight is between 2 and 6 pounds
    standard_cost = 3 * weight + 20
elif 6 < weight <=  10: # if weight is between 6 and 10 pounds
    standard_cost = 4 * weight + 20
elif weight > 10: # if weight is more than 10 pounds
    standard_cost = 4.75 * weight + 20
else:
    standard_cost = 0

# The premium cost is always the same
premium_cost = 125


# ********* Drone shipping ***************
# The drone shipping cost depend on the weight

if weight <= 2: # if weight is equal or less than 2 pounds
    drone_cost = 4.5 * weight
elif 2 < weight <= 6: # if weight is between 2 and 6 pounds
    drone_cost = 9 * weight
elif 6 < weight <=  10: # if weight is between 6 and 10 pounds
    drone_cost = 12 * weight
elif weight > 10: # if weight is more than 10 pounds
    drone_cost = 14.25 * weight
else:
    drone_cost = 0




# find out which is the cheapest shipping method
cheapest = min(standard_cost, drone_cost, premium_cost) # select the minimum of the three variables

# print a message according with recommended shipping method
if cheapest == standard_cost:
    print('The recommended shipping method is standard, with a cost of %.2f $.' %cheapest)
elif cheapest == drone_cost:
    print('The recommended shipping method is drone, with a cost of %.2f $.' %cheapest)
elif cheapest == premium_cost:
    print('The recommended shipping method is premium, with a cost of %.2f $.' %cheapest)
