# Create a list containing five subject marks
marks = [75, 68, 82, 90, 71]

# Display all marks
print("Marks:", marks)

# Calculate and display total marks
total_marks = sum(marks)
print("Total Marks:", total_marks)

# Calculate and display average mark
average_mark = total_marks / len(marks)
print("Average Mark:", average_mark)

# Display highest and lowest marks
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# Modify the third subject mark
marks[2] = 85

# Display updated list
print("Updated Marks:", marks)