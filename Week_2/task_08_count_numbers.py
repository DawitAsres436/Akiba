# counting even, odd and total numbers range 1 upto user input
number = int(input("Enter a number: "))

if number <= 0:
    print("Please enter a positive number!")
else:
    even_number = 0
    odd_number = 0
    total = 0

    for num in range (1, number+1):
        total += num
        if num%2==0:
            even_number+=1
        else:
            odd_number+=1
    print(f"In range of 1 to {number} there are {even_number} even numbers and {odd_number} odd numbers.\nAnd the sum of the numbers 1 upto {number} is {total}")