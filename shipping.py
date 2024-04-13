# Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
#
# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
# 
# Sal’s Shippers has several different options for a customer to ship their package:
# - Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# - Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# - Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

weight = 41.5
ground_cost = 0.0
ground_premium_cost = 0.0
ground_flat_charge = 20.00
ground_premium_charge = 125.00
drone_cost = 0.0


# Ground shipping
if weight <= 2.0:
    ground_cost = weight * 1.5
elif weight > 2.0 and weight <= 6.0:
    ground_cost = weight * 3.0
elif weight > 6.0 and weight <= 10.0:
    ground_cost = weight * 4.0
else:
    ground_cost = weight * 4.75

ground_cost += ground_flat_charge
ground_premium_cost += ground_premium_charge
print(f"Ground Shipping: {ground_cost}")
print(f"Ground Shipping Premium: {ground_premium_cost}")

# Drone shipping
if weight <= 2.0:
    drone_cost = 4.5 * weight
elif weight > 2.0 and weight <= 6:
    drone_cost = 9.0 * weight
elif weight > 6 and weight <= 10:
    drone_cost = 12.0 * weight
else:
    drone_cost = 14.25 * weight
 
print(f"Drone Shipping: {drone_cost}")

# Cheapest shipping
cheapest_shipping = f"The cheapest shipping method for a package that weighs {weight} pounds"
if ground_cost < ground_premium_cost and ground_cost < drone_cost:
    print(f"{cheapest_shipping} is Ground Shipping and the cost is ${ground_cost}")
elif ground_premium_cost < ground_cost and ground_premium_cost < drone_cost:
    print(f"{cheapest_shipping} is Ground Premium Shipping and the cost is ${ground_premium_cost}")
elif drone_cost < ground_cost and drone_cost < ground_premium_cost:
    print(f"{cheapest_shipping} is Drone Shipping and the cost is ${drone_cost}")
else:
    print("Error. The cheapest shipping method can not be determined")