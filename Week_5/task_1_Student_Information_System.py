class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

student1 = Student("Abebe Kebede", 24, "BAIS")
student2 = Student("Sara", 21, "Electrical Engineering")
student3 = Student("Mastewal Getu", 22, "SC" )

student1.display_info()
student2.display_info()
student3.display_info()


