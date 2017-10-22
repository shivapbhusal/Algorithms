# A simple python implementation of stack

class Stack:   # Creation of a stack class 

    def __init__(self): # constructor that creates myStack, an empty list. 
        self.mystack=[]

    def is_empty(self):     # If the stack is empty, return False Else Return True 
        return self.size()==0
         
    def push(self, x):      # Append item at the end of the list 
        self.mystack.append(x) 

    def pop(self):
    	return self.mystack.pop()  # Pop the last element of the List

    def size(self):              # Return the length of the List 
        return len(self.mystack)

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)

size=int(s.size())
while (size>0):
	item=s.pop()
	print(item)
	size=int(s.size()) 
            

