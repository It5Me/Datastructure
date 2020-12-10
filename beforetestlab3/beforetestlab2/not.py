class DummyDoublyLinklist:
    class Node:
        def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None
    def __init__(self):
        self.head=self.Node(None)
        self.tail=self.head
        self.size=0
    def isEmpty(self):
        return self.size==0
    def __len__(self):
        return self.size
    def __str__(self):
        cur=self.head.next
        s=''
        while cur!=None:
            s+=str(cur.data)+' '
            cur=cur.next
        return s
    def append(self,data):
        cur=self.tail
        n=self.Node(data)
        cur.next=n
        n.prev=cur
        self.tail=n
        self.size+=1
    def indexOf(self,data):
        cur=self.head.next
        count=0
        while cur!=None:
            if cur.data==data:
                return count
            cur=cur.next
            count+=1
        return -1
    def insert(self,index,data):
        cur=self.head
        n=self.Node(data)
        if index<0:
            index=index+self.size
        for i in range(index):
            cur=cur.next
        n.next=cur.next
        n.prev=cur
        if cur.next!=None:
            cur.next.prev=n
        else:
            self.tail=n
        cur.next=n
        self.size+=1
    def nodedAt(self,data):
        cur=self.head
        while cur!=None:
            if cur.data==data:
                return  cur
            cur=cur.next
        return 'Not'
    def pop(self,index):
        if 0<=index<=self.size-1:
            cur=self.head
            for i in range(index):  
                cur=cur.next       
            cur.next=cur.next.next
            if cur.next!=None:
                cur.next.prev=cur
            else:
                self.tail=cur
            self.size-=1
    def remove_all(self,data):
        cur=self.head.next
        i=0
        while cur!=None:
            if cur.data==data:
                self.pop(i)
                i-=1
                cur=cur.prev
            i+=1
            cur=cur.next
    def remove(self,data):
        cur=self.head.next
        count=0
        while cur!=None:
            if cur.data==data:
                self.pop(count)
                return
            cur=cur.next
            count+=1
    def removedup(self):
        cur=self.head.next
        temp=DummyDoublyLinklist()
        while cur!= None:
            if temp.indexOf(cur.data)==-1:
                temp.append(cur.data)
            self.remove(cur.data)
            cur=cur.next
        temp_cur=temp.head.next
        while temp_cur!=None:
            self.append(temp_cur.data)
            temp_cur=temp_cur.next
        return str(self)
            
it=DummyDoublyLinklist()
it.insert(0,1)
it.append(2)
it.append(3)
print(it)
it.insert(3,'eoeo')
print(it)



 