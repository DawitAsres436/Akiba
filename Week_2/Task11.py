# EVEN OR ODD

Number = int(input("Enter number: "))

if Number %2 == 0:
    if Number > 0:
        print(f"The number {Number} is positive even number")
    elif Number == 0:
        print(f"The number {Number} is even (Zero)")
    else:
        print(f"The number {Number} is negative even number")
else:
    if Number > 0:
        print(f"The number {Number} is positive odd number")
    else:
        print(f"The number {Number} is negative odd number")