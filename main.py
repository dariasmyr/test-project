# Import and open a database
import csv
from datetime import datetime

file: str = input("Enter the name of the file: ")
startDate_str = input("Enter the start date: ")
endDate_str = input("Enter the end date: ")
address: str = input("Who is the owner of the wallet? ")
if address == "admin":
    address = "0x715c9ef6e4f3c6c30ce2761371cca97bb6912345"
else:
    address = address

open(file, mode='r')
type(file)
csv_reader = csv.reader(file)

# Select rows with specific period and sender address
with open(file) as file:
    csv_reader_content = csv.reader(file)
    next(csv_reader_content)
    sum = 0
    for row in csv_reader_content:
        date = row[3]
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        startDate = datetime.strptime(startDate_str, '%Y-%m-%d')
        endDate = datetime.strptime(endDate_str, '%Y-%m-%d')
        address = row[4]
        if startDate <= date <= endDate and address == '0x715c9ef6e4f3c6c30ce2761371cca97bb6912345':
            print(row[3], row[4], row[5], row[8], row[10])
            sum += float(row[8]) + float(row[10])
            print(round(sum, 2))
            print("Total sum is: ", round(sum, 2))
        else:
            print("No transactions found")
        print("End of the program")



