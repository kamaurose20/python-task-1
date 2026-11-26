# Creating employees dictionary
employees = {
    "John": 50000,
    "Mary": 45000,
    "Peter": 55000,
    "Susan": 60000,
    "David": 48000
}

# Display all employees and salaries
print("Employee Salary Records:")
for employee, salary in employees.items():
    print(employee, ":", salary)

# Update salary of one employee
employees["Mary"] = 50000

# Add a new employee
employees["Alice"] = 52000

# Calculate total salary payable
total_salary = sum(employees.values())

print("\nUpdated Employee Records:")
for employee, salary in employees.items():
    print(employee, ":", salary)

print("\nTotal Salary Payable =", total_salary)