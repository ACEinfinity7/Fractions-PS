import hashlib
import os
import csv
import pbkdf2_hmac_1
import binascii
filename = 'stored_password_data.csv'

def read_in_data(filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + filename, 'r') as f:
        reader = csv.DictReader(f)
        uid_dict = {}
        for row in reader:
            pass_1 = row['data'].encode()
            salt_1 = row['salt'].encode()
            uid_dict[row['uid']] = (pass_1, salt_1)
    return uid_dict

def read_in_inputs(uid, password, uid_dict, hash_type, iterations):
    if uid in uid_dict:
        salt = (uid_dict[uid][1])
        output = hashlib.pbkdf2_hmac(hash_type, b'password', salt, iterations)
        print(uid_dict[uid][0])
        print(binascii.hexlify(output))
        if uid_dict[uid][0] == output.hex():
            return True
        else:
            return False
    else:
        return False



uid = 'soso'
password = 'baseball'
iterations = 10000
hash_type = 'sha512'
uid_dict = read_in_data(filename)
print(read_in_inputs(uid, password, uid_dict, hash_type, iterations))
print(uid_dict)
