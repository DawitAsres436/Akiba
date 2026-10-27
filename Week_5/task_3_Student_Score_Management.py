class Student:
    School_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Department: {self.department}")

student1 = Student("Abebe Kebede", 85, "Computer Science")
student2 = Student("Selam Tesfaye", 92, "Electrical Engineering")
student3 = Student("Daniel Alemu", 78, "Mathematics")

print("----Before Update----")
student1.display()
student2.display()
student3.display()

student1.score = 90

print("\n----After Update----")
student1.display()
student2.display()
student3.display()