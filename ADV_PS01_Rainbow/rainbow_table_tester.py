import hashlib
import os
import csv
import pandas
from rainbow_table_2 import *
filename = '500-most-common_passwords.txt'
tar_filename = 'target_hash_list.csv'
out_filename = 'rainbow-table.csv'
reps = 5

targets = read_in_targets(tar_filename)
# print(targets)
#common = read_in_common_passwords(filename)
#rainbow = iterate_list_and_hash_reduce(common, reps)
rainbow = read_in_rainbow_table(out_filename)

#print(rainbow)

#write_to_file(rainbow,out_filename)
for target in targets.values():
    count, solved, check = compare_password_with_table(rainbow,target,reps)
    if check == True:
        final = work_back_up(count, solved)
        print(target, final, hash.sha1(final.encode()).hexdigest())
