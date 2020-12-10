class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(''.join(self.items))
inp=input("Enter infix expression   :")
operation=Stack()
real=Stack()
for i in inp:
    print('i',i)
    if 'a'<=i<='z':
        real.push(i)
    elif i == '(':
        operation.push(i)
        print(operation)
    elif i == ')':
        for i in range(operation.size()):
            temp=operation.peek()
            if temp=='(':
                operation.pop()
                print(operation)
                break
            else:
                real.push(operation.pop())
    else:
        if operation.isEmpty():
            operation.push(i)
            print(operation)
        else:
            if i =='/':
                if operation.peek()=='*':
                    for j in range(operation.size()):
                        temp=operation.peek()
                        if temp=='(':
                            operation.push(i)
                            print(operation)
                            break
                        else:
                            real.push(operation.pop())
                    else:
                        operation.push(i)
                    print(operation)
                else:
                    operation.push(i)
                    print(operation)
            elif i=='*':
                if operation.peek()=='/':
                    for j in range(operation.size()):
                        temp=operation.peek()
                        if temp=='(':
                            operation.push(i)
                            print(operation)
                            break
                        else:
                            real.push(operation.pop())
                    else:
                        operation.push(i)
                    print(operation)
                else:
                    operation.push(i)
                    print(operation)
            else:
                if operation.peek() in '/*':
                    for j in range(operation.size()):
                        temp=operation.peek()
                        if temp=='(':
                            operation.push(i)
                            print(operation)
                            break
                        else:
                            real.push(operation.pop())
                    else:
                        operation.push(i)
                    print(operation)
                else:
                    operation.push(i)
                    print(operation)
while not operation.isEmpty():
    real.push(operation.pop())
print(real)
numoper=0
numstri=0
for x in inp:
    if x in '+-*/':
        numoper+=1
    elif 'A'<=x<='Z' or 'a'<=x<='z':
        numstri+=1
print(numoper)
print(numstri)






