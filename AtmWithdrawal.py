# Initial account balance
balance = 50000

# Ask customer to enter withdrawal amount
withdrawal = int(input("Enter withdrawal amount (KSh): "))

# Check conditions
if withdrawal <= 0:
    print("Error: Withdrawal amount must be greater than zero.")
elif withdrawal > balance:
    print("Error: Insufficient account balance.")
elif withdrawal % 500 != 0:
    print("Error: Withdrawal amount must be a multiple of KSh 500.")
else:
    balance = balance - withdrawal
    print("Withdrawal successful!")
    print("Remaining balance: KSh", balance)