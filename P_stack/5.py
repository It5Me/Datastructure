class Stack:
    def __init__(self,n=None):
        if n==None:
            self.li=[]
        else:
            self.li=[n]    
    def is_empty(self):
        return len(self.li)==0
    def size(self):
        return len(self.li)
    def pop(self):
        return self.li.pop()        
    def push(self,v):
        self.li.append(v)
    def peek(self):
        return self.li[-1]
    
inp=input("Enter Input : ").split(",")
stack=Stack()
for x in inp:
    if x.split()[0]=='A':
        while stack.size()>0 and stack.peek()<=x:
            stack.pop()  
        stack.push(x)

    elif x=='B':
        print(stack.size())        