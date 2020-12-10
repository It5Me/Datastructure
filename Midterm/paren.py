class Stack:
    def __init__(self,li=None):
        if li==None:
            self.item=[]
        else:
            self.item=li
    def push(self,data):
        self.item.append(data)
    def isEmpty(self):
        return self.item==[]
    def size(self):
        return len(self.item)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
    def peek(self):
        return self.item[-1]
    def __str__(self):
        return str(self.item)
inp=input("Enter Input ")
it=Stack()
count=0
d={')':'(','}':'{',']':'['}
for i in inp:
    if i in '({[':
        it.push(i)
    elif i in '}])':
        if it.isEmpty():
            count=1
            break
        else:
            if d[i]==it.peek():
                it.pop()
            else:
                break
if count==1:
    print('False')
elif it.isEmpty():
    print('True')
else:
    print('False')
