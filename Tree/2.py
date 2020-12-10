class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        n=Node(data)
        cur=self.root
        if self.root==None:
            self.root=n
        else:
            while cur!=None:
                if data<cur.data:
                    if cur.left==None:
                        cur.left=n
                        break
                    else:
                        cur=cur.left
                else:
                    if cur.right==None:
                        cur.right=n
                        break
                    else:
                        cur=cur.right
        return self.root
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     ' * level, node)
            self.printTree(node.left,level+1)
    def findMin(self):
        mi=99999
        cur=self.root
        while cur!=None:
            if cur.data<mi:
                mi=cur.data
                cur=cur.left
            else:
                cur=cur.left
        return mi
            
    def findMax(self):
        ma=-1
        cur=self.root
        while cur!=None:
            if cur.data>ma:
                ma=cur.data
                cur=cur.right
            else:
                cur=cur.right
        return ma
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Min :',T.findMin())
print('Max :',T.findMax())

    