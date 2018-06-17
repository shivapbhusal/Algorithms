'''
Python implementation of selection sort.
Takes the fileName with numbers as the argument.

Running the program:
python selection.py $filename
Complexity: O(N^2) 

'''

import sys


def selection(num_list): # Selection sort function
    size=len(num_list)
    for i in range(0,size-1):
        for j in range(i,size-1):
            if num_list[j]<num_list[i]: # Swap if num_list[j] is less than num_list[i]
                temp=num_list[i]
                num_list[i]=num_list[j]
                num_list[j]=temp

fin=open(sys.argv[1]) # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

selection(num_list)
print(num_list)



