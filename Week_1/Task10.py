# BMI Health Information 
name = input("Enter your name: ")
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in meter: "))

double_line = "====================================="

bmi = weight/height**2

print(f"{double_line}\n{' BMI REPORT':^25}\n{double_line}\n\nName:  {name}\nWeight: {weight}Kg\nHeight: {height}\n\nBMI:   {bmi}\n{double_line}")
