# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Dummy:
#     def __init__(self):
#         n=Node(None)
#         self.head=n
#         self.sizes=0
#     def isEmpty(self):
#         return self.sizes==0
#     def size(self):
#         return   self.sizes
#     def append(self,data):
#         n=Node(data)
#         cur=self.head
#         while cur.next!=None:
#             cur=cur.next
#         cur.next=n
#         self.sizes+=1
#     def insert(self,index,data):
#         cur=self.head
#         n=Node(data)
#         if 0<index<=self.sizes:
#             count=0
#             while count<index:
#                 cur=cur.next
#                 count+=1
#             n.next=cur.next
#             cur.next=n
#             self.sizes+=1
#         elif index==0:
#             n.next=self.head.next
#             self.head.next=n
#             self.sizes+=1
#     def index(self,data):
#         cur=self.head.next
#         for i in range(self.sizes):
#             if cur.data==data:
#                 return i
#         else:
#             return "NotFound"
#     def pop(self,index=None):
#         if not self.isEmpty():   
#             if index==None:
#                 cur=self.head.next
#                 while cur.next.next!=None:
#                     cur=cur.next
#                 cur.next=None
#                 self.sizes-=1

#             elif 0<=index<self.sizes-1:
#                 cur=self.head
#                 count=0
#                 while count<index: 
#                     cur=cur.next
#                     count+=1
#                 cur.next=cur.next.next
#                 self.sizes-=1
#     def lookBack(self):
#         cur=self.head
#         while cur.next!=None:
#             cur=cur.next
#         return cur.data
#     def lookFront(self):
#         cur=self.head.next
#         if cur!=None:
#             return cur.data  
#         else:
#             return None  
#     def __str__(self):
#         st=''
#         cur=self.head.next
#         while cur !=None:
#             st+=str(cur.data)+' '
#             cur=cur.next
#         return st
   
# class stack:
#     def __init__(self):
#         self.s = Dummy()
#     def push(self,data):
#         self.s.append(data)
#     def pop(self):
#         s=self.s.lookBack()
#         self.s.pop()
#         return s 
#     def peek(self):
#         return self.s.lookBack()
#     def __str__(self):
#         return str(self.s)
#     def isEmpty(self):
#         return self.s.isEmpty()
#     def size(self):
#         return self.s.size()


# class Queue:
#     def __init__(self):
#         self.q = Dummy()
#     def enque(self,data):
#         self.q.append(data)
#     def deque(self):
#         s=self.q.lookFront()
#         self.q.pop(0)
#         return q 
#     def front(self):
#         return self.q.lookFront()
#     def __str__(self):
#         return str(self.q)
#     def isEmpty(self):
#         return self.q.isEmpty()
#     def size(self):
#         return self.q.size()

class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sizes = 0
    def __str__(self):
        st=''
        cur=self.head
        while cur!=None:
            st+=str(cur.data)+' '
            cur=cur.next
        return st
    def reverse(self):
        st=''
        cur=self.tail
        while cur!=None:
            st+=str(cur.data)+' '
            cur=cur.prev
        return st
    def pushBack(self,data):
        n=Node(data)
        cur=self.tail
        n.prev=cur.prev
        n.next=cur
        cur.prev.next=n
        cur.prev=n
        self.sizes+=1
    def pushFront(self,data):
        n=Node(data)
        cur=self.head
        n.next=cur.next
        n.prev=cur
        cur.next.prev=n
        cur.next=n
        self.sizes+=1
    def insert(self,index,data):
        cur=self.head
        n=Node(data)
        for i in range(index):
            cur=cur.next
        n.next=cur.next
        n.prev=cur
        cur.next.prev=n
        cur.next=n
        self.sizes+=1
    def pop(self,index):
        if 0<=index<=self.sizes-1:
            cur=self.head
            count=0
            while count!=index:
                cur=cur.next
                count+=1
            cur.next=cur.next.next
            cur.next.prev=cur
            self.sizes-=1    
    def length(self):
        return self.sizes
    def isEmpty(self):
        return self.sizes==0
    def search(self,data):
        cur=self.head.next
        for i in range(self.sizes):
            if cur.data==data:
                return i
            cur=cur.next
        else:
            return 'Not Found'       
    def index(self,index):
        cur=self.head.next
        for i in range(index): 
            cur=cur.next
        return cur.data
    def clear(self):
        self.head = Node()
        self.tail = Node()
        self.sizes = 0


