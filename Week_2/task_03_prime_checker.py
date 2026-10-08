# Check whether the number is prime
number = int(input("Enter number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime number")
            break
    else:
        print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")