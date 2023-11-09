## 1
# colors = ["red", "orange", "yellow"]
# for color in colors:
#     print("Here is a color that I know:")
#     print(color)
#     print()
# print("\nThe for-loop has ended.")

## 3
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Hello {name}. Welcome to the Python course.")

## 4
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Have a good day, {name}. I hope you enjoyed experimenting with python.")

## 5
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print()

## 6
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print(f"5 years ago, that person was {age - 5} years old.")
#     print()

## 7
# For each of the following numbers, display "Half of __ is ___". For example, "Half of 21 is 10.5"
# numbers = [21, 40, 32, 10, 8, 3]
# for number in numbers:
#     print(f"Half of {number} is {number / 2}.")

## 8
# for num in range(1,5):
#     print(num)

## 9
# for num in range(1,7):
#     print(num)

# 10
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")

## 11
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 90:
#         print("That's hot.")

## 12
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 32:
#         print("That's above freezing.")
#     else:
#         print("That's below freezing.")

## 12b
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print("Looking at the temperatures.")
#     print(f"One of the temperatures in the list is {temp}")
#     if temp > 90:
#         print("That's hot.")

## 13
# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# print("That's all I have to say.")

## 14
# x = input("Say a word: ")
# if x.endswith("day"):
#     print("I think that's a day of the week.")
# print("That's all I have to say.")

## 15
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# berryCount = 0
# for fr in fruits:
#     if fr.endswith("berry"):
#         berryCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {berryCount} that ended with berry.")

## 16
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# mCount = 0
# for fr in fruits:
#     if fr.startswith("m"):
#         mCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {mCount} that started with 'm'.")

## 17
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]
# aboveF = 0
# for temp in temps_in_F:
#     if temp > 32:
#         aboveF += 1
# print(f"There are {aboveF} temperatures above freezing.")

# ## 18
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]
# aboveF = 0
# belowF = 0
# for temp in temps_in_F:
#     if temp > 32:
#         aboveF += 1
#     else:
#         belowF += 1
# print(f"There are {aboveF} temperatures above freezing and {belowF} temperatures below freezing.")

# 20
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for instructor in instructors:
#     name, age, yearsExp = instructor
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 21
# name, color = ["Bob", "Green"]
# print(f"{name} likes the color {color}")

## 22
# personinfo = ["Bob", "Green"]
# name, color = personinfo
# print(f"{name} likes the color {color}")

## 23
# personinfo = ["Bob", "Green", 20]
# name, color, age = personinfo
# print(f"{name} is {age} years old, and likes the color {color}")

## 25
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for instructor in instructors:
#     name, age, yearsExp = instructor
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 26
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 27
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} is {age} years old, and started working at age {age - yearsExp}.")

## 28
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} has been working for {yearsExp} years, and will receive a ${yearsExp * 10} bonus this year.")

## 29
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# bonus = int(input("What is the bonus per year of experience? "))
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} has been working for {yearsExp} years, and will receive a ${yearsExp * bonus} bonus this year.")

## 30
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# totalYearsExp = 0
# for name, age, yearsExp in instructors:
#     totalYearsExp += yearsExp
# print(f"The total amount of work experience for this team is {totalYearsExp}.")

## 31
# runners = [
#     ["James", 5, 60],
#     ["Tom", 1, 7],
#     ["Steve", 2, 22],
#     ["Carson", 2, 12]
# ]
# for name, miles, minutes in runners:
#     print(f"{name} ran {miles} miles in {minutes} minutes.")
#     print(f"That means {name} took an average of {minutes / miles} minutes to run each mile.")

## 32
# phrase = "Hello world"
# for letter in phrase:
#     print(f"The letter is {letter}")

## 33
# word = input("Input a word: ")
# for letter in word:
#     print(f"The letter is {letter}")

## 34
# word = input("Input a word: ")
# for letter in word:
#     print(f"{letter}!")

## 35
# for num in range(1,6):
#     print(num ** 2)

## 36
# max = int(input("Input a number for the highest range: "))
# for num in range(1,max+1):
#     print(num ** 2)

## 37
# for num in range(1,13):
#     print(f"{num} divided by 4 would have a remainder of {num % 4}")

## 38
# print("Hello"*3)

## 39
# count = int(input("How many times would you like to print Hello? "))
# print("Hello"*count)

## 40
# howmany = int(input("How many rows would you like? "))
# for i in range(howmany):
#     print("AAAAA")

## 41
# howmany = int(input("How many rows would you like? "))
# for i in range(howmany):
#     print(f"{i+1} A")

## 42
# rows = int(input("How many rows should be printed? "))
# for i in range(rows):
#     print(f"{i+1} times A is {"A"*(i+1)}")

## 43
# rows = int(input("How many rows should be printed? "))
# for i in range(rows):
#     print("A"*(i+1))

## 44
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# base_pay = 35000
# pay_adjustment = 1000
# for name, age, yearsExp in instructors:
#     pay_level = yearsExp // 5
#     salary = base_pay + (pay_adjustment * pay_level)
#     print(f"{name}: {yearsExp} years of experience, ${salary} per year.")

## 45
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# base_pay = int(input("What is the base pay? "))
# pay_adjustment = int(input("What is the pay adjustment per 5 years of experience? "))
# for name, age, yearsExp in instructors:
#     pay_level = yearsExp // 5
#     salary = base_pay + (pay_adjustment * pay_level)
#     print(f"{name}: {yearsExp} years of experience, ${salary} per year.")

# 46
# Try this. It shows how to use `enumerate`.
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for indx, elem in enumerate(names):
#     print(f"The index is {indx} and the element is {elem}")

# 47
# word = "Hello"
# for indx, letter in enumerate(word):
#     print(f"{indx}: {letter}!")

## 48
freqs = [2403.6, 101.3, 90.1, 5.2, 2410.2, 3.7]
# Using a loop, print each frequency, and then print whether it is
# in the Wi-Fi range, the FM Radio range, or Neither Wi-Fi nor FM.

# 49
# Modify the previous example to count how many frequencies were in each category.
# At the end of the program, print the count for each category.

# 50
# A report is being produced which only shows detected Wi-Fi frequencies.
# Make a copy of the previous program that only prints the Wi-Fi frequencies from the list.


# 51
# After having read the report, someone wants to know where in the list that the Wi-Fi
# frequencies occur. Make a program that prints both Wi-Fi frequencies and their indices.
# You'll most likely want to use the enumerate function.

# Expected output:
# 2403.6 MHz: index 0
# 2410.2 MHz: index 4


# 52
# Some of the audience of the report is unfamiliar with MHz.
# Modify one (any one) of the above spectrum-related questions
# to allow the user to choose if they want to see the results in MHz or GHz.
# Then print the frequencies using the chosen unit.


# 53
# Someone now wants a program to convert between MHz and GHz.
# The person wants to be able to type everything in one prompt, for example,

#   What would you like to convert? 3445 MHz
#   That is 3.445 GHz.

# Convert appropriately from MHz to GHz or vice versa using input from a single prompt.
# Note 1: the following exercise provides a useful hint.
# Note 2: You can assume the user enters valid data, or, for a challenge, check for data validity.


# 54
# Try this:
# userdata = input("Enter two numbers, separated by a space.")
# a, b = userdata.split()
# print(f"First number: {a} and second number: {b}")