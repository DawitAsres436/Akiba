# SUM OF DIGITS using while loop

number = int(input("Enter number: "))

original_number = number
sum = 0
while number > 0:
    dig = number%10
    sum= sum + dig
    number = number //10
print(f"The sum of digits on number {original_number} is {sum}.")