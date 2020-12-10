def bublesort(inp):
    for i in range(len(inp)):
        for j in range(0,len(inp)-1-i):
            if inp[j]>inp[j+1]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
def insertion(inp):
    for i in range(1,len(inp)):
        inde=i
        while inp[inde]<inp[inde-1] and inde>0:
            inp[inde],inp[inde-1]=inp[inde-1],inp[inde]
            inde-=1
def selection(inp):
    for i in range(len(inp)):
        valuemin=inp[i]
        minindex=i
        for j in range(i,len(inp)):
            if inp[j]<valuemin:
                valuemin=inp[j]
                minindex=j
        inp[i],inp[minindex]=inp[minindex],inp[i]

inp=list(map(int,input('Enter Input :').split()))
selection(inp)
print(inp)