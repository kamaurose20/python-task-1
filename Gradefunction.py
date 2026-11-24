# Function to calculate grade
def calculate_grade(mark):
    if 70 <= mark <= 100:
        return "A"
    elif 60 <= mark <= 69:
        return "B"
    elif 50 <= mark <= 59:
        return "C"
    elif 40 <= mark <= 49:
        return "D"
    else:
        return "F"

# Input from user
mark = int(input("Enter student mark: "))

# Call function
grade = calculate_grade(mark)

# Display result
print("Grade:", grade)