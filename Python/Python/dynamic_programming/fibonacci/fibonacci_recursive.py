# Recursive Fibonacci solution 

import sys

N=sys.argv[1]

def fibonacci(N):
	if N<=2:
		return N
	else:
		return fibonacci(N-1)+fibonacci(N-2)

print(fibonacci(int(N)))


