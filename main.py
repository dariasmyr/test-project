# Import and open a database
import csv
from datetime import datetime

# Input the attributes
file: str = input("Enter the name of the file: ")
start_date_str = input("Enter the start date: ")
end_date_str = input("Enter the end date: ")
user_address: str = input("Who is the owner of the wallet? ")
if user_address == "admin":
    user_address = "0x715c9ef6e4f3c6c30ce2761371cca97bb6912345"
else:
    pass

# Open the database
open(file, mode='r')
type(file)
csv_reader = csv.reader(file)

# Select rows with specific period and sender address
with open(file) as file:
    csv_reader_content = csv.reader(file)
    next(csv_reader_content)
    sum = 0
    count = 0
    total_sum = 0
    for row in csv_reader_content:
        # Convert the date to datetime format
        date = row[3]
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        endDate = datetime.strptime(end_date_str, '%Y-%m-%d')
        senderAddress = row[4]
        # Print the rows with specific period and sender address
        if start_date <= date <= endDate and user_address == senderAddress:
            sum += float(row[8]) + float(row[10])
            total_sum = round(sum, 2)
            if row != '\n':
                count += 1
        else:
            pass
    print(f"Transaction № {count} \nTotal sum is: {total_sum} MATIC")

