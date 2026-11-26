f = open("customers.txt", "r")

# Read file contents
contents = f.read()

# Display contents
print("Customer Records:")
print(contents)

# Close the file
f.close()