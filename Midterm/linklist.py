class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
        self.sizes=0
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def append(self,data):
        n=Node(data)
        if self.isEmpty():
            self.head=n
            self.sizes+=1
        else:
            cur = self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=n
            self.sizes+=1
    def insert(self,index,data):
        if  not self.isEmpty():
            if index<=self.sizes+1:
                if 0<index<self.sizes:
                    cur =self.head
                    for i in range(index-1):
                        cur=cur.next
                    n=Node(data)
                    n.next=cur.next
                    cur.next=n
                    self.sizes+=1
                elif index==0:
                    cur =self.head
                    n=Node(data)
                    n.next=cur
                    self.head=n
                    self.sizes+=1
                elif index-1==self.sizes:
                    n=Node(data)
                    cur =self.head
                    while cur.next!=None:
                        cur=cur.next
                    cur.next=n
                    self.sizes+=1
    def __str__(self):
        if self.sizes==0:
            return 'list is Empty'
        else:
            st=''
            cur = self.head
            while cur!=None:
                st+=str(cur.data)+' '
                cur=cur.next
            return str(st)

inp=input("Enter Input : ").split(',')
it=Linklist()
for i in inp[0].split():
    it.append(i)
    
print(it)
print(it.insert(3,'is 3'))
print(it)

                   


            



