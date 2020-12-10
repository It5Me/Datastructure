def findvalue (inp,x):
    tempint=[]
    for i in inp:
        if i>x:
            tempint.append(i-x)
    if len(tempint)==0:
        return 'No First Greater Value'
    value=min(tempint)
    return value+x
def bubblesort(inp):
    for i in range(len(inp)):
        for j in range(len(inp)-1-i):
            if inp[j]>inp[j+1]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
inp=input('Enter Input : ').split('/')
temp=[]
for i in inp[0].split():
    temp.append(int(i))
bubblesort(temp)
for j in inp[1].split():
    print(findvalue(temp,int(j)))

