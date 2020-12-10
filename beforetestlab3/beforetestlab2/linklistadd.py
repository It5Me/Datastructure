class Linklist:
    class Node:
        def __init__(self,data,next=None):
            self.data=data
            if next==None:
                self.next=None
            else:
                self.next=next
    def __init__(self):
        self.head=self.Node(None,None)
        self.sizes=0
    def __str__(self):
        s='LinkList data : '
        p=self.head.next
        while p!=None:
            s+=str(p.data)+' '
            p=p.next
        return s
    def size(self):
        return self.sizes
    def isEmpty(self):
        return self.sizes==0
    def indexOf(self,data):
        q=self.head.next
        for i in range(self.sizes):
            if q.data==data:
                return i
            else:
                q=q.next
        return -1
    def isIn(self,data):
        return self.indexOf(data)<=0 # return true when notfound
    def nodeAt(self,ind):
        p=self.head
        for j in range(-1,ind):
            p=p.next
        return p
    def append(self,data):
        self.insertAfter(self.sizes,data)
    def insertAfter(self,i,data):
        p=self.nodeAt(i-1)
        p.next=self.Node(data,p.next)
        self.sizes+=1
    def addsort(self,data):
        if not self.isEmpty():
            i=0
            p=self.head.next
            for i in range(self.sizes):
                if data>p.data:
                    p=p.next
                    i+=1
                else:
                    self.insertAfter(i,data)
                    return
        self.append(data)
    def deleteAfter(self,i):
        if 0<=i<self.sizes-1:
            p=self.nodeAt(i)
            p.next=p.next.next
            self.sizes-=1
    def removeDup(self):
        p=self.head.next
        i=0
        while p!=None and p.next!=None:
            if p.data==p.next.data:
                p=p.next
                print('i',i)
                self.deleteAfter(i)

            else:
                p=p.next
                i+=1
    def findMean(self):
        summ=0
        n=0
        p=self.head.next
        while p!=None:
            summ+=p.data
            n+=1
            p=p.next
        return summ/n
    def findeMode(self):
        check=[0]*100
        p=self.head.next
        while p!=None:
            check[p.data]+=1
            p=p.next
        mx=-1
        index=0
        for i in range(len(check)):
            if check[i]>mx:
                mx=check[i]
                index=i
        st=''
        if  not mx==1:
            for i in range(len(check)):
                if check[i]==mx:
                    print(i)
                    st+=str(i)
            return ', '.join(st)           
        else:
            return 'Mode is not avilable'
    def findeMedian(self):
        if self.sizes%2==0:
            n=self.sizes
            p=self.nodeAt(n//2).data
            q=self.nodeAt((n//2)-1).data
            summ=(p+q)/2
            return summ
        else:
            n=self.sizes
            p=self.nodeAt(n//2).data
            return p
         
inp=list(map(int,input("Enter Input :").split()))
it=Linklist()

for x in inp:
    it.addsort(x)
print(it)
it.removeDup()
print(it)
print('Mean %.2f' % it.findMean())
print('Mode',it.findeMode())
print('Median',it.findeMedian())

