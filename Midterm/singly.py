class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylinklist:
    def __init__(self):
        self.head=None
        self.sizes=0
    def append(self,data):
        n=Node(data)
        if self.isEmpty():
            self.head=n
            self.sizes+=1
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=n
            self.sizes+=1
    def insert(self,index,data):
        n=Node(data)
        if index>0:
            if index<self.sizes:
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                n.next=cur.next
                cur.next=n
                self.sizes+=1    
            elif index==(self.sizes)+1:
                cur =self.head
                while cur.next!=None:
                    cur=cur.next
                cur.next=n
                self.sizes+=1
        elif index==0:
            cur =self.head
            n.next=cur
            self.head=n
            self.sizes+=1
        elif index<0:
            cur=self.head
            if index*(-1)<=self.sizes-1:
                for i in range(0,index+self.sizes-1,1):
                    cur=cur.next
                n.next=cur.next
                cur.next=n
                self.sizes+=1
    def __str__(self):
        st=''
        if not self.isEmpty():
            cur=self.head
            while cur!=None:
                st+=str(cur.data)+' '
                cur=cur.next
            return st
        else:
            return 'List is Empty'
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def pop(self,index):
        if self.isEmpty():
           return 'List is Empty' 
        else:
            if index>0:
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                cur.next=cur.next.next
                self.sizes-=1
            elif index<0:
                 cur=self.head
                 for i in range(0,index+self.sizes-1,1):
                    cur=cur.next
                 cur.next=cur.next.next
                 self.sizes-=1
            elif index==0:
                cur=self.head
                self.head=cur.next
                self.sizes-=1
    def index(self,data):
        if  not self.isEmpty(): 
            cur=self.head
            for i in range(0,self.sizes): 
                if cur.data==data:
                    return i
                cur=cur.next  
            else:
                return 'NOT FOUND'           
    def search(self,data):
        if  not self.isEmpty(): 
            cur=self.head
            for i in range(0,self.sizes): 
                if cur.data==data:
                    return 'Found'
                cur=cur.next  
            else:
                return 'NOT FOUND' 
    def addhead(self,data):
        if not self.isEmpty():
            n=Node(data)
            cur=self.head
            n.next=cur
            self.head=n
            self.sizes+=1
        else:
            n=Node(data)
            self.head=n
            self.sizes+=1
it=Singlylinklist()
it.addhead('kijuh')
it.append(1)
it.append(2)
print(it)
it.pop(-999)
print(it)
