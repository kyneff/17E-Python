# Valid variable names -- These are examples of valid variable assignment statements:
mynumber = 7
temp_in_f = 8.3
my2ndthing = "hi"
x3 = "stuff"
_myStuff = 7
result = mynumber * _myStuff

# This definition of a variable is valid, but please don't, because "input" will no longer be a function.
input = 7

print(mynumber)
print(f"The recorded temperature is {temp_in_f}°F")
print(f"The following message was received '{my2ndthing}'.")
print(f"The result of multiplying", mynumber, "and", _myStuff, "is equal to", result)