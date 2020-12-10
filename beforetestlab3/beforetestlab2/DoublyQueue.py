class DoublyLinkList:
    class Node:
        def __init__(self,data,prev=None,next=None):
            self.data=data
            if prev==None:
                self.prev=None
            else:
                self.prev=prev
            if next==None:
                self.next=None
            else:
                self.next=next
    def __init__(self):
        self.head=self.Node(None,None,None)
        self.head.next=self.head.prev=self.head
        self.sizes=0
    def __str__(self):
        st='LinkedList data : '
        cur=self.head.next
        while cur.data !=None:
            st+=str(cur.data) + ' '
            cur=cur.next
        return st
    def __len__(self):
        return self.sizes
    def isEmpty(self):
        return self.sizes==0
    def indexOf(self,data):
        cur=self.head.next
        for i in range(self.sizes):
            if cur.data==data:
                return i
            cur=cur.next
        return -1
    def isIn(self,data):
        cur=self.head.next
        for i in range(self.sizes):
            if cur.data==data:
                return True
        return False
    def nodeAt(self,inde):
        cur=self.head
        for i in range(-1,inde):
            cur=cur.next
        return cur
    def insertBefore(self,q,data):
        p=q.prev
        x=self.Node(data,p,q)
        p.next=q.prev=x
        self.sizes+=1
    def append(self,data):
        self.insertBefore(self.nodeAt(len(self)),data)
    def add(self,i,data):
        self.insertBefore(self.nodeAt(i),data)
    def remove(self,data):
        q=self.head.next
        while q.data!=None:
            if q.data==data:
                self.removeNode(q)
                return 0
            q=q.next
        return -1 
    def removeNode(self,p):
        p.prev.next=p.next
        p.next.prev=p.prev
        self.sizes-=1
class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=DoublyLinkList()
        else:
            self.items=li
    def __str__(self):
        s='Queue data : '
        st=str((self.items))
        s+=str(st[18:])
        return s
    def __len__(self):
        return len(self.items.sizes)
    def isEmpty(self):
        return self.items.isEmpty()
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        self.items.removeNode((self.items.nodeAt(0)))
    def enQueueLeft(self,data):
        self.items.insertBefore(self.items.nodeAt(0),data)
    def enQueueRight(self,data):
        self.items.append(data)

it=DoublyLinkList()
q=Queue()
it.append(1)
it.append(2) 
it.remove(5)
q.enqueue(0)
q.dequeue()
q.enqueue(1)
q.enQueueLeft(55)
q.enQueueRight('PIm')
print(q)

        

        


    


    

