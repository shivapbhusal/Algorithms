# Python implementation of selection sort 

import sys

def merge(num_list, start, midpoint, end):# Merge procedure
    B=[]
    C=[]
    for i in range(start,midpoint+1):
        B.append(num_list[i])

    for i in range(midpoint+1,end+1):
        C.append(num_list[i])

    B.append(sys.maxsize)
    C.append(sys.maxsize)

    i=1 
    j=1

    for k in range(start,end):
        if B[i]<=C[j]:
            num_list[k]=B[i]
            i=i+1
        else:
            num_list[k]=C[j]
            j=j+1


def merge_sort(num_list, start,end): # Merge  sort function
    if start>=end:
        return
    else:
        midpoint=int((start+end)/2)
        merge_sort(num_list,start,midpoint)
        merge_sort(num_list, midpoint+1,end)
        merge(num_list,start, midpoint, end)


fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
merge_sort(num_list,0,len(num_list)-1)




