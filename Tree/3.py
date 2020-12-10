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
T=BST()
T1=BST()
inp=input("Enter Input : ").split('/')
for i in inp[0].split():
    root1=T1.insert(int(i))
T1.printTree(root1)
print('--------------------------------------------------')
for i in inp[0].split():
    if int(i)>int(inp[1]):
        root = T.insert(int(3*int(i)))
    else:
        root = T.insert(int(i))
T.printTree(root)





