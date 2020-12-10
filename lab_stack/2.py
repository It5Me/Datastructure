num=list(input("Enter Input : ").split(","))
li=[num[0]]
for i in range(1,len(num)):
    while len(li)>0 and int(li[-1].split(" ")[0])<int(num[i].split(" ")[0]):
            print(li[-1].split(" ")[1])
            li.pop()
    else:
        li.append(num[i])        
            


