class DummyDoublyLinklist:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
    def __init__(self):
        self.head=self.Node(None)
        self.tail=self.head
        self.size=0
    def __str__(self):
        cur=self.head.next
        s=''
        while cur!=None:
            s+=str(cur.data)+' '
            cur=cur.next
        return s
    def reversestr(self):
        cur=self.tail
        s=''
        while cur!=None and cur.prev!=None:
            s+=str(cur.data)+' '
            cur=cur.prev
        return s
    def __len__(self):
        return self.size
    def insert(self,index,data):
        n=self.Node(data)
        cur=self.head
        if index<0:
            index=index+self.size
        for i in range(index):
            cur=cur.next
        n.prev=cur
        n.next=cur.next
        if cur.next!=None:
            cur.next.prev=n
        else:
            self.tail=n
        cur.next=n
        self.size+=1
    def append(self,data):
        self.insert(len(self),data)
    def indexOf(self,data):
        cur=self.head.next
        count=0
        while  cur!=None:
            if cur.data==data:
                return count
            else:
                cur=cur.next
                count+=1
        return -1
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
    def remove(self,data):
        cur=self.head.next
        count=0
        while cur!=None:
            if cur.data==data:
                self.pop(count)
                return
            else:
                cur=cur.next
                count+=1
    def remove_all(self,data):
        cur=self.head.next
        count=0
        while cur!=None:
            if cur.data==data:
                self.pop(count)
                count-=1
                cur=cur.prev
            else:
                cur=cur.next
                count+=1   
    def removedup(self):
        cur=self.head.next
        temp=DummyDoublyLinklist()
        while cur!=None:
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
it.append(5)
it.append(4)
it.append(4)
print(it)
it.removedup()
print(it)
it.remove(5)
print(it)
print(it.reversestr())

    
            