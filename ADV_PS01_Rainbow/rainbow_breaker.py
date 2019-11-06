import hashlib
import os
import csv
import pandas
my_dir = os.path.dirname(os.path.realpath(__file__))

with open(my_dir + '/' + "target_hash_list.csv", 'r') as target_list:
    tar_lst_reader = csv.DictReader(target_list)
    targets = {}
    for row in tar_lst_reader:
        targets[row['pwd']] = row['pwd_hash']


with open(my_dir + '/' + 'rainbow_table.csv','r') as f:
    rainbow = {}
    reader = csv.DictReader(f)
    for row in reader:
        rainbow[row['final']] = row['initial']


val = targets['sunshine']
for i in range(5):
        val2 = val.encode('utf-8')
        new_val = hashlib.sha1(val2).hexdigest()
        val = new_val[:8]

target = val
print(target)
def rainbow_check(target,rainbow):
    for i in range(5):
        if target in rainbow:
            print(true)

#rainbow_check(target,rainbow)
