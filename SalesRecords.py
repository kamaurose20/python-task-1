f = open("sales.txt", "a")

# Get sales details from the user
product = input("Enter product name: ")
quantity = input("Enter quantity sold: ")
total_sales = input("Enter total sales amount: ")

# Write record to file
f.write(f"Product: {product}, Quantity: {quantity}, Total Sales: {total_sales}\n")

# Close the file
f.close()

print("Sales record added successfully.")