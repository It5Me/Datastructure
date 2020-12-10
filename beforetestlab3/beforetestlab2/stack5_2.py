class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return  self.items==[]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return ''.join(self.items)
it=Stack()
inp=input("Enter Input :").split(',')
m=-1
for i in inp:
    if i.split()[0]=='A':
        if int(i.split()[1])>m:
            for j in range(it.size()):
                it.pop()
            it.push(i.split()[1])
            m=int(i.split()[1])
        else:
            it.push(int(i.split()[1]))
    elif i.split()[0]=='B':
        print(it.size())
    else:
        
