def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
# def LCM(a,b):
#     return (a * b) / GCD(a,b)
# print(LCM(24,16))