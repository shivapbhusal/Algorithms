/*A Java Program demonstrating Insertion Sort*/ 

package com.algo.practice;

public class InsertionSort {

	public static void main(String[] args) {
		 int[] input = {1,5,2,6,8,0};
	        insertionSort(input);
		
		// TODO Auto-generated method stub

	}
	private static void printNumbers(int[] input) {
        
        for (int i = 0; i < input.length; i++) {
            System.out.print(input[i] + ", ");
        }
        System.out.println("\n");
    }
 
    public static void insertionSort(int array[]) {
        int n = array.length;
        for (int j = 1; j < n; j++) {
            int key = array[j];
            int i = j-1;
            while ( (i > -1) && ( array [i] > key ) ) {
                array [i+1] = array [i];
                i--;
            }
            array[i+1] = key;
            printNumbers(array);
        }
    }

}
