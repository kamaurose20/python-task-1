# Parent Class
class Employee:
    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id

    def displayEmployee(self):
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)


# Child Class
class Lecturer(Employee):
    def __init__(self, employee_name, employee_id, teaching_subject):
        super().__init__(employee_name, employee_id)
        self.teaching_subject = teaching_subject

    def displayLecturer(self):
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Teaching Subject:", self.teaching_subject)


# Main Program
lecturer = Lecturer("John Kamau", "EMP001", "Python Programming")

lecturer.displayLecturer()