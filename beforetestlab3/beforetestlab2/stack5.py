class Stack:
    def __init__(self,m,l=None):
        self.mxsize=m
        if l==None:
            self.items=[]
        else:
            self.items=l
    def push(self,data):
        self.items.append(data)
    def isEmpty(self):
        return len(self.items)==0
    def pop(self):
        if self.isEmpty():
            return 'Empty'
        else:
            return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)
    def size(self):
        return len(self.items)
    def arrive(self,n):
        for i in self.items:
            if i==n:
                return print("car {} already in soi".format(n))
            else:
                if self.size()==self.mxsize:
                    return print("car {} cannot arrive : Soi Full".format(n)) 
    def depart(self,n):
        if self.isEmpty():
            return print("car {} cannot depart : Soi Empty".format(n))
        else:
            for i in self.items:
                if i==n:
                    self.items.remove(n)
                    return print("car {} depart ! : Car {} was remove".format(n,n))
                elif self.size()==0:
                    return print("car {} cannot depart : Soi Empty".format(n))
                else:
                    return print("car {} cannot depart : Dont Have Car {}".format(n,n))



print("******** Parking Lot ********")
size,inp,act,num=input("Enter max of car,car in soi,operation : ").split()
stack=Stack(int(size))
for i in inp.split(','):
    if int(i)>0:
        stack.push(int(i))
if act=='arrive':
    stack.arrive(int(num))
elif act=='depart':
    stack.depart(int(num))
print(stack)





        