## 1
# word = input('Input a word: ')
# print(word[-3:])

## 2
# word = input('Input a word: ')
# if  word[-3:] == 'MHz':
#     print('Mike')
# elif word[-3:] == 'GHz':
#     print('Golf')
# else:
#     print('No match.')

## 3
# word = input('Input a word: ')
# print(word[:-3])

## 4
# userInput = input('Input a number with MHz: ')
# frequency, megahertz = userInput.split()
# print(frequency)

## 5
# frequency = input('Input a number with MHz: ')
# x, y = frequency.split()
# z = int(x)
# print(z / 1000)

## 6
# mix = input('Input a string that contains letters and numbers: ')
# for digits in mix:
#     if digits.isnumeric() == True:
#         print(digits)

## 7
# word = input('Input a word: ')
# backwards = reversed(word)
# print(''.join(backwards))

## 8
# x = input("Type some words, and type extra space at the beginning or end.").strip()
# print(f"I have removed the extra space. You typed... {x}")

## 9
# username = input('Input a name: ')
# while username.lower().strip() not in ['chimi', 'ollie', 'olive', 'tux', 'pickle', ]:
#     username = input('This username is not allowed. Input a name: ')
# print('This username is allowed.')

## 10
import string

word = input('Input a word: ')
shift = int(input('Input a number between 0-24: '))

letters = list(string.ascii_lowercase)
for x in word:
    position = letters.index(x)
    encrypt = position + shift

    print(letters[encrypt], end='')

## 11
# Make Tic Tac Toe.

## 12
# Do the Matplotlib tutorial.
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

## 20
# As an exercise, make the Wordle game: https://www.nytimes.com/games/wordle/index.html
# (Note: this is only an educational exercise; please do not infringe on their rights.)

# You'll most likely want to use the `in` keyword:
# if "e" in "hello":
#     print("The letter e is in the word hello.")