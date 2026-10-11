# PALINDROME WORD CHECKER

word = input("Enter the word: ")

if word == word[::-1]:
    print(f"The word {word} is palindrome")
else:
    print(f"The word {word} is not palindrome")