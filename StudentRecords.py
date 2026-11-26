f = open("students.txt", "w")

# Write student records to the file
print("Name: Rose Waithira", file=f)
print("Registration Number: BIT2024/001", file=f)
print("Course: Bachelor of Information Technology", file=f)
print("Mark: 85\n", file=f)

print("Name: John Mwangi", file=f)
print("Registration Number: BIT2024/002", file=f)
print("Course: Computer Science", file=f)
print("Mark: 78\n", file=f)

print("Name: Mary Wanjiku", file=f)
print("Registration Number: BIT2024/003", file=f)
print("Course: Software Engineering", file=f)
print("Mark: 90\n", file=f)

# Close the file
f.close()

print("Student records saved successfully.")