def twobit(x):
    if x == n:
        print(''.join(map(str,a)))
        return
    a[x]=0
    twobit(x+1)
    a[x]=1
    twobit(x+1)
n = 3
a = [0]*n
twobit(0)