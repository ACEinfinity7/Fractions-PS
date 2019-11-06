import hashlib as hash
import os
import csv
import pandas


def read_in_common_passwords(filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + filename, 'r') as common_list:
        common_reader = csv.reader(common_list)
        common = []
        for row in common_reader:
            if len(str(row[0])) == 8:
                common.append(row[0])
    return common

def read_in_targets(tar_filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + tar_filename, 'r') as target_list:
        tar_lst_reader = csv.DictReader(target_list)
        targets = {}
        for row in tar_lst_reader:
            targets[row['pwd']] = row['pwd_hash']
    return targets

def read_in_rainbow_table(out_filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + out_filename, 'r') as target_list:
        tar_lst_reader = csv.DictReader(target_list)
        targets = {}
        for row in tar_lst_reader:
            targets[row['final']] = row['initial']
    return targets

def write_to_file(rainbow, out_filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + out_filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(('final','initial'))
        for value in rainbow.items():
           writer.writerow((value[0],value[1]))

def iterate_list_and_hash_reduce(common, reps):
    rainbow = {}
    for item in common:
        val = item
        for i in range(reps):
            val = hash.sha1(val.encode()).hexdigest()[:8]
        rainbow[val] = item
    return rainbow

def compare_password_with_table(rainbow, target, reps):
    target = target[:8]
    for i in range(reps-1):
        if target in rainbow:
            return i, target, True
        else:
            val = hash.sha1(target.encode()).hexdigest()
            target = val[:8]
    return False, False, False

def work_back_up(count, solved):
    for i in range(count-1):
        val = hash.sha1(solved.encode()).hexdigest()
        solved = val[:8]
    return solved
