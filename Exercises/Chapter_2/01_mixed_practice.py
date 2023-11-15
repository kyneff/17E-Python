## 1 Word Guessing Game
# from termcolor import cprint

# secretWord = "water"
# count = 0

# print("Welcome to the word guesser!")
# guess = input("What is your guess? ")

# while guess.lower() != secretWord:
#     count += 1
#     if count % 3 == 0:
#         cprint(f"Three strikes, you're out! Just kidding, you can keep guessing. That's {count} guesses so far.", "white", "on_red")
#     else:
#         print(f"Try again! You have made {count} guesses.")
#     guess = input("What is your guess? ")

# cprint(f"You got it! It took {count+1} guesses.", "green", "on_blue")

## 2 Number Guessing Game
# secretNumber = 15

# print("Welcome to the number guesser!")
# guess = int(input("What is your guess? "))

# while guess != secretNumber:
#     if guess < secretNumber:
#         print("Your guess is too low. Guess again. ")
#     else:
#         print("Your guess is too high. Guess again.")
#     guess = int(input("What is your guess? "))
# print("You got it!")

## 3 Data File
# f = open("original_names.txt", "w")
# f.write("Bob Smith\n")
# f.write("Alley Cat\n")
# f.write("Mona Jones\n")
# f.close()

## 4 Add more names.
# f = open("original_names.txt", "a")
# f.write("Big Dog\n")
# f.write("Super Man\n")
# f.write("Bone Man\n")
# f.close()

## 5
# f = open("original_names.txt", "r")
# lines = f.read().splitlines()
# for line in lines:
#     username = line.split()
#     print(f"{username[0]} {username[1]}'s username is {username[0][0].lower() + username[1].lower()}.")