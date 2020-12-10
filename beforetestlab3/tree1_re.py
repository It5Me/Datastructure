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
            print('*')
            root=Node(data)
        else:
            if data>root.data:
                print('R',end='')
                root.right=self.insert(root.right,data)
            else:
                print('L',end='')
                root.left=self.insert(root.left,data)
        return root
    def print_tree(self,root,level=0):
        if root!=None:
            self.print_tree(root.left,level+1)
            print('     '*level,root)
            self.print_tree(root.right,level+1)
T = BST()
root=None
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(root,i)
T.print_tree(root)
