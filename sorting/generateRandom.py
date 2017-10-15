#!/usr/bin/python
# Python program to generate random numbers taking inputs from users. 
# Author : Shiva Bhusal, Bowling Green State University 
import sys
from random import *

inputs=sys.argv

if len(inputs)>4:
	print('To many command line inputs !')
else: 
	lower_range=int(inputs[1])
	upper_range=int(inputs[2])
	n=int(inputs[3])

for numbers in range(1,n+1):
    x = randint(lower_range, upper_range)    # Pick a random number between the range 
    print (x)








