"""
Listing the numbers between 1 and 100 and if the number is multiple of 3 FIZZ
 abd if multiple of 5 BUZZ both FIZZBUZZ
"""

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FIZZBUZZ")
    elif i%5 == 0:
        print("BUZZ")
    elif i%3 == 0:
        print("FIZZ")
    else:
        print(i)