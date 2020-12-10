# def selection(inp):
#     for i in range(len(inp)):
#         minn=inp[i]
#         minnindex=i
#         for j in range(i,len(inp)):
#             if minn>inp[j]:
#                 minn=inp[j]
#                 minnindex=j
#         inp[i],inp[minnindex]=inp[minnindex],inp[i]
def recurselection(inp,start,stop):
    if start==stop:
        return
    temp=recurfor(inp,start,stop,inp[start],start)
    inp[start],inp[temp]=inp[temp],inp[start]
    if start!=temp:
        print('swap {} <-> {} : {}'.format(inp[temp],inp[start],inp))
    recurselection(inp,start-1,stop)
def recurfor(inp,start,stop,maxx,maxxindex):
    if start==stop:
        return maxxindex
    if maxx<inp[start]:
        maxx=inp[start]
        maxxindex=start
    return recurfor(inp,start-1,stop,maxx,maxxindex)

inp=list(map(int,input('Enter Input : ').split()))
recurselection(inp,len(inp)-1,-1)
print(inp)




