class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.m=0
        self.mi=0
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
    def findMax(self,root):
        if root.right==None:
            return self.m
        else:
            self.m=root.right.data
            return self.findMax(root.right)
    def findemin(self,root):
        if root.left==None:
            return root.data
        else:
            return self.findemin(root.left)
    # def findemin(self,root):
    #     if root.left==None:
    #         return self.mi
    #     else:
    #         self.mi=root.left.data
    #         return self.findemin(root.left)
       
T=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=T.insert(root,i)
T.print_tree(root)
print(T.findMax(root))
print(T.findemin(root))
