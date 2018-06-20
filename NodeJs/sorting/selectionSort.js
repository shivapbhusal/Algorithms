/*
Selection sort implementation in Nodejs
Sorting is done by ascending order.
Space complexity : O(N)
Time complexity : O(N^2)
*/

function selectionSort(array){
	for (let i = 0; i<=(array.length-1); i+=1){
		for (let j = i; j<=(array.length -1); j+=1){
			if (array[i]>array[j]){
			// Swap if array[i] greater than array[j]
			temp = array[i];
			array[i] = array[j];
			array[j] = temp;
			}

		}
	}

	return array;
}

sortedArray = selectionSort([2,2,10,0,10,20,30,100,20,15]);
console.log(sortedArray);
