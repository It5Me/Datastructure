def deleteNode(self,root,key):
        if root==None:
            return root
        if key<root.data:
            root.left=self.deleteNode(root.left,key)
        elif key>root.data:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None:
                temp=root.right
                root=None
                return temp
            elif root.right==None:
                temp=root.left
                root=None
                return temp
            temp=self.minValue(root.right)
            root.data=temp.data
            root.right=self.deleteNode(root.right,temp.data)
        return root