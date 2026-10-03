Emp_name = input("Enter the employee's name: ")
Base_salary = float(input("Enter employee's Base Salary: "))
Transport_allowance = float(input("Enter employee's Transport allowance: "))
Food_allowance = float(input("Enter Employee's food allowance: "))

DoubleLine = "===================================="
line = "----------------------"

Gross_salary = Base_salary + Transport_allowance + Food_allowance

print(f"{DoubleLine}\n{'EMPLOYEE PAYSLIP':^30}\n{DoubleLine}\n\nEmployee: {Emp_name}\n")
print(f"{'Basic Salary: ':<25}{Base_salary}ETB\n{'Transport Allowance: ':<25}{Transport_allowance}ETB\n{'Food Allowance: ':<25}{Food_allowance}ETB\n{line}\n{'Gross Salary: ':<25}{Gross_salary}")
print(f"{DoubleLine}")