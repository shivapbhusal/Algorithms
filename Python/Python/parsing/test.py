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

print(checkPrecedence('+','-'))