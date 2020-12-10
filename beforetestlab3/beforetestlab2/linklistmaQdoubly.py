class DoublyLinklist:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def append(self,data):
        n=self.Node(data)
        if self.isEmpty():
            self.head=self.tail=n
        else:
            cur=self.tail
            n.next=None
            n.prev=cur
            cur.next=n
            self.tail=n
        self.sizes+=1
    def __str__(self):
        s=''
        cur=self.head
        while cur!=None:
           s+=str(cur.data)+' '
           cur=cur.next
        return s
    def insert(self,index,data):
        n=self.Node(data)
        if 0<=index<=self.sizes:
            if self.isEmpty():
                self.append(data)
                return
            else:
                if index==0:
                    cur=self.head
                    n.next=cur
                    n.prev=None
                    cur.prev=n
                    self.head=n
                    self.sizes+=1
                    return
                elif index==self.sizes:
                    self.append(data)
                else:
                    cur=self.head
                    for i in range(index-1):
                        cur=cur.next
                    n.prev=cur
                    n.next=cur.next
                    cur.next.next.prev=n
                    cur.next=n
                    self.sizes+=1
                    return
    def indexof(self,data):
        cur=self.head
        count=0
        while cur!=None:
            if cur.data==data:
                return count
            cur=cur.next
            count+=1
        return 'No  index'
    def nodeAt(self,index):
        cur=self.head
        for i in range(index):
            cur=cur.next
        return cur
    def pop(self,index):
        if not self.isEmpty():
            if 0<=index<=self.sizes-1:
                if index==0:
                    cur=self.head
                    self.head=cur.next
                    self.head.prev=None
                elif index==self.sizes-1:
                    cur=self.tail
                    cur.prev.next=None
                    self.tail=cur.prev
                else:
                    cur=self.head
                    for i in range(index-1):
                        cur=cur.next
                    cur.next=cur.next.next
                    cur.next.prev=cur
                self.sizes-=1
class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=DoublyLinklist()
        else:
            self.items=li
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return self.items.size()
    def isEmpty(self):
        return self.items.isEmpty()
    def __str__(self):
        s=str(self.items)
        return s
    def getNextjob(self):
        temp=self.dequeue()
        return temp
    
inp=input("Enter Input : ")



