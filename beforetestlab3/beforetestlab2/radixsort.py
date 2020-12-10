def max_digit(inpu):
    check_len=0
    for i in inpu:
        i=len(str(i))
        if i>check_len:
            check_len=i
    return check_len
inp=list(map(int,input("Enter input : ").split()))   
print(max_digit(inp))
def get_digit(n,i):
    for i in range(i):
        n=n//10
    return n%10
def radix(inp):
    li=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(max_digit(inp)):
        while len(inp)!=0:
            temp=inp.pop(0)
            li[get_digit(temp,i)].append(temp)
        for j in li:
            while len(j)!=0:
                inp.append(j.pop(0))
print(inp)
radix(inp)
print(' '.join([str(x) for x in inp])) 
