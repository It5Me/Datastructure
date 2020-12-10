class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        pass
    def insert(self,root,data):
        if root==None:
            root=Node(data)
            return root
        else:
            if data<root.data:
                root.left=self.insert(root.left,data)
            else:
                root.right=self.insert(root.right,data)
        return root
    def print_tree(self,root,level=0):
        if root!=None:
            self.print_tree(root.right,level+1)
            print('     '*level,root)
            self.print_tree(root.left,level+1)
T=BST()
root=None
inp=list(map(int,input("Enter Input : ").split()))
for i in inp:
    root=T.insert(root,i)
T.print_tree(root)



