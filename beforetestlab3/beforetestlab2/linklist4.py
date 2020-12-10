class LinkList:
    class Node:
        def __init__(self,data):
            self.prev=None
            self.next=None
            self.data=data
    def __init__(self):
        self.head=None
        self.tail=None  
        self.sizes=0
    def __str__(self):
        st=''
        if not self.isEmpty():
            cur=self.head
            while cur!=None:
                st+=str(cur.data)+' '
                cur=cur.next
            return st
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.sizes
    def append(self,data):
        if not self.isEmpty():
            n=self.Node(data)
            cur=self.tail
            n.prev=cur
            cur.next=n
            self.tail=n
        else:
            self.head=self.tail=self.Node(data)
        self.sizes+=1
    def indexOf(self,data):
        cur=self.head
        count=0
        while cur!=None:
            if cur.data==data:
                return count
            count+=1
            cur=cur.next
        return print('Not Found')
    def pop(self,index):
        if not self.isEmpty():
            if 0<=index<=self.sizes-1:
                if index==0:
                    cur=self.head
                    self.head=cur.next
                    cur.prev=None
                elif index==self.sizes-1:
                    cur=self.tail
                    self.tail=cur.prev
                    self.tail.next=None
                else:
                    cur=self.head
                    for i in range(index-1):
                        cur=cur.next
                    cur.next.next.prev=cur
                    cur.next=cur.next.next
                self.sizes-=1
    def insert(self,index,data):
        n=self.Node(data)
        if not self.isEmpty():
            if index==0:
                cur=self.head
                n.next=cur
                n.prev=None
                cur.prev=n
                self.head=n
                self.sizes+=1
            elif index==self.sizes:
                self.append(data)
            else:
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                n.prev=cur
                n.next=cur.next
                cur.next.prev=n
                cur.next=n
                self.sizes+=1
        else:
            self.append(data)
inp=input("Enter Input : ").split(',')
vim=LinkList()
cou=0
vim.append('|')  
for i in inp:
    if i.split()[0].startswith('I'):
        if vim.isEmpty():
            vim.append(i.split()[1])
            vim.append('|')
        else:
            vim.insert(vim.indexOf('|'),i.split()[1])
    elif i.split()[0].startswith('L'):
        temp=vim.indexOf('|')
        if temp !=0:
            vim.pop(temp)
            vim.insert(temp-1,'|')
    elif i.split()[0].startswith('R'):
        temp=vim.indexOf('|')
        if temp!=vim.size()-1:
            vim.pop(temp)
            vim.insert(temp+1,'|')
    elif i.split()[0].startswith('B'):
        temp=vim.indexOf('|')
        vim.pop(temp-1)
    elif i.split()[0].startswith('D'):
        temp=vim.indexOf('|')
        vim.pop(temp+1)
print(vim)