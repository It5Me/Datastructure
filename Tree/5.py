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
    def printinfix(self,inp):
        stack=Stack()
        for i in inp[0]:
            if i in '-*/+':
                after=stack.pop()
                # print(after)
                before=stack.pop()
                # print(before)
                temp=str('('+str(before)+str(i)+str(after)+')')
                stack.push(temp)
            else:
                print(i)
                stack.push(str(i))
        return str(stack)
    def printPrefix(self,inp):
        stack=Stack()
        for i in inp[0]:
            if i in '-*/+':
                stack.push(str(i))
            else:
                after=stack.pop()
                before=stack.pop()
                temp=str(+str(before)+str(i)+str(after)+')')
                stack.push(temp)
        return str(stack)
    def printInorder(self,node,level=0):
        if node!=None:
            if node.right and node.left:
                print('(',end='')
            self.printInorder(node.left,level+1)
            print(node,end='')
            self.printInorder(node.right,level+1)
            if node.right and node.left:
                print(')',end='')
    def printPreorder(self,node,level=0):
        if node!=None:
            print(node,end='')
            self.printPreorder(node.left,level+1)
            self.printPreorder(node.right,level+1)
    def appendByposfix(self,inp):
        operation=Stack()
        for i in inp[0]:
            # print(i)
            if i in '*-+/':
                after=operation.pop()
                before=operation.pop()
                operation.push(Node(i,before,after))
            else:
                operation.push(Node(i))
        self.root=operation.pop()
        return self.root
class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return self.items==[]
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return ''.join(self.items)
T = BST()
inp =  input('Enter Postfix : ').split()
root=T.appendByposfix(inp)
print('Tree :')
T.printTree(root)
print('--------------------------------------------------')
print('Infix :', end=' ')
T.printInorder(root)
print('')
print('Prefix :', end=' ')
T.printPreorder(root)
