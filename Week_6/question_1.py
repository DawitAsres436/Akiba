class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")

    def introduce(self):
        print(f"I'm {self.name}")

student1 = Student("Abebe Kebede", "Akiba_123", "BAIS")
student2 = Student("Sara", "Akiba_3456", "Electrical Engineering")
student3 = Student("Mastewal Getu", "Akiba_8957", "SC" )

for student in (student1, student2, student3):
    student.display_info()
    print("-" * 20)
    student.introduce()
    print("-" * 30)     

