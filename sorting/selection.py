# Python implementation of selection sort 

def selection(num_list, size): # Selection sort function
    for i in range(0,size-1):
        for j in range(i,size-1):
            if num_list[j]<num_list[i]: # Swap if num_list[j] is less than num_list[i]
                temp=num_list[i]
                num_list[i]=num_list[j]
                num_list[j]=temp

fin=open('data.txt') # Open the file
num_list=[]

for lines in fin:    # Read numbers from the file and create an unsorted list 
    lines=int(lines)
    num_list.append(lines)

n=len(num_list)
selection(num_list,n)
print(num_list)



