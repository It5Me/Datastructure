class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0
    def isEmpty(self):
        return self.head==None
    def __str__(self):
        cur=self.head
        st=''
        while cur!=None:
            st+=str(cur.data)+' '
            cur=cur.next
        return st
    def reverse(self):
        cur=self.tail
        st=''
        while cur!=None:
            st+=str(cur.data)+' '
            cur=cur.prev
        return st
    def append(self,data):
        n=Node(data)
        if not self.isEmpty():
            cur=self.head
            while  cur.next!=None:
                cur=cur.next
            n.next=cur.next
            n.prev=cur
            cur=self.tail
            cur.next=n
            self.tail=n
            self.sizes+=1
        else:
            self.head=n
            self.tail=n
            self.sizes+=1
    def addHead(self,data):
        n=Node(data)
        if not self.isEmpty():
            cur=self.head
            n.next=cur
            n.prev=cur.prev
            cur.prev=n
            self.head=n
            self.sizes+=1
        else:
            self.head=n
            self.tail=n
            self.sizes+=1 
    def search(self,data):
        cur=self.head
        while cur!=None:
            if cur.data==data:
                return print('Found')
            cur=cur.next
        return print('Not found') 
    def indexof(self,data):
        cur=self.head
        count=0
        while cur!=None:
            if cur.data==data:
                return print('index',count)
            cur=cur.next
            count+=1
        else:
            return -1
    def size(self):
        return self.sizes
    def pop(self,pos):
        cur=self.head
        for i in range(pos-1):
            cur=cur.next
        cur.next=cur.next.next
        cur.next.prev=cur
        self.sizes-=1
    def insert(self,index,data):
        if 0<=index<=self.sizes:
            if index==0:
                self.addHead(data)
            elif index==self.sizes:
                self.append(data)
            else:
                n=Node(data)
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                n.prev=cur
                n.next=cur.next
                cur.next.prev=n
                cur.next=n
        else:
            self.append(data)
        self.sizes+=1     
      
inp=input("Enter Input : ").split(',')
it=Linklist()
for i in inp:   
    if i.split()[0].startswith('AP'):
        it.append(i.split()[1])
    elif i.split()[0].startswith('AH'):
        it.addHead(i.split()[1])
    elif i.split()[0].startswith('SE'):
        it.search(i.split()[1])
    elif i.split()[0].startswith('ID'):
        it.indexof(i.splitI()[1])
    elif i.split()[0].startswith('SI'):
        print("Linked List size = {} : {}".format(it.size(),it))
    elif i.split()[0].startswith('PO'):
        it.pop(i.split()[1])
    elif i.split()[0].startswith('IS'):
        it.insert(i.split()[1],i.split()[2])
print(it)
print(it.reverse())  # เหลือ ติดลบ


        