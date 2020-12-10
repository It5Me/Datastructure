inp=input("Enter Input : ").split(",")
li=[]
m=0
count=0
d=True
counttemp=0
for x in inp:
    if x.split()[0]=='A':
        li.append(x.split()[1])    
    elif x.split()[0]=='B':
        if d==True: 
            for x in li[::-1]:
                # print(li[::-1])
                x=int(x)
                if x>m:
                    m=x
                    count+=1   
            print("count",count)
            count=0
            m=0
        else:
            print("Tempcount",counttemp)
            d=True
            counttemp=0
    elif x.split()[0]=='S':
        temp=[]
        n=0
        for x in li:
            d=False
            x=int(x)
            if x%2==0:
                x=x-1
                temp.append(x)
            else:
                x=x+2    
                temp.append(x) 
            # print(temp[::-1])                    
        for x in temp[::-1]:
            if x>n:
                n=x
                counttemp+=1
                
            

