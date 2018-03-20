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

    def getTop(self):
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

def checkPrecedence(op1, op2):
	orderOps=['-','+','*','/']
	prec1=orderOps.index(op1)
	prec2=orderOps.index(op2)
	if prec1>prec2:
		return 1
	elif prec1==prec2:
		return 0
	else:
		return -1

inputString="2+4+5+10"
outputQueue=Queue()
operatorStack=Stack()
for tokens in inputString:
    if tokens.isnumeric():
    	outputQueue.enqueue(tokens)
    elif tokens in ['*','/','+','-']:
    	if operatorStack.size!=0:
    		while checkPrecedence(operatorStack.getTop(),tokens)==1:
    			outputQueue.enqueue(operatorStack.pop())
    	operatorStack.push(tokens)
    elif tokens=='(':
    	operatorStack.push(tokens)
    elif tokens==')':
    	while (operatorStack.getTop()!=')'):
    		outputQueue.enqueue(operatorStack.pop())
    	operatorStack.pop('(')

while operatorStack.size():
	outputQueue.enqueue(operatorStack.pop())


