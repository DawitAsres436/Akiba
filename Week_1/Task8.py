Stu_name = input("Enter student name: ")
python = int(input("ENter the python score: "))
English = int(input("ENter the English score: "))
Maths = int(input("ENter the Mathematics score: "))

double_line = "========================================="
single_line = "------------------------------------"

Average = (python + English + Maths)/3

print(f"{double_line}\n{'STUDENT RESULT':^25}\n{double_line}\n\n{'Student: ':<15}{Stu_name}\n\n{'Python: ':<15}{python}\n{'English: ':<15}{English}\n{'Mathematics: ':<15}{Maths}\n{single_line}\n{'Average: ':<15}{Average}\n{double_line}")
