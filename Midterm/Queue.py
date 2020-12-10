class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        self.items.pop(0)

