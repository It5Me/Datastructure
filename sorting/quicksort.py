def mergesort(inp,l,r):
    if l==r or l+1==r:
        if inp[l]>inp[r]:
            inp[l],inp[r]=inp[r],inp[l]
        return
    mergesort(inp,l,(l+r)//2)
    mergesort(inp,((l+r)//2)+1,r)
    keepleft=inp[l:(l+r)//2+1]
    keepright=inp[(l+r)//2+1:r+1]
    pos = l
    while len(keepleft)!=0 and len(keepright)!=0:
        if keepleft[0]>keepright[0]:
            inp[pos]=keepright.pop(0)
            pos+=1
        else:
            inp[pos]=keepleft.pop(0)
            pos+=1
    while len(keepleft)!=0:
        inp[pos]=keepleft.pop(0)
        pos+=1
    while len(keepright)!=0:
        inp[pos]=keepright.pop(0)
        pos+=1
def quicksort(inp,l,r):
    if r<=l:
        return
    pivot=r
    i,j=l,l
    while j<pivot:
        if inp[j]<inp[pivot]:
            inp[i],inp[j]=inp[j],inp[i]
            i+=1
            j+=1
        elif inp[j]>inp[pivot]:
            j+=1
    inp[pivot],inp[i]=inp[i],inp[pivot]
    pivot,i=i,pivot
    quicksort(inp,l,pivot-1)
    quicksort(inp,pivot+1,r)
inp=list(map(int,input('Enter input : ').split()))
quicksort(inp,0,len(inp)-1)
print(inp)
