# Create a set with duplicate categories
categories = {
    "Electronics",
    "Clothing",
    "Furniture",
    "Groceries",
    "Books",
    "Electronics",  # Duplicate
    "Books"         # Duplicate
}

# Display the set
print("Product Categories:", categories)

# Add a new category
categories.add("Sports")

# Remove a category
categories.remove("Furniture")

# Display the final set
print("Final Product Categories:", categories)

# Explanation
print("\nExplanation:")
print("A set automatically removes duplicate values.")
print("This helps the company maintain unique product categories and prevents repeated entries.")