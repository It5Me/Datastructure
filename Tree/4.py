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
    def printInorder(self,node,level=0):
        if node!=None:
            self.printInorder(node.left,level+1)
            print(node,end=' ')
            self.printInorder(node.right,level+1)
    def printPreorder(self,node,level=0):
        if node!=None:
            print(node,end=' ')
            self.printPreorder(node.left,level+1)
            self.printPreorder(node.right,level+1)
    def printPosorder(self,node,level=0):
        if node!=None:
            self.printPosorder(node.left,level+1)
            self.printPosorder(node.right,level+1)
            print(node,end=' ')
    def printBreath(self,root,level=0):
            queue=Queue()
            queue.enQ(root)
            while not queue.isEmpty():
                n=queue.deQ()
                print(n.data,end=' ')
                if n.left!=None:
                    queue.enQ(n.left)
                if n.right!=None:
                    queue.enQ(n.right)
            
                            
class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def enQ(self,data):
        self.items.append(data)
    def deQ(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items==[]  
T=BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Preorder : ',end='')
T.printPreorder(root)
print('')
print('Inorder : ',end='')
T.printInorder(root)
print('')
print('Postorder : ',end='')
T.printPosorder(root)
print('')
print('Breadth : ',end='')
T.printBreath(root)
