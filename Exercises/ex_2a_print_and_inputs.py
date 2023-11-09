# 1
# print("Here we go!")

# 1b
# print("I can print")
# print("more than one line.")

# 2a
# print("If you want \n separate lines, you \n can also do it \n like this.")

# 2b
# print("This thing inside quotes is called a \"string\". If you want")
# print("to put quotes inside of quotes, you precede the quotes with a backslash.")

# 2c
# print("""If you put three quote marks, 
# you can easily enter a
# multi-line
# string.""")

# 2d
"""If I wanted to write a long explanation,
I could write it like this
instead of using the '#' if I wanted to."""

# 2e
# print('In Python, the single quote can be used instead of the double quote.')
# print("You can put 'single quotes' inside of double quotes, or vice versa, without needing an escape sequence.")
# print('However, if you want single quotes inside of single quotes, you\'ll need to escape them.')

# 3a
# firstn = "Bob"
# lastn = "Smith"
# print(firstn)

# 3b
# firstn = "Bob"
# lastn = "Smith"
# print(firstn, lastn)

# 4a
# firstn = "Bob"
# lastn = "Smith"
# print(f"My name is {firstn} {lastn}")

# 4b
# firstn = "Bob"
# lastn = "Smith"
# print("My name is", firstn, lastn)

# 4c
# print("Hello!")
# cartype = input("Type the name of a car, then press enter: ")
# print(f"The car you named is {cartype}. That was a good choice.")

# 4d
# print("Hello!")
# cartype = input("Type the name of a car, then press enter: ")
# print(f"The car you named is {cartype}. Do you have one?")

# 4e
# print("Hello!")
# cartype = input("Type the name of an animal, then press enter: ")
# print(f"The animal you named is {cartype}. I think that it would make a nice pet.")

# 5
# firstn = input("Please enter a first name? ")
# lastn = "Smith"
# print(f"Maybe someone is named: {firstn} {lastn}.")

# 6a
# firstn = input("Please enter a first name? ")
# lastn = input("Please enter a last name? ")
# print(f"Your name is {firstn} {lastn}.")

# 6b
# firstn = input("Please enter a first name? ")
# middlen = input("Please enter a middle name? ")
# lastn = input("Please enter a last name? ")
# print(f"Your name is {firstn} {middlen} {lastn}.")

# 7
# color = input("Please name a color? ")
# print(f"{color} is a pretty color.")

# 8
# animal = input("Please enter an animal? ")
# plant = input("Please enter a plant? ")
# print(f"The {animal} eats {plant} every day.")

# 9a
# a = "Hello"
# b = "Goodbye"
# c = a + b
# print(c)

# 9b
# mysentence = "Hello" + "everyone"
# print(mysentence)

# 9c
# mysentence = "Hello" + " " + "everyone"
# print(mysentence)

# 10
# a = input("First word? ")
# b = input("Second word? ")
# c = a + b
# print(c)

# 11
# a = 5
# b = 3
# c = a + b
# print(c)

# 12
# a = "5"
# b = "3"
# c = a + b
# print(c)

# 13
# print("Welcome to the number adder that doesn't work right!")
# a = input("What's a number you like? ")
# b = input("Can you give me another number you like? ")
# c = a + b
# print("I added them. Here's what I got...")
# print(c)

# 14
# print("Welcome to the number adder that works well!")
# a = int(input("What's a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

# 15
# a = int(input("What is a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

# 16
# favnum = int(input("What is your favorite number? "))
# onemore = favnum + 1
# print(f"One more would be {onemore}")

# 17
# num = int(input("Please enter an integer? "))
# twoMore = num + 2
# print(f"That number plus 2 is {twoMore}.")

# 18
# numOne = int(input("Enter your first number: "))
# numTwo = int(input("Enter your second number: "))
# sum = numOne + numTwo
# print(f"The sum of your two numbers is {sum}.")

# 19
# numOne = int(input("Enter your first number: "))
# numTwo = int(input("Enter your second number: "))
# diff = numOne - numTwo
# print(f"The first number minus the second number is {diff}.")

# 20
# num = int(input("Enter a number: "))
# half = num / 2
# print(f"Half of that number is {half}.")

# 21a
# print("Hello"*3)

# 21b
# word = input("Enter a word: ")
# print(word * 3)

# 22a
# print("Hello" * "3")

# 22b
# word = input("Enter a word: ")
# num = int(input("Enter a number for the repetition count: "))
# print(word * num)

# 23
# num = int(input("Give me a number. "))
# print("I'm going to try to multiply that number by 5,")
# print("but something strange is going to happen:")
# print(num * 5)

# 24
# total = int(input("How many total questions were on the test? "))
# right = int(input("How many questions did you get right? "))
# percent = right * 100 / total
# print(f"You got {percent}% right.")

# 25
# name = input("What is your name? ")
# age = int(input("What is your age? "))
# ageTwo = age + 2
# print(f"Guess what, {name}, in two years you'll be {ageTwo}.")

# 26
# x = 123
# y = "123"
# print(x*3)
# print(y*3)

# 27
# x = input("Enter a word. ")
# y = int(input("Enter a number. "))
# print(f"The type of x is {type(x)}, which is another way to say 'string'.")
# print(f"The type of y is {type(y)}, which is another way to say 'integer'.")
# print(x*y)

# 28a
# mystery = 6
# another = "Hello"
# something = input("Enter a number. ")
# whatIsThis = int(input("Enter a number. "))
# thisIsSomething = 3.1
# print(f"The type of mystery is {type(mystery)}.")
# print(f"The type of another is {type(another)}.")
# print(f"The type of something is {type(something)}.")
# print(f"The type of whatIsThis is {type(whatIsThis)}.")
# print(f"The type of thisIsSomething is {type(thisIsSomething)}.")

# 28b
# somenum = int(input("Try typing a non-whole number, such as an approximate value for pi. You'll see that it doesn't work: "))
# print(f"You typed {somenum}")

# 28c
# somenum = float(input("Try typing another non-whole number: "))
# print(f"You typed {somenum}")

# 28d
# numOne = float(input("Enter a number: "))
# numTwo = float(input("Enter a second number: "))
# sum = numOne + numTwo
# print(f"The sum of your two numbers is {sum}.")

# 28e
# num = float(input("Enter a number: "))
# twice = num * 2
# print(f"Twice that number is {twice}.")

# 28f
# name = input("What is your name? ")
# age = float(input("What is your age? "))
# ageTwo = age + 2
# print(f"Guess what, {name}, in two years you'll be {ageTwo}.")

# 29
# x = "hello"
# y = "goodbye"
# print(x*y)

# 30
# x = "3"
# y = "5"
# print(x*y)