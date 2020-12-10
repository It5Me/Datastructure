class Stack:
    def __init__(self,li=None):
        if li==None:
            self.item=[]
        else:
            self.item=li
    def isEmpty(self):
        return self.item==[]
    def size(self):
        return len(self.item)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
    def push(self,data):
        self.item.append(data)
    def peek(self):
        return self.item[-1]

it=Stack()



