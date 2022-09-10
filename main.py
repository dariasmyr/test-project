# Import data from csv file and create a list of dictionaries

import csv

def read_transaction(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/student-00-8e4b5b9b5a9a/data/employees.csv')
print(employee_list)






import data as dt
see = dt.read_csv(r"C:\Users\dasha\work\python-projects\test-project\export-0x715C9eF6e4f3C6c30CE2761371cCa97BB6912345 (1).csv")
see.to_csv(r"C:\Users\dasha\work\python-projects\test-project\export-0x715C9eF6e4f3C6c30CE2761371cCa97BB6912345 (1).csv")
print(dt.read_csv(r"C:\Users\dasha\work\python-projects\test-project\export-0x715C9eF6e4f3C6c30CE2761371cCa97BB6912345 (1).csv"))