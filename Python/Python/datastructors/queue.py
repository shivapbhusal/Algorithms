# A simple python implementation of Queue

class Queue:   # Creation of a Queue class 

    def __init__(self): # constructor that creates myStack, an empty list. 
        self.myqueue=[]

    def is_empty(self):     # If the Queue is empty, return False Else Return True 
        return self.size()==0
         
    def enqueue(self, x):      # Append item at the end of the list 
        self.myqueue.insert(0,x) 

    def dequeue(self):
    	return self.myqueue.pop()  # Pop the last element of the List

    def size(self):              # Return the length of the List 
        return len(self.myqueue)

s=Queue()
for i in range(1,11):
    s.enqueue(i)

size=int(s.size())
while (size>0):
	item=s.dequeue()
	print(item)
	size=int(s.size()) 
            

