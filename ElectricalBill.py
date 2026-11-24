# Function to calculate electricity bill
def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill

# Input from user
units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))

# Call function
total_bill = calculate_bill(units, cost)

# Display result
print("Electricity Bill: KSh", total_bill)