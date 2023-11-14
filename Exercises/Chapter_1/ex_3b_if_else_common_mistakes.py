## 1
# guess = input("Guess one of my words: ")
# if guess == "water" or guess == "food":
#     print("You were right.")
# else:
#     print("Sorry, not right.")

## 2 Intentionally incorrect.
# guess = input("Guess one of my words: ")
# if guess == "water" or "food":
#     print("You were right.")
# else:
#     print("Sorry, not right.")

## 4
# The user's name is never assigned to a variable and the if statement runs regardless of the user answer.
# input("What is your name? ")
# if "Bob":
#     print("Hello Robert.")

## 5
# The if statement runs regardless of the user answer.
# name = input("What is your name? ")
# if "Bob":
#     print("Hello Robert.")

## 6
# The user choice isn't assigned to a variable. The if statement should use a variable instead of input.
# input("What is your name? ")
# if input == "Bob":
#     print("Hello Robert.")

## 7
# The variable name is instructed to print the input immediately. The if statement is never instructed to run.
# name = print(input("What is your name? "))
# if name == "Bob":
#     print("Hello Robert.")

## 8
# The input is told to print immediately before the user can type in an answer. The if statement is never instructed to run.
# name = input(print("What is your name? "))
# if name == "Bob":
#     print("Hello Robert.")

## 9
# Both if statements run regardless of the user choice.
# first = int(input("Give me a number. "))
# operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.")
# double = first * 2
# half = first / 2
# if double:
#     print(f"Ok, double your number is {double}.")
# if half:
#     print(f"Ok, half your number is {half}.")

## 10
# The variable operation is requesting a string. The variables double and half are integers resulting in both if statements being ignored.
# first = int(input("Give me a number. "))
# operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.")
# double = first * 2
# half = first / 2
# if operation == double:
#     print(f"Ok, double your number is {double}.")
# if operation == half:
#     print(f"Ok, half your number is {half}.")

## 11
# The age variable needs to be an integer.
# print("You win the game if your age is at least 90.")
# age = input("How old are you? ")
# if age >= 90:
#     print("You win!")
# else:
#     print("You lose.")

## 11b
# The age variable needs to be an integer.
# print("You win the game if your age is exactly 99.")
# age = input("How old are you? ")
# if age == 99:
#     print("You win!")
# else:
#     print("You lose.")

## 12
# The else statements runs every time because the user choice can't be yes and definitely at the same time.
# opinion = input("Do you like celery? ")
# if opinion == "yes" and opinion == "definitely":
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

## 13
# Using "or" results in the if statement never being false.
# response = input("There are two correct words you can guess. ")
# if response != "marker" or response != "board":
#     print("Not correct. Try again.")
# else:
#     print("You guessed it!")

## 13b
# name.lower is missing ().
# name = input("What is your name? ")
# if name.lower == "bob":
#     print("Hey Bobby!")
# else:
#     print("Hello, good to meet you.")

## 13c
# "Bob" must be lower case.
# name = input("What is your name? ")
# if name.lower() == "Bob":
#     print("Hey Bobby!")
# else:
#     print("Hello, good to meet you.")

## 14
# The like variable is assigned an answer regardless of the user answer resulting in the if statement running every time.
# opinion = input("Do you like celery? ")
# like = ["yes", "Yes", "YES"]
# if like:
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

## 15
# == compares the variable to the whole list instead of each item in the list. Change == to in.
# opinion = input("Do you like celery? ")
# like = ["yes", "Yes", "YES"]
# if opinion == like:
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

## 16
# == must be changed to in. Otherwise it's comparing the whole list instead of each item in the list.
# opinion = input("Do you like celery? ")
# if opinion == ["yes", "Yes", "YES"]:
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")