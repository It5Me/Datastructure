class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes= 0
    def __str__(self):
        if self.isEmpty():
            return ''
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    def isEmpty(self):
        return self.head == None
    def appendlinklist(self, item):
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
    def size(self):
        return self.sizes
    def pop(self, pos):
        cur=self.head
        if pos<0 or pos>self.sizes-1:
            return 'Out of Range'
        elif pos==0:
            if self.head.next!=None:
                self.head.next.previous=self.head.previous
            self.head=self.head.next
            self.sizes-=1
            return 'Success'
        elif pos==self.sizes-1:
            if self.tail.previous!=None:
                self.tail.previous.next=self.tail.next
            self.tail=self.tail.previous
            self.sizes-=1
            return 'Success'
        else:
            cur=self.head
            for i in range(pos-1):
                cur =cur.next
            cur.next.next.previous=cur
            cur.next=cur.next.next
            self.sizes-=1
            return 'Success'
            

inp=list(map(int,input("Enter Input : ").split()))
li=[]
li2=[]
temp=[[] for i in range(10)]
for i in range(10):
    li.append(LinkedList())
for i in inp:
    if i<0: 
        temp[(-i)%10].append(i)
    else:
        temp[i%10].append(i)
for i in range(10):
    for j in sorted(temp[i]):
        li[i].appendlinklist(j)
temp=[[] for i in range(10)]
print('------------------------------------------------------------\nRound : 1')
for i in range(10):
    print('{} : {}'.format(i,li[i]))
r=2
c=10
while li[0].sizes!=len(inp):
    for i in range(10):
        li2.append(LinkedList())    
    for i in li:
        for j in str(i).split():
            if int(j)<0:
                temp[((-int(j))//c)%10].append(int(j))
            else:
                temp[(int(j)//c)%10].append(int(j))
    for j in range(10):
        for k in sorted(temp[j]):
            li2[j].appendlinklist(k)
    temp=[[] for i in range(10)]
    print('------------------------------------------------------------\nRound : {}'.format(r))
    for i in range(10):
        print('{} : {}'.format(i,li2[i]))
    li=li2.copy()
    li2.clear()
    c=c*10
    r+=1
print("------------------------------------------------------------\n{} Time(s)".format(r-2))
print('Before Radix Sort : {}'.format(' -> '.join(map(str,inp))))
print('After  Radix Sort : {}'.format(str(li[0]).strip().replace(' ',' -> ')))
