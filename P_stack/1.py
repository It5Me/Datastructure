n=input("Enter Input : ")
d={')':'(',']':'[','}':'{'}
li=[]
for x in n :
    if x in '([{':
        li.append(x)
    elif x in ')]}':
        if d[x]==li[-1]:
            li.pop()
        else:
            li.append(x)
                
print(len(li))             
