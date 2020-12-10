def insertion(inp):
    for i in range(1,len(inp)):
        j=i
        while j>0 and inp[j]<inp[j-1]:
            inp[j],inp[j-1]=inp[j-1],inp[j]
            j-=1
def recurinsertion(inp,start,stop):
    if start==stop:
        return
    temp=recurwhile(inp,start)
    if len(inp[start+1:len(inp)])!=0:
        print('insert {} at index {} : {} {}'.format(inp[temp],temp,inp[0:start+1],inp[start+1:len(inp)]))
    else:
        print('insert {} at index {} : {} '.format(inp[temp],temp,inp[0:start+1]))

    recurinsertion(inp,start+1,stop)
    
def recurwhile(inp,start):
    if start<= 0 or inp[start] >= inp[start-1]:
        return start
    if start >0 and inp[start] < inp[start-1]:
        inp[start],inp[start-1]=inp[start-1],inp[start]
    return recurwhile(inp,start-1)

inp=list(map(int,input('Enter Input : ').split()))
recurinsertion(inp,1,len(inp))
print('sorted')
print(inp)


