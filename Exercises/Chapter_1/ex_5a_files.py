## 1 
# f = open("something_very_unique_file.txt", "w")
# f.write("Here are some words.\n")
# f.write("More words.\n")
# f.close()

## 2
# f = open("my_thoughts.txt", "w")
# f.write("This is the first line.\n")
# f.write("This is the second line.\n")
# f.write("This is the third line.\n")
# f.write("This is the fourth line.\n")
# f.write("This is the fifth line.\n")
# f.write("This is the sixth line.\n")
# f.write("This is the seventh line.\n")
# f.write("This is the eighth line.\n")
# f.write("This is the ninth line.\n")
# f.write("This is the tenth line.")
# f.close()

## 3
# name = input("What is your name? ")
# age = input("How old are you? ")
# f = open("person_info.txt", "w")
# f.write(f"{name} is {age} years old.")
# f.close()

## 4
# f = open("something_very_unique_file.txt", "r")
# contents = f.read()
# print(contents)
# f.close()

## 6
# f = open("yay_new_file.txt", "w")
# f.write("Here are some words for you.\n")
# f.close()

# Reads the file
# f = open("yay_new_file.txt")
# contents = f.read()
# print(contents)
# f.close()

# Write into the file again but with different text.
# f = open("yay_new_file.txt", "w")
# f.write("I overwrote those words.\n")
# f.close()

## Read the file again for proof that the original text was overwritten.
# f = open("yay_new_file.txt")
# contents = f.read()
# print(contents)
# f.close()

## 7
# Gives an error if the file already exists (rather than overwriting it).
# f = open("yay_new_file.txt", "x")
# f.write("Words to put in the file\n")
# f.close()

# # 8
# Write at the end of a file ("append"), you can use "a".
# f = open("yay_new_file.txt", "a")
# f.write("This will write at the end of an existing file.\n")
# f.close()