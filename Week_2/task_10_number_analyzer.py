# NUMBER ANALYZER
user_input = input("Enter 10 numbers separated by commas: ")
numbers = [int(num.strip()) for num in user_input.split(",")]

largest_no = numbers[0]
smallest_no = numbers[0]
even_number = 0
odd_number = 0
total = 0

for num in numbers:
    total += num

    if num > largest_no:
        largest_no = num

    if num < smallest_no:
        smallest_no = num

    if num % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

average = total / len(numbers)

print(
    f"The largest number: {largest_no}\nThe smallest number: {smallest_no}\nThe total sum: {total}\n"
    f"The average: {average}\n"
    f"The number of even numbers: {even_number}\n"
    f"The number of odd numbers: {odd_number}"
)