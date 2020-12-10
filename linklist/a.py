class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.sizes=0
    def __str__(self):
        s=""
        cur=self.head
        while cur!=None:
            s+=str(cur.data)+' '
            cur=cur.next
        return s
    def append(self,item):
        n=Node(item)
        if self.isEmpty():
            self.head=n
            self.sizes+=1
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=n
            self.sizes+=1    
    def size(self): 
        return self.sizes
    def isEmpty(self):
        return self.sizes==0
    def insert(self,index,data):
        n=Node(data)
        if index==0:
            n.next=self.head
            self.head=n
        elif index==self.sizes:
            self.append(data)
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            n.next=cur.next
            cur.next=n    
        self.sizes+=1
        
l = LinkedList()
for i in [3,6,1]:
    l.append(i)
    #3 6 1
l.insert(1,5)
print(l)