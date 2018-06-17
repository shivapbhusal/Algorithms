'''
Python Implementation of Counting Sort
'''

import sys as sys 
fileName=sys.argv[1]

contents=open(fileName)

rawData=[]
countArray=[]
sortedArray=[]

for i  in range(19): # Find the maximum no to be sorted 
    countArray.append(0)

for lines in contents:
    rawData.append(int(lines))

for nums in rawData:
    countArray[nums]=countArray[nums]+1

sumPrev=0; 

for i in range(len(countArray)):
    sumPrev=sumPrev+countArray[i]
    countArray[i]=sumPrev

for i in range(len(rawData)):
    sortedArray.append(0)

for nums in rawData:
    sortedArray[countArray[nums]-1]=nums
    countArray[nums]-=1 

print(sortedArray)
