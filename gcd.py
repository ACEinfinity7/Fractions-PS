num_1 = 15
num_2 = 24

def find_gcd(a,b):
    while a != b:
        if b > a:
            b -= a
        else:
            c = b
            b = a
            a = c
            b -=a
    return a



def recur_gcd(a,b):
    if a == b:
        return a
    if b > a:
        return recur_gcd(a, b-a)
    else:
        return recur_gcd(b, a-b)
