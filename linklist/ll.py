d={'}':'{',']':'[',')':'('}
inp=input("Enter input :")
li=[]
for i in inp:
    if i in '({[':
        li.append(i)
    elif i in ')}]':
        if len(li)!=0:
            if  d[i]==li[-1]:
                li.pop()
            else:
                break
        else:
            li.append(0)
            break    
if len(li)==0:
    print("Cor")
else:
    print("incor")              





