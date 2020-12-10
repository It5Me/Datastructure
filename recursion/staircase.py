def abs(n):
    if n>0:
        return n
    else:
        return n*-1
def staircase(n,m):
    if n == 0:
        return ''
    if m < 0:
        return staircase(n+1,m) + ("_"*abs(n+1) + "#"*abs(m-n-1) +'\n')
    return staircase(n-1,m) + ("_"*abs(m-n) + "#"*abs(n) +'\n')
size = int(input("Enter Input : "))
if size == 0:
    print("Not Draw!")
else:
    print(staircase(size,size), end='') 