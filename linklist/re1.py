class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
        self.sizes=0
    def __isEmpty(self):
        return self.sizes==0
    def append(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
            self.sizes+=1 
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=n
            self.sizes+=1
    def insert(self,index,data):
        if index>=0:
            if self.sizes!=0  and 0<index<=self.sizes :
                current=self.head
                for i in range(index-1):
                    current=current.next
                n=Node(data)
                n.next=current.next
                current.next=n
            elif index==0:
                cur=self.head
                self.head=Node(data)
                self.head.next=cur
            elif self.sizes==0:
                self.head=Node(data)
            self.sizes+=1
        else:
            print("Data cannot be added")
    def __str__(self):
        if self.sizes==0:
             return "List is empty"
        else:
            s="Link list "
            cur =self.head
            while cur.next !=None:
                s+=str(cur.data)+' '
                cur=cur.next
            s+=str(cur.data)+' '    
               
            return s    
                


it=Linklist()
it.append(5)
it.append(1)
it.insert(2,100)
it.insert(1,333)
it.insert(0,2222)
print(it)



            