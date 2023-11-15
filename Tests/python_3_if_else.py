print("This is a basic calculator that adds, subtracts, multiplies, and divides.")

numOne = (float(input("First number? ")))
numTwo = (float(input("Second number? ")))
userChoice = (input("Pick an operation. Your choices are 'add', 'subtract', 'multiply', 'divide'. "))

if userChoice == "add":
    print(f"The sum is {numOne + numTwo}.")
elif userChoice == "subtract":
    print(f"The difference is {numOne - numTwo}.")
elif userChoice == "multiply":
    print(f"The product is {numOne * numTwo}.")
elif userChoice == "divide":
    print(f"The quotient is {numOne / numTwo}.")
else:
    print("You did not select a correct operation.")