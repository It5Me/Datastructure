class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
        self.previous=None
class Linklist:
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
                cur.next.previous=n
                cur.next=n
                self.sizes+=1
            elif pos == 0:
                self.addHead(item)
            elif pos>self.sizes-1:
                self.append(item)
        
    def search(self, item):
        cur=self.head
        while cur!=None:
            if cur.value==item:
                return self.index(item)
            cur=cur.next
               
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
    def inp(self,i,j=None):
        if i=='I':
            if self.isEmpty():
                self.head=Node(j)
                self.tail=Node("|")
                self.head.next=self.tail
                self.tail.previous=self.head
                self.sizes+=2  
            else:
                self.insert(self.search('|'),j)
                # print(self.tail.value)
                # print(self.head.next.value)              
        elif i=='L':
            if self.sizes!=0:
                inde=self.search('|')
                if inde >0:
                    self.pop(inde)
                    self.insert(inde-1,'|')       
        elif i=='R':
            if self.sizes!=0:
                inde=self.search('|')
                self.pop(inde)
                self.insert(inde+1,'|')
            else:
                self.append('|')    
            
        elif i=='B':
            if self.sizes!=0:
                inde=self.search('|')
                self.pop(inde-1)
            else:
                self.append('|')        
        elif i=='D':
            if self.sizes!=0:
                inde=self.search('|')
                self.pop(inde+1)
            else:
                self.append('|')        
inp=input("Enter Input : ").split(',')

it=Linklist()
for i in inp: 
    ke=i.split()[0]
    if len(i.split())>1:
        wor=i.split()[1]
        it.inp(ke,wor)
    else:
        it.inp(ke)    
print(it)    


                    

