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
    def append(self,data):
        if not self.isEmpty():
            n=Node(data)
            cur=self.tail
            cur.next=n
            n.previous=cur
            self.tail=n
            self.sizes+=1
        elif self.sizes==0:
            n=Node(data)
            self.head=n
            self.tail=n
            self.sizes+=1
    def addHead(self,data):
        n=Node(data)
        if self.sizes!=0:
            self.head.previous=n
            n.next=self.head
            self.head=n
        elif self.sizes==0:
            self.append(data)                                                                               
    def __str__(self):
        st=''
        cur=self.head
        while cur!=None:
            st+=str(cur.data)+' '
            cur=cur.next
        return st        
it=Doublylinklist()
# it.append("jjkl")
# it.append("pppp")
it.addHead("HEAdddd")
print(it)