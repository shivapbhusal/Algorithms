# Python implementation of three way merge sort

import sys

def merge_proc(num_list, start,q1, q2,end):# Merge procedure
    B=[]
    C=[]
    D=[]
    n1=q1-start+1
    n2=q2-q1
    n3=end-q2 
    for i in range(0,n1):
        B.append(num_list[start+i])

    for i in range(0,n2):
        C.append(num_list[q1+i+1])

    for i in range(0,n3):
        D.append(num_list[q2+i+1])

    B.append(sys.maxsize)
    C.append(sys.maxsize)
    D.append(sys.maxsize)

    i=0 
    j=0
    k=0

    for l in range(start,end):
        if B[i]<=C[j] and B[i]<=D[k]:
            num_list[l]=B[i]
            i=i+1
        elif C[j]<=B[i] and C[j]<=D[k]:
            num_list[l]=C[j]
            j=j+1
        else:
            num_list[l]=D[k]
            k=k+1 


def three_merge_sort(num_list, start,end): # Merge  sort function
    if (end-start)<2:
        if (end-start)==0:
            return
        else:
            if num_list[start]>num_list[end]:
                temp=num_list[start]
                num_list[start]=num_list[end]
                num_list[end]=temp

    else:
        q1=start+int((end-start)/3)
        q2=start+int(2*(end-start)/3)
        three_merge_sort(num_list,q1+1,q2)
        three_merge_sort(num_list,q2+1,end)
        merge_proc(num_list,start,q1,q2,end)


fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
three_merge_sort(num_list,0,len(num_list)-1)
print(num_list)




