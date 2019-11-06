import scrypt
import bcrypt
from argon2 import PasswordHasher
import os

def use_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(),salt)
    return hashed

def check_bcrypt(password_1, user_list, uid):
    if bcrypt.checkpw(password_1.encode(), user_list[uid]):
        return True
    else:
        return False

def use_scrypt(password, maxtime, salt_len):
    salt = os.urandom(salt_len)
    hash = scrypt.encrypt(password, salt, maxtime)
    return hash

def check_scrypt(uid, user_lst_2, password_1, maxtime):
    try:
        scrypt.decrypt(user_lst_2[uid], password_1, maxtime)
        return True
    except scrypt.error:
        return False

def use_argon(password):
    ph = PasswordHasher()
    hash = ph.hash(password)
    return hash

def check_argon(uid, user_lst_3, password_1):
    ph = PasswordHasher()
    try:
        ph.verify(user_lst_3[uid], password_1)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

user_lst_1 = {}
user_lst_2 = {}
user_lst_3 = {}

uid = 'hello'
password = 'goodbye'
password_1 = 'goodbye'
maxtime = 1.0
salt_len = 64

user_lst_1[uid] = use_bcrypt(password)
print(check_bcrypt(password_1, user_lst_1, uid))
print(user_lst_1)
user_lst_2[uid] = use_scrypt(password, maxtime, salt_len)
print(check_scrypt(uid, user_lst_2, password_1, maxtime))
print(user_lst_2)
user_lst_3[uid] = use_argon(password)
print(check_argon(uid, user_lst_3, password_1))
print(user_lst_3)
