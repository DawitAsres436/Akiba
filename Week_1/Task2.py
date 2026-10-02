student_name = input("Enter your name: ")
student_ID = input("Enter your ID: ")
department = input("Enter your department: ")
year = int(input("Enter your akademic year: "))
university = input("Enter your University: ")
phone_number = input("Enter your phone number: ")

line = "+--------------------------+"
print(f"{line}\n|    AKIBA STUDENT CARD    |\n{line}")
print(f"|Name: {student_name}               |\n|ID: {student_ID}               |\n|Department: {department}          |\n|Year: {year}                   |\n|University: {university}           |\n|Phone: {phone_number}         |")
print(line)