class Stack:
    def __init__(self,n=None):
        if n!=None:
            self.li=n
        else:
            self.li=[]    
    def is_empty(self):
        return len(self.li)==0
    def size(self):
        return len(self.li)
    def peek(self):
        return self.li[-1]
    def pop(self):
        return self.li.pop()
    def push(self,x):
        self.li.append(x)
    def __str__(self):
        return str(''.join(self.li[::-1]))

inp=input("Enter Input : ").split()
l=Stack()
count=0
combo=0
for x in inp:
    if l.is_empty():
        l.push(x)
        count=1
    else:
        if l.peek()==x:
            count+=1
            if count==3:
                l.pop()
                l.pop()
                combo+=1
                if l.size()>=2: 
                    temp=l.pop()
                    if temp==l.peek():
                        count=2
                    else:
                        count=1
                    l.push(temp)        
                elif l.size()==1:
                    count=1
            else:
                l.push(x)    
        else:
            count=1
            l.push(x)
print(l.size())
if l.is_empty():
    print("Empty")                         
else:
    print(l)
if combo>=2:
    print("Combo : {} ! ! !".format(combo))              
