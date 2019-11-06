import hashlib
import os
import csv
filename = 'pbkdf2_uid_pwd_list_for2ndpart.csv'

def read_in_data(filname):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    user_list = []
    with open(my_dir + '/' + filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            user_list.append((row[0],row[1]))
    return user_list

def save_out_data(out_data, outfile):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    with open(my_dir + '/' + outfile, 'w') as o_f:
        out_writer = csv.writer(o_f)
        out_writer.writerow(('uid', 'data', 'salt'))
        for keys in out_data.keys():
            out_writer.writerow((keys, out_data[keys][0], out_data[keys][1]))

def make_database(user_list, iterations, hash_type, salt_length):
    out_data = {}
    for items in user_list:
        val, salt = do_pbkdf2_hamc(items[1], iterations, hash_type, salt_length)
        #print(val.hex())
        out_data[items[0]] = (val.hex(), salt.hex())
    return out_data


def do_pbkdf2_hamc(password, iterations, hash_type, salt_length):
    salt = os.urandom(salt_length)
    output = hashlib.pbkdf2_hmac(hash_type, b'password', salt, iterations)
    return output, salt

iterations = 10000
hash_type = 'sha512'
salt_length = 64

user_list = read_in_data(filename)
out_data = make_database(user_list, iterations, hash_type, salt_length)
outfile = 'stored_password_data.csv'
save_out_data(out_data, outfile)
