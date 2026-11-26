# Creating a dictionary
student = {
    "Registration Number": "BIT2024/001",
    "Student Name": "Rose Waithira",
    "Course": "Bachelor of Information Technology",
    "Year of Study": 2
}

# Display student's name and course
print("Student Name:", student["Student Name"])
print("Course:", student["Course"])

# Change the year of study
student["Year of Study"] = 3

# Add email address
student["Email"] = "rose@example.com"

# Display updated dictionary
print("\nUpdated Student Record:")
print(student)