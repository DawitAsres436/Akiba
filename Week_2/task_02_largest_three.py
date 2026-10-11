# Comparison of three numbers entered by the user

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 == num2 == num3:
    print("All three numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"The number {num1} is the largest number")
elif num2 >= num1 and num2 >=num3:
    print(f"The number {num2} is the largest number")
else:
    print(f"The number {num3} is the largest number")