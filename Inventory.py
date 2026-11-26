# Creating inventory dictionary
inventory = {
    "Sugar": 50,
    "Bread": 80,
    "Milk": 60,
    "Rice": 40,
    "Soap": 100
}

# Display quantity of a specified product
print("Quantity of Milk:", inventory["Milk"])

# Add a new product
inventory["Cooking Oil"] = 30

# Update quantity of an existing product
inventory["Sugar"] = 70

# Remove one product
del inventory["Soap"]

# Display final inventory
print("\nFinal Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)