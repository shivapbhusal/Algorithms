# Python implementation of Heap sort 

def heapSort(num_list, size): # Selection sort function
    for i in range(1, size):
        key=num_list[i]
        j=i-1
        while (j>0) and (num_list[j]>key):
            num_list[j+1]=num_list[j]
            j=j-1
        num_list[j+1]=key

fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
insertion(num_list,n)
print(num_list)



