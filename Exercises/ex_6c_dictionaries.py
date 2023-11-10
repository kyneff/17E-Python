## 1
# print("If you want to put everything", end="")
# print("on one line, then you can", end="")
# print("use this.")

## 2
# mypersondata = {
#   "firstname": "Bob",
#   "lastname": "Smith",
#   "age": 23
# }
# print(mypersondata["firstname"])

## 3
# mypersondata = {
#   "firstname": "Bob",
#   "lastname": "Smith",
#   "age": 23
# }
# print(mypersondata["lastname"])

## 4
# mypersondata = {
#   "firstname": "Bob",
#   "lastname": "Smith",
#   "age": 23
# }
# print(f'Do you know {mypersondata["firstname"]} ...?')

## 5
# mypersondata = {
#   "firstname": "Bob",
#   "lastname": "Smith",
#   "age": 23
# }
# print(f'Did you know that {mypersondata["firstname"]} {mypersondata["lastname"]} is {mypersondata["age"]} years old?')

## 6
# namelocation = {
#   "Sophia": "Greece",
#   "Mario": "Italy",
#   "Jaques": "France"
# }

# for name in namelocation:
#     print(name)
#     print("is from")
#     print(namelocation[name])
#     print()
    

## 7
# namelocation = {
#   "Sophia": "Greece",
#   "Mario": "Italy",
#   "Jaques": "France"
# }

# print("These people are from Greece:")
# for name in namelocation:
#     if namelocation[name] == "Greece":
#         print(name)
    
## Alternate approach:
# for name, loc in namelocation.items():
#     if loc == "Greece":
#         print(name)