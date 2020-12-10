class Stack:
    def __init__(self,l=None):
        if l==None:
            self.items=[]
        else:
            self.items=l
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        if self.isEmpty():
            return ''
        else:
            return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(''.join(self.items[::-1]))
    def size(self):
        return len(self.items)

inp=input("Enter Input : ").split()
stack=Stack()
count=0
combo=0
for i in inp:
    if stack.isEmpty():
        stack.push(i)
        count+=1
    else:
        if stack.peek()==i:
            stack.push(i)
            count+=1
            if count==3:
                stack.pop()
                stack.pop()
                stack.pop()
                count=0
                =combo+=1
                if stack.size()==1:
                    if stack.peek()==i:
                        count=2
                    else:
                        count=1
                elif stack.size()>=2:
                    temp=stack.pop()
                    if stack.peek()==temp:
                        count=2
                        stack.push(temp)
                    else:
                        stack.push(temp)
                        count=1
        else:
            stack.push(i)
            count=1
            combo=0
if stack.size()>0:
    print(stack)
else:
    print("Empty")
if combo>1:
    print("Combo :",combo)
