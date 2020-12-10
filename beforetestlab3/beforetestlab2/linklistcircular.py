class Doublylinklist:
    class Node:
        def __init__(self,data,prev=None,next=None):
            self.data=data
            if next==None:
                self.next=None
            else:
                self.next=next
            if prev==None:
                self.prev=None
            else:
                self.prev=prev
    def __init__(self):
        self.head=self.Node(None,None,None)
        self.head.next=self.head.prev=self.head
        self.size=0
    def __str__(self):
        s=''
        cur=self.head.next
        while cur.data!=None:
            s+=str(cur.data)+' '
            cur=cur.next
        return s
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def indexOf(self,data):
        cur=self.head.next
        count=0
        for i in range(len(self)):
            if cur.data==data:
                return count
            else:
                count+=1
                cur=cur.next
        return -1
    def isIn(self,data):
        if self.indexOf(data)==-1:
            return False
        else:
            return  True
    def nodeAt(self,index):
        cur=self.head
        for i in range(-1,index):
            cur=cur.next
        return cur
    def insertBefore(self,q,data):
        p=q.prev
        x=self.Node(data,p,q)
        p.next=q.prev=x
        self.size+=1
    def append(self,data):
        self.insertBefore(self.nodeAt(len(self)),data)
    def add(self,i,data):
        self.insertBefore(self.nodeAt(i),data)
    def remove(self,data):
        q=self.head.next
        while q.data!=None:
            if q.data==data:
                self.removeNode(q)
                return
            else:
                q=q.next
    def removeNode(self,q):
        q.prev.next=q.next
        q.next.prev=q.prev
        self.size-=1
it=Doublylinklist()
it.append(5)
it.append(6)
print(it.indexOf(5))
print(it)