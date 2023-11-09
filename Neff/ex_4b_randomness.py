import random

## 1
# things = ["dinosaur", "dog", "cat"]
# print(random.choice(things))

## 2
# things = ["car", "plane", "taco", "burrito", "cloud"]
# print(random.choice(things))

## 3
# phrases = ["flying squirrel", "talking dog", "fire tree", "super sonic", "brushing teeth"]
# print(random.choice(phrases))

## 4
# nums = [28, 99, 7]
# oneNum = random.choice(nums)
# print(oneNum)

## 5
# nums = [47, 99, 13, 2, 101]
# oneNum = random.choice(nums)
# print(f"I randomly picked a number, and I got {oneNum}.")

## 6
# nums = [47, 99, 13, 2, 101]
# oneNum = random.choice(nums)
# print(f"I randomly picked a number, and I got {oneNum}.")
# if oneNum > 40:
#     print("It was a big number.")
# else:
#     print("It was not a very big number.")

## 7
# Similar to range.
# num = random.randint(3, 6)
# print(num)

## 8
# score = random.randint(1, 100)
# print(f"You got a {score} on the test.")

## 9
# Random Floating Point Number
# Generates a random floating point number from 0.0 to 1.0
# x = random.random()
# print(x)

## 10
# Random Floating Point Number, modified
# Generates a random number between 0.0 to 1.0, adds 3, and then cuts off at 5 decimal places.
# x = random.random()
# y = x + 3
# print(f"{y:0.5f}")

## 11 Random Floating Point Number of an Arbitrary Size.
x = random.random()
y = float(input("Input a number for a maximum value: "))
z = x * y
print(z)