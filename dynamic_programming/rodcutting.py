# Python implementation of Rodcutting dynamic programming 

import sys as sys

def bottom_up(price,n):
	r=[]
	s=[]
	r.append([0])
	for j in range(1,n):
		q=-sys.maxsize
		for i in range(1,j+1):
			if q< price[i]+r[j-i]:
				q=price[i]+r[j-i]
				s[j]=i
		r[j]=q
	return r

fin=open('data_rodcutting.txt') # Open the file
price=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    price.append(lines)

rev_list=bottom_up(price, len(price))

for revenue in rev_list:
	print(revenue)



