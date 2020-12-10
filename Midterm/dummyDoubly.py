class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class Doublylinklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def append(self,data):
        n=Node(data)
        if self.isEmpty():
            self.head=n
            self.tail=n
        else:
            n.previous=self.tail
            n.next=self.tail.next
            self.tail.next=n
            self.tail=n
        self.sizes+=1
    def insert(self,index):
        pass
    def indexof(self,data):
        pass
    def search(self,data):
        pass
    def pop(self,index):
        if  not self.isEmpty():
            cur=self.head
            if index==0:
            elif 0<index<self.sizes-1:
            elif index=self.sizes

    def addhead(self):
        pass 


    