'''
Python implementation of Binary tree 
Author: Shiva Bhusal, BGSU
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def updateLeft(self, left):
        self.left=left

    def upDateRight(self, right):
        self.right=right
    
    def updateParent(self, parent):
        self.parent=parent

class BinaryTree:
    def __init__(self,root):
        self.root=root

    def addNode(self, newNode):
        if root.right==None and root.left==None:
            if newNode.data>root.data:
                root.left=newNode
            else:
                root.right=newNode
        else:
            current=root


b=Node(1)
#print(b.root)
