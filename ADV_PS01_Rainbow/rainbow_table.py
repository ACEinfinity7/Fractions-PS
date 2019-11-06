import hashlib
import os
import csv
import pandas
my_dir = os.path.dirname(os.path.realpath(__file__))

#print(hashlib.sha1(("hello").encode('utf-8')).hexdigest())

with open(my_dir + '/' + "500-most-common_passwords.txt", 'r') as common_list:
    common_reader = csv.reader(common_list)
    common = []
    for row in common_reader:
        if len(str(row[0])) == 8:
            common.append(row[0])

#print(common)

rainbow = {}

for i in range(len(common)):
    val = common[i]
    for j in range(5):
        val2 = val.encode('utf-8')
        new_val = hashlib.sha1(val2).hexdigest()
        val = new_val[:8]
    rainbow[val] = common[i]


with open(my_dir + '/' + 'rainbow_table.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('final','initial'))
    for key, value in rainbow.items():
       writer.writerow((key,value))
