## 1
# count = 10
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")

## 2
# count = int(input("Enter a number: "))
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")

## 3
# count = 3
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print("Reached zero. Proof:")
# print(count)

## 4
# count = 3
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

## 5
# count = int(input("Enter a number: "))
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

## 6
# count = int(input("Enter a number: "))
# while count > 0:
#     print(f"Launch in {count}")
#     count -= 1
# print("Liftoff!")

## 7
# import time
# print("Start...")
# time.sleep(1)
# print("Done.")

## 8
# import time
# userInput = int(input("Enter a number: "))
# print("Start...")
# time.sleep(userInput)
# print("Done.")

## 9
# import time
# count = int(input("Enter a number: "))
# while count > 0:
#     print(f"Launch in {count}")
#     count -= 1
#     time.sleep(1)
# print("Liftoff!")

## 10
# keepGoing = "yes"
# while keepGoing == "yes":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")


## 11
# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")

## 12
# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")


## 13
# keepGoing = "yes"
# while keepGoing in ["yes", "y"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")


## 14
# keepGoing = "yes"
# while keepGoing not in ["no", "no thanks"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")


## 15
# keepGoing = "yes"
# while keepGoing in ["hey", "woo", "yes"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

## 16
# keepGoing = "yes"
# while keepGoing != "no":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

## 17
# keepGoing = "yes"
# while keepGoing.lower() not in ["done", "quit", "exit"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

## 18
# count = 0
# keepGoing = "yes"
# while keepGoing != "quit":
#     print(f"The counter is currently {count}.")
#     keepGoing = input("Would you like to add one, subtract one, or quit? ")
#     if keepGoing == "add one":
#         count += 1
#     elif keepGoing == "subtract one":
#         count -= 1
#     else:
#         print(f"Your finally tally is {count}.")
# print("Thanks for using my counter program!")

## 19
# print("Welcome to the word guesser!")
# secretWord = "water"
# guess = ""
# while guess != secretWord:
#     guess = input("What is your guess? ")
# print("You got it!")

## 20
# print("Welcome to the word guesser!")
# secretWord = "water"
# guess = ""
# while guess != secretWord:
#     guess = input("What is your guess? ")
#     print("Let me check to determine whether that's right.")
# print("You got it!")

## 22
# print("Welcome to the number doubler.")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Double your num is {num * 2}.")
# print("Exiting.")

## 23
# print("Welcome to the number squared.")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Your num squared is {num ** 2}.")
# print("Exiting.")

## 24
# print("Welcome to the number doubler.")
# num = int(input("Type a number, or type -1 to quit: "))
# while num != -1:
#     print(f"Double your num is {num * 2}.")
#     num = int(input("Type a number, or type -1 to quit: "))
# print("Exiting.")

## 26
# animal = input("Name an animal, or say 'moose' to exit: ")
# while animal != "moose":
#     sound = input("Name the sound the animal makes: ")
#     print(f"The {animal} says {sound}.")
#     animal = input("Name an animal, or say 'moose' to exit: ")
# print("Moose out.")

## 27
# animal = input("Name an animal: ")
# sound = input("Name the sound the animal makes: ")
# while animal != "moose" or sound != "meow":
#     print(f"The {animal} says {sound}.")
#     animal = input("Name an animal: ")
#     sound = input("Name the sound the animal makes: ")
# print("Moose out.")

## 28    
## Have you ever played the game Duck Duck Goose?
# import random
# import time

# print("This is a Duck, Duck, Goose Simulator. Have fun!!!!!")
# choices = ["Goose",
#               "Duck",
#               "Duck",
#               "Duck"]
# one_choice = random.choice(choices)
# while one_choice != "Goose":
#     print(f"{one_choice}...")
#     one_choice = random.choice(choices)
# print("Goose!")  


## 29
# import random

# print("Welcome to the word guesser!")
# secretWord = "water"
# guess = input("What is your guess? ")
# choices = ["Not yet, try again.",
#               "I bet you'll get it, keep trying!",
#               "That's not it.",
#               "I appreciate your patience, but you haven't guessed it yet."]
# while guess.lower() != secretWord:
#     one_choice = random.choice(choices)
#     print(f"{one_choice}")
#     guess = input("What is your guess? ")
# print("You got it!")

## 29b
# names_starting_with_c = []
# name = input("Enter a name, or q to quit: ")
# while name != "q":
#     if name.lower()[0] == "c":
#         names_starting_with_c.append(name)
#     name = input("Enter a name, or q to quit: ")
# print(f"These names start with the letter c: {names_starting_with_c}")

## 30
# import random

# randomNumber = random.randint(20,100)
# guess = int(input(f"If you divided {randomNumber} by 12, what would be the remainder? "))
# while guess != randomNumber % 12:
#     guess = int(input(f"Guess: "))
# print("You got it!")

## 31
# print("This is a grade tracking helper.")
# f = open("physics_grades.csv", "w")
# f.write("StudentName,StudentGrade\n")
# questionsTotal = float(input("What is the total number of questions for this assignment? "))
# name = input("What is the student name? (Press enter with no name to exit.) ")
# while name != "":
#     questionsCorrect = float(input("How many questions did that student answer correctly? "))
#     questionsPercent = questionsCorrect * 100 / questionsTotal
#     print(f"{questionsPercent:.2f}%")
#     f.write(f"{name},{questionsPercent:.2f}\n")
#     name = input("What is the student name? (Press enter with no name to exit.) ")
# f.close()
# print("Exiting...")