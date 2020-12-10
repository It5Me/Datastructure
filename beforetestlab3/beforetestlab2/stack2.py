class Stack:
    def __init__(self,l=None):
        if l==None:
            self.items=[]
        else:
            self.items=l
    def push(self,data):
        self.items.append(data)
    def pop(self):
            return self.items.pop()
    def peek(self):
        if self.isEmpty():
            return ''
        else:
            return self.items[-1]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

inp=input("Enter Input : ").split(',')
stack=Stack()
stackHz=Stack()
li=[]
for i in inp:
    if stack.isEmpty():
        stack.push(i.split()[0])
        stackHz.push(i.split()[1])
    else:
        while stack.size()!=0:
            if stack.peek()<i.split()[0]:
                stack.pop()
                li.append(stackHz.pop())
            else:
                break
        stack.push(i.split()[0])
        stackHz.push(i.split()[1])
print(stackHz)           
for i in li:
    print(i)
                


    

        