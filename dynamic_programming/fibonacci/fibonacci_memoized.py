'''Memoized Fibonacci solution
Created By: Shiva Bhusal, BGSU 
''' 

import sys

N=sys.argv[1]

memo=dict()
def fibonacci(N):
	if N in memo:
		return memo[N]
	elif N<=2:
		return N
	else:
		memo[N]=fibonacci(N-1)+fibonacci(N-2)
		return memo[N]
	
print(fibonacci(int(N)))


