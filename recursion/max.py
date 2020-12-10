def findmax(inp,n):
    if n==1:
        return inp[0]
    else:
        return max(inp[n-1],findmax(inp,n-1))
        
inp=list(map(int,input("Enter Input : ").split()))
n=len(inp)
print("Max :",findmax(inp,n))