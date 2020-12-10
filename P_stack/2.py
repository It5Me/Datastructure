inp=input("Enter Input : ").split(",")
li=[]
for i in range(0,len(inp)):
    if len(li)==0:
        li.append(inp[i])
    else:
        while len(li)>0 and int(li[-1].split(" ")[0])<int(inp[i].split(" ")[0]) :
            print(li[-1].split(" ")[1])
            if len(li)>0:
                li.pop()     
        else:
            li.append(inp[i])    

                