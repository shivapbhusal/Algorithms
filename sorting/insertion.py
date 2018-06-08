'''
Python implementation of Insertion sort. 
Takes a data file as an argument.
Example, python insertion.py data.txt as a input. 
'''

import sys

def insertion(num_list):
    '''
    Insertion sort function. 
    Argument type: list
    '''
    size =len(num_list)
    for i in range(1, size):
        key=num_list[i]
        j=i-1
        while (j>=0) and (num_list[j]>key):
            num_list[j+1]=num_list[j]
            j=j-1
        num_list[j+1]=key

fin=open(sys.argv[1]) # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

insertion(num_list)
print(num_list)



