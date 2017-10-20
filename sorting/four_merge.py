# Python implementation of Four way merge sort

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
    B=[]
    C=[]
    D=[]
    E=[]
    n1=q1-start+1
    n2=q2-q1
    n3=q3-q2
    n4=end-q3
    for i in range(0,n1):
        B.append(num_list[start+i])

    for i in range(0,n2):
        C.append(num_list[q1+i+1])

    for i in range(0,n3):
        D.append(num_list[q2+i+1])

    for i in range(0,n4):
        E.append(num_list[q3+i+1])



    B.append(sys.maxsize)
    C.append(sys.maxsize)
    D.append(sys.maxsize)
    E.append(sys.maxsize)

    i=0 
    j=0
    k=0
    l=0

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


def three_merge_sort(num_list, start,end): # Merge  sort function
    if (end-start)<3:
        if (end-start)!=0:
            selection_sort(num_list)

    else:
        q1=start+int((end-start)/4)
        q2=start+int(2*(end-start)/4)
        q3=start+int(3*(end-start)/4)
        three_merge_sort(num_list,start,q1)
        three_merge_sort(num_list,q2+1,q2)
        three_merge_sort(num_list,q2+1,q3)
        three_merge_sort(num_list,q3+1, end)
        merge_proc(num_list,start,q1,q2,q3,end)


fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
three_merge_sort(num_list,0,n-1)

for numbers in num_list:
    print(numbers)


