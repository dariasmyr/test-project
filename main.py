import csv

file = open(
    r"C:\Users\dasha\work\python-projects\test-project\export-0x715C9eF6e4f3C6c30CE2761371cCa97BB6912345 (1).csv")

type(file)

csv_reader = csv.reader(file)

# Select rows with specific date

with open(
        r"C:\Users\dasha\work\python-projects\test-project\export-0x715C9eF6e4f3C6c30CE2761371cCa97BB6912345 (1).csv") as file:
    csv_reader_content = csv.reader(file)
    next(csv_reader_content)
    sum = 0
    for row in csv_reader_content:
        if "2022-09-01" in row[3] and row[4] == "0x715c9ef6e4f3c6c30ce2761371cca97bb6912345":
            print(row[3], row[4], row[5], row[8], row[10])
            sum += float(row[8]) + float(row[10])
            print(round(sum, 2))
            print("Total sum is: ", round(sum, 2))
        else:
            print("No transactions found")
        print("End of the program")
