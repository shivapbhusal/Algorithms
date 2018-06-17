# Python implementation of K-Way Merge Sort

import sys

def selection_sort(num_list):
    n=len(num_list)
    for i in range(0,n):
        for j in range (i,n):
            if num_list[j]<num_list[i]:
                temp=num_list[i]
                num_list[i]=num_list[j]
                num_list[j]=temp

def merge_proc(num_list, start,q1, q2,q3,end):# Merge procedure
    nested_list=[]
    sizes=[]
    sizes.append(pivot[1]-pivot[0]+1)
    for i in range(1, len(pivot)):
        sizes.append(pivot[i+1]-pivot[i])

    for i in range(0,pivot[0]):
        first_list.append(num_list[pivot[0]+i])

    nested_list.append(first_list);
        
    for sizes in size:
        for i in range(1,size):
            temp_list=[]
            temp_list.append(num_list[sizes+i+1])

    nested_list.append(temp_list)

    for lists in nested_list:
        lists.append(sys.maxsize)

    for i in range (0,len(nested_list)):
        for j in range(0,len(nested_list)):
            nested_list[0][j]

    for m in range(start,end+1):
        if B[i]<=C[j] and B[i]<=D[k] and B[i]<=E[l]:
            num_list[m]=B[i]
            i=i+1
        elif C[j]<=B[i] and C[j]<=D[k] and C[j]<=E[l]:
            num_list[m]=C[j]
            j=j+1
        elif D[k]<=B[i] and D[k]<=C[j] and D[k]<=E[l]:
            num_list[m]=D[k]
            k=k+1
        else :
            num_list[m]=E[l]


def kway_merge_sort(num_list, start,end, k): # Merge  sort function
    if (end-start)<k-1:
        if (end-start)!=0:
            selection_sort(num_list)

    else:
        pivots=[]
        for i in range(1,k+1):
            pivots.append(start+int((end-start)*i/k))

        kway_merge_sort(num_list,start,pivots[0])
        for i in range(1,len(pivots)-1):
            kway_merge_sort(num_list,pivots[i]+1,pivots[i+1])

        merge_proc(num_list,pivots)


fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
kway_merge_sort(num_list,0,n-1,k)

for numbers in num_list:
    print(numbers)


