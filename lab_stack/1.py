in_p=input("Enter Input : ")
d={')':'(',']':'[','}':'{'}
li=[]
for i in in_p:
    if i in '([{':
        li.append(i)
    elif i in ')]}':
        if len(li)>0 and li[-1]==d[i]:
            li.pop()
        else:
            li.append(i)
if len(li)==0:
    print(len(li))
    print("Perfect ! ! !")
else:
    print(len(li))               
