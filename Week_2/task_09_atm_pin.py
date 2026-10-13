# ATM PIN verification program

correct_PIN = 1234
attempt = 1
line = "="*40
print(f"{line}\n{'ATM PIN verification program':^40}\n{line}")

while attempt <= 3:
    user_PIN = int(input("Enter your PIN: "))
    if user_PIN == correct_PIN:
        print("Congratulations you are corret!")
        break
    else:
        print(f"Incorrect PIN.\nAttempts remaining: {3-attempt}")

    attempt+=1

else:
    print("Your account is locked. Too many incorrect attempts.")
