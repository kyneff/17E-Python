print("Hello!")
name = input("What is your name? ")
print(f"Greetings, {name}")
print("This is a basic calculator that adds, subtracts, multiplies, and divides.")
numFirst = float(input("First number? "))
numSecond = float(input("Second number? "))
sum = numFirst + numSecond
dif = numFirst - numSecond
prod = numFirst * numSecond
quot = numFirst / numSecond
print(f"The sum is {sum}.")
print(f"The difference is {dif}.")
print(f"The product is {prod}.")
print(f"The quotient is {quot:.4f}.")
print("Now, we are going to convert distance from km to m.")
distance = float(input("How many kilometers? "))
print(f"In meters, that would be {distance * 1000}m.")
print("Have a good day!")