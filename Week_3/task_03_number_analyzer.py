number = int(input("Enter number: ")) 

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True
               

def get_divisors(number):
    divisor = []

    if number == 0:
        return divisor

    for i in range(1, number+1):
        if number % i == 0:
            divisor.append(i)
    return divisor


def sum_of_digits(number):
    sum_of_digit = 0
    for i in range(len(str(number))):
        last_digit = number % 10
        sum_of_digit += last_digit
        number = number // 10
    return sum_of_digit

def reverse_number(number):
    reverse = str(number)
    reverse = reverse[::-1]
    return reverse

def analyze_number(number):
    if number % 2 == 0:
        even_or_odd = "Even"
    else:
        even_or_odd = "Odd"

    return {
        "number": number,
        "even_or_odd": even_or_odd,
        "prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed": reverse_number(number),
        "divisors": get_divisors(number)
    }

result = analyze_number(number)

print("\n========== NUMBER ANALYSIS ==========")
print(f"Number: {result['number']}")
print(f"Even or Odd: {result['even_or_odd']}")
print(f"Prime: {result['prime']}")
print(f"Sum of digits: {result['sum_of_digits']}")
print(f"Reversed: {result['reversed']}")
print(f"Divisors: {result['divisors']}")
print("=====================================")

