class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes= 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, ""
        while cur.previous != None:
            s += str(cur.value) + " "
            cur = cur.previous
        s += str(cur.value)
        return s

    def isEmpty(self):
        return self.head == None
    def append(self, item):
        n=Node(item)
        if self.sizes==0:
            self.head=self.tail=n
            self.sizes+=1
        else:
            n.next=self.tail.next
            n.previous=self.tail
            self.tail.next=n
            self.sizes+=1
            self.tail=n
    def addHead(self, item):
        n=Node(item)
        if self.isEmpty():
            self.head=self.tail=n
            self.sizes+=1
        else:
            n.next=self.head
            n.previous=self.head.previous
            self.head.previous=n
            self.head=n
            self.sizes+=1
    def insert(self, pos, item):
        n=Node(item)
        if pos>=0:
            if pos!=0 and pos<self.sizes:
                cur = self.head
                for i in range(pos-1):
                    cur=cur.next
                n.previous=cur
                n.next=cur.next
                self.sizes+=1
            elif pos == 0:
                # n.previous=self.head.previous
                # n.next=self.head
                # self.head.previous=n
                # self.head=n
                # self.sizes+=1
                self.addHead(item)
            elif pos>self.sizes-1:
                self.append(item)
        else:
            n=Node(item)
            if pos <=-1*(self.sizes):
                self.addHead(item)
            elif (self.sizes)*-1<pos<=-1:
                # pos+=self.sizes
                cur =self.tail
                for i in range(-1,pos,-1):
                    cur=cur.previous
                n.previous=cur.previous
                n.next=cur
                cur.previous.next=n
                cur.previous=n
                self.sizes+=1                
    def search(self, item):
        cur=self.head
        while cur!=None:
            if cur.value==item:
                return 'Found'
            cur=cur.next
        else:
            return 'Not Found'         

    def index(self, item):
        cur=self.head
        i=0
        while cur!=None:
            if cur.value==item:
                return i
            i+=1
            cur=cur.next
        else:
            return -1    
    def size(self):
        return self.sizes
    def pop(self, pos):
        cur=self.head
        if pos<0 or pos>self.sizes-1:
            return 
        elif pos==0:
            if self.head.next!=None:
                self.head.next.previous=self.head.previous
            self.head=self.head.next
            self.sizes-=1
            return 
        elif pos==self.sizes-1:
            if self.tail.previous!=None:
                self.tail.previous.next=self.tail.next
            self.tail=self.tail.previous
            self.sizes-=1
            return 
        else:
            cur=self.head
            for i in range(pos-1):
                cur =cur.next
            cur.next.next.previous=cur
            cur.next=cur.next.next
            self.sizes-=1
            return 

inp=input("Enter Input (L1,L2) : ").split()
l1=LinkedList()
for i in inp[0].split('->'):
    l1.append(i)
l2=LinkedList()
for i in inp[1].split('->'):
    l2.append(i)

print("L1    : {}".format(l1))
print("L2    : {}".format(l2))
print("Merge : {}{}".format(l1,l2.reverse()))