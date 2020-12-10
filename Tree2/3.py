class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
    def __str__(self):
        return str(self.data)
class BTS:
    def __init__(self):
        self.keeprank=[]
    def insert(self,root,data):
        if root==None:
            root=Node(data)
        elif data<root.data:  
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def rank(self,root):
        if root!=None:
            self.rank(root.left)
            self.keeprank.append(root.data)
            self.rank(root.right)
        return self.keeprank
    def getrankNotin(self,f):
        count=-1
        for i in self.keeprank:
            count+=1
            if str(i)==f:
                return count
    def getrankin(self,f):
        count=0
        for i in self.keeprank:
            count+=1
            if str(i)==f:
                return count
root=None
T=BTS()
inputs=input('Enter Input : ').split('/')
f=inputs[1]
for i in inputs[0].split():
    root=T.insert(root,int(i))
T.printTree(root)
if not f in inputs[0].split():
    root=T.insert(root,int(f))
    print('--------------------------------------------------')
    T.rank(root)
    print('Rank of {} : {}'.format(f,T.getrankNotin(f)))
else:
    print('--------------------------------------------------')
    T.rank(root)
    print('Rank of {} : {}'.format(f,T.getrankin(f)))


