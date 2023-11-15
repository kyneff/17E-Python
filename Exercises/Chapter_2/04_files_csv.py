## 1
# f = open("ex_7b_data1.csv", "w")
# f.write("name_last,name_first,department,years_employed\n")
# f.write("Grantham,Bob,shipping,5\n")
# f.write("Oligarch,Chris,management,13\n")
# f.write("Smith,Sarah,customer service,12\n")
# f.write("Lasiter,Samatha,shipping,7\n")
# f.write("Zepher,bob,shipping,4\n")
# f.write("Salad,Leslie,customer service,8\n")
# f.write("LeBlu,ben,customer service,10\n")
# f.write("Wolfslayer,Kyle,shipping,3\n")
# f.write("simmering,Lance,receiving,5\n")
# f.close()

## 2
# import csv

# with open("ex_7b_data1.csv") as csv_file:
#     csv_data = csv.DictReader(csv_file, delimiter=",")
#     print()
#     print("The rows in the data set are:")
#     for row in csv_data:
#         print(row)
#     print()

## 3
# import csv

# with open('ex_7b_data1.csv') as csv_file:
#     csv_data = csv.DictReader(csv_file, delimiter=',')
#     line_count = 0      #This variable will be used to add line numbering to the output.
#     print("\nEmployee Report")
#     for row in csv_data:
#         line_count += 1
#         print(f'{line_count}) {row["name_first"]} {row["name_last"]} works in the {row["department"]} ', end='')
#         print(f'department, and has been employed with our company for {row["years_employed"]} years.')

## 4
# import csv

# with open('ex_7b_data1.csv') as csv_file:
#     csv_data = csv.DictReader(csv_file, delimiter=',')
#     line_count = 0
#     print("\nEmployee Report")
#     for row in csv_data:
#         line_count += 1
#         if row['name_last'][0].lower() == "s":
#             print(f'{line_count}) {row["name_first"]} {row["name_last"]} works in the {row["department"]} ', end='')
#             print(f'department, and has been employed with our company for {row["years_employed"]} years.')

## 5
# import csv

# with open('ex_7b_data1.csv') as csv_file:
#     csv_data = csv.DictReader(csv_file, delimiter=',')
#     line_count = 0
#     print("\nEmployee Report")
#     for row in csv_data:
#         line_count += 1
#         if int(row['years_employed']) >= 10:
#             print(f'{line_count}) {row["name_first"]} {row["name_last"]} works in the {row["department"]} ', end='')
#             print(f'department, and has been employed with our company for {row["years_employed"]} years.')

## 6
# import csv

# def bonus(row, line_count):
#     smallBonus = 200
#     mediumBonus = 500
#     largeBonus = 800
#     if int(row['years_employed']) < 5:
#         print(f'{line_count}) {row["name_first"]} {row["name_last"]} gets a ${smallBonus} bonus for {row["years_employed"]} years of service.')
#     elif int(row['years_employed']) >= 5 and int(row['years_employed']) < 10:
#         print(f'{line_count}) {row["name_first"]} {row["name_last"]} gets a ${mediumBonus} bonus for {row["years_employed"]} years of service.')
#     else:
#         print(f'{line_count}) {row["name_first"]} {row["name_last"]} gets a ${largeBonus} bonus for {row["years_employed"]} years of service.')

# def main():
#     with open('ex_7b_data1.csv') as csv_file:
#         csv_data = csv.DictReader(csv_file, delimiter=',')
#         line_count = 0
#         print("\nEmployee Report")
#         for row in csv_data:
#             line_count += 1
#             bonus(row, line_count)

# main()

## 7
# import csv

# csv_extrn2 = "ex_7b_data2.csv"  
# # Data to write to the file, stored in a list of lists:
# employees_more = [["Carver", "George Washington", "new product development", 45],
#                   ["Newton", "Isaac", "R&D", 48]]

# print(f"\nTask 7: Write employee data to a file named {csv_extrn2}.")
# with open(csv_extrn2, 'w', newline='') as csv_file:
#     field_names = ['name_last','name_first','department','years_employed']
#     writer = csv.DictWriter(csv_file, fieldnames = field_names, delimiter=",")  #Prepares an abreviated file-pointer
#     writer.writeheader()
#     # Establish a new variable "record" and assign data sets to it in sequence:
#     for record in employees_more:
#         writer.writerow({'name_last': record[0], 'name_first': record[1], 'department': record[2], 
#                         'years_employed': record[3]})
# # after exiting the "with" command, the external file writing session will be closed.
# print(f"Data writing to file '{csv_extrn2}' is completed.")

## 8
# import csv

# with open("ex_7b_data2.csv", "a", newline="") as csvInput:
#     recordsWrite = csv.writer(csvInput, delimiter=",")
#     with open("ex_7b_data1.csv") as csvData:
#         recordsRead = csv.reader(csvData, delimiter=",")
#         next(recordsRead)
#         for row in recordsRead:
#             recordsWrite.writerow(row)