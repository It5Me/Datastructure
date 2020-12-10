class Stack:
    def __init__(self,l=None):
        if l==None:
            self.li=[]
        else:
            self.li=l
    def push(self,data):
        self.li.append(data)
    def pop(self):
        if self.isEmpty():
            return 'Empty'
        return self.li.pop()
    def peek(self):
        return self.li[-1]
    def isEmpty(self):
        return len(self.li)==0
    def size(self):
        return len(self.li)
    def clear(self):
        self.li.clear()

s=Stack()
for i in [3,2,1]:
    s.push(i)     3 2 1
s.pop()
print(s.peek())
s.push(7)
print(s.peek())
for i in range(5):
    s.pop()
s.push(4)
print(s.peek())
                            
        