def findMedian(inp):
    total=0
    if len((inp))%2==0:
        n=((len(inp)+1)//2)
        m=((len(inp)+1)//2)-1
        total=(inp[n]+inp[m])/2
        return total
    else:
        n=((len(inp)+1)//2)-1
        return inp[n]
def input_sort(inp):
    for i in range(0,len(inp)):
        for j in range(len(inp)-1-i):
            if inp[j]>inp[j+1] :
                inp[j],inp[j+1]=inp[j+1],inp[j]
    return inp   
l = [e for e in input("Enter Input : ").split()]
ar=[]
toprint=[]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    for x in l:
        ar.append(int(x))
        toprint.append(int(x))
        temp=findMedian(input_sort(ar))
        print('list = {} : '.format(toprint),end='')
        print('median = {:.1f}'.format(temp))



    