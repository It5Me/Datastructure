class Stack:
    def __init__(self,l=None):
        if l==None:
            self.items=[]
        else:
            self.items=l
    def pop(self):
        if self.isEmpty():
            return ''
        else:
            return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def peek(self):
        if self.isEmpty():
            return -1
        else:    
            return self.items[-1]
inp=input("Enter Infix : ")
stack=Stack()
temp=""
for i in inp:
    if i in '/*-+()^':
        if stack.isEmpty():
            stack.push(i)
        elif i in '+-':
            if stack.peek() in '/*^':
                while not(stack.isEmpty()) and stack.peek()!='(':
                    temp+=stack.pop()
            stack.push(i)
        elif i in '*/':
            if stack.peek() in '^':
                while not(stack.isEmpty()) and stack.peek()!='(':
                    temp+=stack.pop()
            stack.push(i)
        elif i in '(':
            stack.push(i)
        elif i in ')':
            while not(stack.isEmpty()) and stack.peek()!='(':
                temp+=stack.pop()
            stack.pop()

    else:
        temp+=i
else:
    while not(stack.isEmpty()) :
        temp+=stack.pop()
print(temp)        

