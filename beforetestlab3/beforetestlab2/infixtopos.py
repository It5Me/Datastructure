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
    def value(self):
        if not self.isEmpty():
            return self.items
inp=input("Enter input : ")
stri=Stack()
operation=Stack()
for i in inp:
    if 'a'<=i<='z':
        stri.push(i)
        # print('a : ',i)
        print(operation.value())
    elif i in '(':
        # print('( : ',i)
        operation.push(i)
        print(operation.value())
    elif i in ')':
        # print("kut",operation.value())
        for  i  in range (operation.size()):
            temp=operation.peek()
            if temp=='(':
                operation.pop()
                break
            else:
                stri.push(operation.pop())
    else:
        # print('operation : ',i)
        if i in '/':
            if operation.isEmpty():
                operation.push(i)
            elif operation.peek()=='(':
                    operation.push(i)
            else:
                for k in operation.value():
                        if k in '*':
                            while not operation.isEmpty():
                                if not operation.peek()=='(':
                                    stri.push(operation.pop())
                                else:
                                    break
                else:
                        operation.push(i)        
        else:
            if i in '*':
                if operation.isEmpty():
                    operation.push(i)
                elif operation.peek()=='(':
                    operation.push(i)
                else:
                    for j in operation.value():
                        if j in '/':
                            while not operation.isEmpty():
                                if not operation.peek()=='(':
                                    stri.push(operation.pop())
                                else:
                                    break
                                
                    else:
                        operation.push(i)
            elif i in '+-':
                if operation.isEmpty():
                    operation.push(i)
                elif operation.peek()=='(':
                    operation.push(i)
                else:
                    for j in operation.value():
                        if j in '*/-+':
                            while not operation.isEmpty():
                                if not operation.peek()=='(':
                                    stri.push(operation.pop())   
                                else:
                                    break
                    else:
                        operation.push(i)
        print(operation.value())        

else:
    while not operation.isEmpty():
        stri.push(operation.pop())
print(stri)
