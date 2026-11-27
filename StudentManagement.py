# Student Management Class

class Student:
    def __init__(self):
        self.name = ""
        self.reg_number = ""
        self.course = ""
        self.mark = 0
        self.grade = ""

    def setStudentDetails(self, name, reg_number, course, mark):
        self.name = name
        self.reg_number = reg_number
        self.course = course
        self.mark = mark

    def calculateGrade(self):
        if 70 <= self.mark <= 100:
            self.grade = "A"
        elif 60 <= self.mark <= 69:
            self.grade = "B"
        elif 50 <= self.mark <= 59:
            self.grade = "C"
        elif 40 <= self.mark <= 49:
            self.grade = "D"
        else:
            self.grade = "F"

    def displayStudentDetails(self):
        print("Student Name:", self.name)
        print("Registration Number:", self.reg_number)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.grade)


# Main Program
student = Student()

student.setStudentDetails(
    "Rose Kamau",
    "BIT/2024/001",
    "Bachelor of Information Technology",
    75
)

student.calculateGrade()
student.displayStudentDetails()
