# Input
purchase_amount = float(input("Enter the total purchase amount (KSh): "))

# Calculate discount
if purchase_amount >= 10000:
    discount = 0.15 * purchase_amount
else:
    discount = 0.0

# Calculate final amount
final_amount = purchase_amount - discount

# Output
print("\n----- Purchase Summary -----")
print("Purchase Amount: KSh", purchase_amount)
print("Discount: KSh", discount)
print("Final Amount: KSh", final_amount)
