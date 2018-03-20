''' 
Python Implementation of Shunting Yard Algorithm 
Author: Shiva Bhusal 
Bowling Green State University
'''

class Stack:

    def __init__(self):
        self.mystack=[]

    def is_empty(self): 
        return self.size()==0
         
    def push(self, x):
        self.mystack.append(x) 

    def pop(self):
    	return self.mystack.pop()

    def size(self):
        return len(self.mystack)

    def checkTop(self):
    	return self.mystack[len(self.mystack)-1]

class Queue:

    def __init__(self):
        self.myqueue=[]

    def is_empty(self):
        return self.size()==0
         
    def enqueue(self, x):
        self.myqueue.insert(0,x) 

    def dequeue(self):
    	return self.myqueue.pop()

    def size(self):
        return len(self.myqueue)

inputString="2+4+5+10"
outputQueue=Queue()
operatorStack=Stack()
for tokens in inputString:
    if tokens.isnumeric():
    	outputQueue.enqueue(tokens)
    elif tokens in ['*','/','+','-']:
    	'''check whether the operator in operator stack is of higher precedence
    	'''
    	operatorStack.push(tokens)
    elif tokens=='(':
    	operatorStack.push(tokens)
    elif tokens==')':
    	operatorStack.push(tokens)


