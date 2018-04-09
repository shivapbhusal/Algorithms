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
        self.root=None

    def addNode(self, z):
        '''
        Adds Node 
        '''
        y=None 
        x=self.root
        newNode=Node(z)

        while x is not None:
            y=x
            if z<x.data:
                x=x.left
            else:
                x=x.right
        newNode.parent=y

        if y is None:
            self.root=newNode
            print("Root added")
        else:
            if z<y.data:
                y.left=newNode
            else:
                y.right=newNode

    def traverse(self,current):
        if current!=None:
            self.traverse(current.left)
            print(current.data)
            self.traverse(current.right)

b=BinaryTree()

for i in [5,6,0,10,8,2]:
    b.addNode(int(i))
    print(str(i)+ "added")

b.traverse(b.root)



