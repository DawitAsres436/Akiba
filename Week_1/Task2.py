student_name = input("Enter your name: ")
student_ID = input("Enter your ID: ")
department = input("Enter your department: ")
year = int(input("Enter your academic year: "))
university = input("Enter your University: ")
phone_number = input("Enter your phone number: ")

line = "-"*30
print(f"+{line}+\n|{'AKIBA STUDENT CARD':^30}|\n+{line}+")
print(f"|{'Name:':<15}{student_name:<15}|\n|{'ID:':<15}{student_ID:<15}|\n|{'Department:':<15}{department:<15}|\n|{'Year:':<15}{year:<15}|\n|{'University:':<15}{university:<15}|\n|{'Phone:':<15}{phone_number:<15}|")
print(f"+{line}+")