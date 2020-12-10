class Queue:
    def __init__(self,l=None):
        if l==None:
            self.li=[]
        else:
            self.li=l
    def enq(self,data):
        self.li.append(data)
    def deq(self):
        if self.isEmpty():
            return 'Empty'
        else:
            self.li.pop(0)    
    def isEmpty(self):
        return len(self.li)==0
    def front(self):
        return self.li[0]
    def clear(self):
        self.li.clear()
    def size(self):
        return len(self.li)    
