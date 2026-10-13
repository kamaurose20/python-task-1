# Create variables
employee_name = ""
employee_id = ""
employee_age = 0
basic_salary = 0.0

# Accept input
employee_name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
employee_age = input("Enter Employee Age: ")
basic_salary = input("Enter Basic Salary: ")

# Convert data types
employee_age = int(employee_age)
basic_salary = float(basic_salary)

# Calculate annual salary
annual_salary = basic_salary * 12

# Display results
print("\n===== Employee Details =====")
print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Employee Age: {employee_age}")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Annual Salary: {annual_salary:.2f}")