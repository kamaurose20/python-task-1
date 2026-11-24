name = input("Enter student name: ")
mark = int(input("Enter examination mark: "))

# Check for valid mark and assign grade
if mark < 0 or mark > 100:
    grade = "Invalid mark"
elif mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 40:
    grade = "D"
else:
    grade = "F"

# Display the student's name, mark, and grade
print("\nStudent Details")
print("Name:", name)
print("Mark:", mark)
print("Grade:", grade)