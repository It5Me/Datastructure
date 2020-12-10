class DummyDoublyLinkList:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
    def __init__(self):
        self.head=self.Node(None)
        self.tail=self.head
        self.sizes=0
    def __str__(self):
        s=''
        cur=self.head.next
        while cur.next!=None:
            s+=str(cur.data)+'->'
            cur=cur.next
        s+=str(cur.data)
        return s
    def __len__(self):
        return self.sizes
    def isEmpty(self):
        return self.sizes==0
    def append(self,data):
        cur=self.tail
        n=self.Node(data)
        cur.next=n
        n.prev=cur
        self.tail=n
        self.sizes+=1
    def pop(self,index):
        cur=self.head
        if 0<=index<=self.sizes-1:
            for i in range(-1,index-1):
                cur=cur.next
            cur.next=cur.next.next
            if cur.next!=None:
                cur.next.prev=cur
            else:
                self.tail=cur
            self.sizes-=1         
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
    def insert(self,index,data):
        cur=self.head
        if index<=self.sizes:
            if index<0 :
                index=index+self.sizes
            for i in range(index):
                cur=cur.next
            n=self.Node(data)
            n.next=cur.next
            n.prev=cur
            if cur.next!=None:
                cur.next.prev=n
            else:
                self.tail=n
            cur.next=n
            self.sizes+=1
    def addsort(self,data):
        cur=self.head.next
        count=0
        while cur!=None:
            if data>cur.data:
                cur=cur.next
                count+=1
            else:
                self.insert(count,data)
                return
        self.append(data)
    def nodeAt(self,index):
        cur=self.head
        for i in range(-1,index): 
            cur=cur.next
        return cur.data
    def findMin(self):
        return self.nodeAt(0)
    def findmean(self):
        cur=self.head.next
        summ=0
        while cur!=None:
            summ+=cur.data
            cur=cur.next
        return summ/self.sizes
    def findMode(self):
        check=[0]*100
        cur=self.head.next
        while cur!=None:
            check[cur.data]+=1
            cur=cur.next
        m=-999
        for i in range(len(check)):
            if check[i]>m:
                m=check[i]
        if m==1:
            return 'not'
        else:
            s=''
            for  i in range(len(check)):
                if check[i]==m:
                    print('i',check[i])
                    s+=str(i)
            return ','.join(s)
    def findMedian(self):
        su=0
        if (self.sizes)%2==0:
            a=self.nodeAt((self.sizes//2)-1)
            n=self.nodeAt(self.sizes//2)
            su=(n+a)/2
            return su
        else:
            su=self.nodeAt(self.sizes//2)
            return su

it=DummyDoublyLinkList()
inp=list(map(int,input("Enter Input : ").split()))
for i in inp:
    it.addsort(i)
print(it)
print('min',it.findMin())
print('mean',it.findmean())
print('mode',it.findMode())
print('median',it.findMedian())
