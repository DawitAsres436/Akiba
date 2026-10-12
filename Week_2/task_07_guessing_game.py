# Number gussing game
# Import the random module to generate a random number
import random

# Generate a secret number between 1 and 100 
secret_number = random.randint(1,100)
# Initialize the number of attempts used and set maximum attempt
attempt= 0
max_attempt = 5
line = "="*30

print(f"{line}\nNUMBER GUSSING GAME\n{line}")
print(f"I'm thinking a number between 1-100. You have {max_attempt} attempts\n")

# While loop to check the users input vs the secret number
while attempt < max_attempt:
# Ask the player to enter a guess
    guess = int(input(f"Enter your guess ({attempt+1}/{max_attempt}):"))
    if guess == secret_number:
        print(f"Congratulations!\nYou guessed the number in {attempt+1}/{max_attempt} attempts.")
        break
    elif guess < secret_number:
        print("Higer\n")
    elif guess > secret_number:
            print("Lower\n")
    attempt+=1
# This runs only if the player uses all attempts without guessing correctly
else:
    print("Game Over!")
    