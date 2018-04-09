'''
Python implementation of Binary tree 
Author: Shiva Bhusal, BGSU
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None

class BinaryTree:
    def __init__(self):
        self.root=Node(None)

    def addNode(self, x):
        newNode=Node(x)
        current=self.root

        if self.root==None:
            self.root=newNode
        else:
            while(current.data!=None):
                if x<current.data:
                    current=current.left
                else:
                    current=current.right

            newNode.parent=current
            if x<current.data:
                current.left=newNode
                #print(current.data)
            else:
                current.right=newNode
                #print(current.data)

    def traverse(self,current):
        if current!=None:
            self.traverse(current.left)
            print(current.data)
            self.traverse(current.right)

b=BinaryTree()

for i in [5,6,0,10,8,2]:
    b.addNode(i)

b.traverse(b.root)



