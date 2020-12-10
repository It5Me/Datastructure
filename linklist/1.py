class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
        if self.head==None:
            self.head=n
            self.sizes+=1
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=n
            self.sizes+=1
    def insert(self,index,data):
        if 0<=index<=self.sizes:
            if self.head == None or index==self.sizes:
                self.append(data)
            elif index==0:
                cur=self.head
                self.head=Node(data)
                self.head.next=cur
            else:    
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                q = Node(data)
                q.next = cur.next
                cur.next=q
            print("index = {} and data = {}".format(index,data))
            self.sizes+=1
        else:
            print("Data cannot be added")
    def __str__(self):
        if self.isEmpty():
            return 'List is empty'
        else:
            cur=self.head
            s="link list : "
            while cur.next !=None:
                s+=str(cur.data) + '->'
                cur=cur.next
            s+=str(cur.data)    
            return s
inp=input("Enter Input : ").split(',')
it=Linklist()
for i in inp[0].split(): #keepdatafirst
    it.append(i)
for i in range(1,len(inp)):
    s = inp[i].strip().split(':')
    print(it)
    it.insert(int(s[0]),s[1])
it.insert(3,'3')    
print(it)







                    



    


