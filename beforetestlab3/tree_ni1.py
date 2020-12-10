class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def __str__(self):
        return ' '.join(self.items)
    def isEmpty(self):
        return self.items==[]
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
    def insert(self,root,data):
        if root==None:
            root=Node(data)
            return root
        else:
            if data<root.data:
                root.left=self.insert(root.left,data)
                return root
            else:
                root.right=self.insert(root.right,data)
                return root
        return root
    def print_tree(self,root,level=0):
        if root!=None:
            self.print_tree(root.right,level+1)
            print('     '*level,root.data)
            self.print_tree(root.left,level+1)
    def in_order(self,root):
        if root!=None:
            self.in_order(root.left)
            print(root.data,end=' ')
            self.in_order(root.right)
    def preorder(self,root):
        if root!=None:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def posorder(self,root):
        if root!=None:
            self.posorder(root.left)
            self.posorder(root.right)
            print(root.data,end=' ')
    def print_levelorder(self,root):
        if root!=None:
            queue=Queue()
            queue.enqueue(root)
            while not queue.isEmpty():
                n=queue.dequeue()
                print(n.data,end=' ')
                if n.left!=None:
                    queue.enqueue(n.left)
                if n.right!=None:
                    queue.enqueue(n.right)          
T=BST()
root=None
inp=list(map(int,input('Enter some numbers : ').split()))
for i in inp:
    root=T.insert(root,i)
T.print_tree(root)
print("Inorder")
T.in_order(root)
print('')
print("Preorder")
T.preorder(root)
print('')
print("Posorder")
T.posorder(root)
print('')
print('Travel ')
T.print_levelorder(root)

