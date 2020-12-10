
class Linklist:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    def __init__(self):
        self.head=None
        self.sizes=0
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def insert(self,index,data):
        if 0<=index<=self.sizes:
            n=self.Node(data)
            if self.isEmpty():
                self.append(n)
            else:
                if index==0:
                    cur=self.head
                    n.next=cur
                    self.head=n
                elif index==self.sizes:
                    self.append(n)
                else:
                    cur=self.head
                    for i in range(index-1):
                        cur=cur.next
                    n.next=cur.next
                    cur.next=n
            self.sizes+=1
        else:
            return print('Can not Add')
    def append(self,data):
        n=self.Node(data)
        cur=self.head
        if  not self.isEmpty():
            for i in range(self.sizes-1):
                cur=cur.next
            cur.next=n
            self.sizes+=1
        else:
            self.head=n
    def __str__(self):
        cur=self.head
        s=''
        while cur!=None:
            s+=str(cur.data)+' '
            cur=cur.next
        return s
inp=input("Enter Input : ").split(',')
link=Linklist()
for i in inp[0].split():
    link.append(i)
for i in range(1,len(inp)):
    s=inp[i].strip().split(':')
    print(s)
    link.insert(int(s[0]),s[1])
print(link)
    
