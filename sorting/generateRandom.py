
# Python program to generate random numbers taking inputs from users. 
# Author : Shiva Bhusal, Bowling Green State University 
# Example, python generateRandom.py 10 20 50. 
# Example generates 50 random numbers in between 10 and 20. 

import sys
from random import *

inputs=sys.argv

if len(inputs)>4:
	print('To many command line inputs !')

else: 
	lower_range=int(inputs[1])
	upper_range=int(inputs[2])
	n=int(inputs[3])

for numbers in range(0,n):
    x = randint(lower_range, upper_range)    # Pick a random number between the range 
    print (x)








