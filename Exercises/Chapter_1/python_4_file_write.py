student = input("What is the student's name? ")
mathGrade = float(input(f"What is {student}'s grade for math? "))
scienceGrade = float(input(f"What is {student}'s grade for science? "))
historyGrade = float(input(f"What is {student}'s grade for history? "))
average = (mathGrade + scienceGrade + historyGrade) / 3

print(f"{student}'s average is {average:.2f}.")

f = open("calculated_average.txt", "w")
f.write(f"{student}'s average is {average:.2f}.\n")
f.close()