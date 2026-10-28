# Create a tuple
customer = (
    "Rose Kamau",  # Customer Name
    "C001", # Customer ID
    "0712345678",# Telephone Number
    "rosekamau22@gmail.com" # Email Address
)

# Display the complete tuple
print("Customer Tuple:", customer)

# Access and display customer's name and telephone number
print("Customer Name:", customer[0])
print("Telephone Number:", customer[2])

# Display the number of items in the tuple
print("Number of Items:", len(customer))

# Attempt to modify the telephone number
# customer[2] = "0798765432"

print("\nModification cannot be performed.")
print("Reason: Tuples are immutable, meaning their values cannot be changed after creation.")