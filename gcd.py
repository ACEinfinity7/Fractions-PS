num_1 = 997
num_2 = 1

def find_gcd(a,b):
    a,b = abs(a),abs(b)
    if a == 0 and b == 0:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if b > a:
            b -= a
        else:
            a,b = b,a
            b -=a
    return a



def recur_gcd(a,b):
    a,b = abs(a),abs(b)
    if a == 0 and b == 0:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if b > a:
        return recur_gcd(a, b-a)
    if a > b:
        return recur_gcd(b, a-b)
    return a

print(find_gcd(num_1,num_2))
print(recur_gcd(num_1, num_2))
