class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def __str__(self):
        if not self.isEmpty():
            return ''.join(self.items)
    def value(self):
        if not self.isEmpty():
            li1=[]
            temp=self.items.copy()
            print(temp)
            # while self.size()!=0:
            #     li1.append(temp)
            return li1[::-1]
inp=input("Enter infix expression        : ")
st=Stack()
opera=Stack()
for i in inp:
    if 'a'<=i<='z':
        st.push(i)
    elif i in '+-*/()':
        if i in '+-':
            if opera.isEmpty():
                opera.push(i)
            else:
                for j in opera.value():
                    if j in '*/':
                        for x in opera.value():
                            st.push(x)
                            opera.pop()
                        else:
                            opera.push(i)
                    else:

                        opera.push(i)

        elif  i in '*':
            if opera.isEmpty():
                opera.push(i)
            else:
                for j in opera.value():
                    if j in '/':
                        for x in range(opera.size()):
                            st.push(x)
                            opera.pop()
                        else:
                            opera.push(j)
                    else:
                        opera.push(j)
        elif i in '/':
            opera.push(i)
        else:
            pass
else:
    while not opera.isEmpty():
        st.push(opera.pop())
               
print(st) 


