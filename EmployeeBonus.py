# Ask the employee to enter details
name = input("Enter employee name: ")
years_of_service = int(input("Enter years of service: "))
performance_rating = int(input("Enter performance rating (1-5): "))

# Check eligibility using logical operators
if years_of_service >= 3 and performance_rating >= 4:
    result = "Employee qualifies for a bonus"
else:
    result = "Employee does not qualify for a bonus"

# Display employee details and result
print("\nEmployee Details")
print("Name:", name)
print("Years of Service:", years_of_service)
print("Performance Rating:", performance_rating)
print("Eligibility:", result)