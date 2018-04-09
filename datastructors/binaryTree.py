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
    def __init__(self,root):
        self.root=None

    def addNode(self, data):
        newNode=Node(data)

        if self.root==None:
            root=newNode
        else:
            current=root
            while(current!=None):
                if current.data>data:
                    current=current.right
                else:
                    current=current.left

            if current.parent<data:
                current.right=newNode
            else:
                current.left=newNode

    def traverse(self):
        current=self.root
        print(current.data)

b=BinaryTree(None)

for i in range(10):
    b.addNode(i)

print(b.root)



