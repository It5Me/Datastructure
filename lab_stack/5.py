class Stack:
    def __init__(self,maxsize=0,n=None):
        self.maxsize=maxsize
        if n is None:
            self.li=[]
        else:
            self.li=n
    def push(self,v):
        for i in self.li:
            if i==v:
                return 2
        if self.size()<self.maxsize:
            self.li.append(v)
            return 1
        else:
            return 0    
    def peek(self):
        return self.li[-1]
    def pop(self):
        return self.li.pop()
    def size(self):
        return len(self.li)
    def is_empty(self):
        return len(self.li)==0
    def __str__(self):
        return str(self.li)
    def remove(self,re):
        try:
            self.li.remove(re)
            return 1
        except:
            return 0


inp=input("******** Parking Lot ********\nEnter max of car,car in soi,operation : ").split()
stack=Stack(int(inp[0]))
n=list(map(int,inp[1].split(",")))
if n[0]==0:
    pass
else:
    for x in n:
        stack.push(x)
if inp[2]=="arrive":
    if stack.push(int(inp[3]))==1:
        print("car {} arrive! : Add Car {}".format(inp[3],inp[3]))
    elif  stack.push(int(inp[3]))==0:
        print("car {} cannot arrive : Soi Full".format(inp[3]))
    elif  stack.push(int(inp[3]))==2:
        print("car {} already in soi".format(inp[3]))
else:
    if stack.size()==0:
        print("car {} cannot depart : Soi Empty".format(inp[3]))        
    elif stack.remove(int(inp[3]))==1:
        print("car {} depart ! : Car {} was remove".format(inp[3],inp[3]))
    else:
        print("car {} cannot depart : Dont Have Car {}".format(inp[3],inp[3]))
print(stack)               