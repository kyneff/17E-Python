## 1
# The list prints chair because lists start at 0.
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[1])

## 2
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[3])

## 3
# thelist = ["water", "chair", "mug", "mouse"]
# #            -4       -3      -2      -1
# print(thelist[-1])  # This will print "mouse".
# print(thelist[-2])  # This will print "mug".

## 4
# foods = ["Potatoes", "Beef", "Broccoli", "Lemons", "Grapes"]
# #            0          1         2          3        4
# #           -5         -4        -3         -2       -1
# print(foods[1])  # This prints "Beef".
# print(foods[-1])  # This prints "Grapes".

## 5
# foods = ["Potatoes", "Beef", "Broccoli", "Lemons", "Grapes"]
# #            0          1         2          3        4
# #           -5         -4        -3         -2       -1
# print(foods[3])
# print(foods[-2])

## 6
# Omits the last number.
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[0:3])

## 7
# Omits the last number.
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[1:3])

## 8
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[0:4])

## 9
# Starts with the element 1 and lists to the end.
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[1:])

## 10
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[2:])

## 11
# Print the list.
# letters = ["a", "b", "c", "d", "e"]
# letters[0] = "ROCKET"
# print(letters)

## 12
# letters = ["a", "b", "c", "d", "e"]
# letters[3] = "WAVE"
# print(letters)

## 13
# letters = ["a", "b", "c", "d", "e"]
# letters[-2] = "WAVE"
# print(letters)

## 14
# name = "Becky"
# print(name[0])

## 15
# name = "Becky"
# print(name[2])

## 16
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[4][3])

## 17
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[0][4])

## 18
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[-1][-1])

## 19
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# sentence = "Hello to " + names[1] + " and everyone else."
# print(sentence)


## 20
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(f"Hello to {names[1]} and everyone else.")


## 21
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# id_num = 4
# print(f"ID: {id_num} Name: {names[id_num]}")

## 22
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# idNum = int(input("Enter an ID number between 0-4: "))
# print(f"The student with id number {idNum} is named {names[idNum]}.")

## 24
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# newName = input("Enter a name to add to the list: ")
# print(names)
# names.append(newName)
# print(names)

## 26
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# delName = int(input("Enter a number between 0-4 to remove a name from the list. "))
# print(names)
# del names[delName]
# print(names)

## 27 
# A list can be generated using the range() function.
# start = 1
# stop = 10+1
# step = 2
# num_list = list(range(start, stop, step))  
  # range parameters: start #, stop#+1, increment (i.e., the "count by" value)
  # Note: Range always omits the final number, so a "+1" has been added 
  # to shown what the actual stopping number will be.  In this example the stop will occur at 10.
# print(num_list)

## 28
# Modify the previous example to create a list that includes all numbers  
# between 0 and 30 that are divisible by 3.  
# Note: 1, 2, 4, 5 etc. are not divisible by 3.  Do not include them.
# start = 3
# stop = 30+1
# step = 3
# num_list = list(range(start, stop, step)) 
# print(num_list)