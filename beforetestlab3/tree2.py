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
    def insert(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            cur=self.root
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
    def print_tree(self,node,level=0):
        if node!=None:
            self.print_tree(node.right,level+1)
            print('     '*level,node)
            self.print_tree(node.left,level+1)
inp =list(map(int,input("Enter Input : ").split()))
T=BST()
for i in inp:
    root=T.insert(i)
T.print_tree(root)

            


