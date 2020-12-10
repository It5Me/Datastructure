class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None
        self.keepstr=''
    def insert(self,data):
        n=Node(data)
        self.keepstr=''
        if self.root==None:
            self.root=n
        else:
            cur=self.root
            while cur!=None:
                if data<cur.data:
                    self.keepstr+='L'
                    if cur.left==None:
                        cur.left=n
                        break
                    else:
                        cur=cur.left
                else:
                    self.keepstr+='R'
                    if cur.right==None:
                        cur.right=n
                        break
                    else:
                        cur=cur.right
        self.keepstr+='*'
    def print_str(self):
        return self.keepstr
T=BST()
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=T.insert(i)
    print(T.print_str())



