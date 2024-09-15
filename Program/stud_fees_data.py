#Program [ 1 ]
#Create table stud(id, name, dept, paidfee) with 8 records.
#Create stud.csv file of the stud data (Department will be BBA and BCA).
#Read csv file using reader object and write data with remaining fee.
#( Total fee of bba is 13400 and bca is 15400 Rs)

import csv

#Read the CSV file and print data from the file with append()
#with skipping the header

students = []

with open("D:\\sqlite\\csv\\stud1.csv", "r") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if all(row):
            students.append(row)
print(students)

#Define the total fees of BCA and BBA and convert paidfee
#into integer form and appending each data into a list

total_fees = {
    'BCA': 15400,
    'BBA': 13400
}
students_with_remaining_fee = []
for student in students:
    id, name, dept, paidfee = student
    if paidfee:
        paidfee = int(paidfee)  
    else:
        paidfee = 0  
    
    remaining_fee = total_fees[dept] - paidfee
    
    # Append the updated data to the list
    students_with_remaining_fee.append([id, name, dept, paidfee, remaining_fee])

print(students_with_remaining_fee)

#Write the updated data into a new CSV file named "stud_remaining_fee"
#with header

# Write the data with remaining fees to a new CSV file

with open("D:\\sqlite\\csv\\stud_remaining_fee.csv", "w", newline='') as f:
    writer = csv.writer(f)
    
    # header
    writer.writerow(['id', 'name', 'dept', 'paidfee', 'remaining_fee'])
    
    writer.writerows(students_with_remaining_fee)

print("File with remaining fees created successfully!")
