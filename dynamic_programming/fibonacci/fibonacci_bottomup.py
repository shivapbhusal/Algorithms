'''
Bottom up Fibonacci solution 
Created By: Shiva Bhusal, BGSU 
'''

import sys

N=sys.argv[1]

memo=dict()
for k in range(1,int(N)+1):
	if k<=2:
		memo[k]=k
	else:
		memo[k]=memo[k-1]+memo[k-2]

print(memo[k])

