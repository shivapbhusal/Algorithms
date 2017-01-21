package com.algo.practice;

public class Insertionsorttwo {

	public static void main(String[] args) {
		int[] input={1,3,5,6,2}; 
		insertionsort(input); 
		

	}
	public static void printarray(int[] input)
	{
		for ( int i=0;i<(input.length);i++)
		{
			System.out.print(input[i]+",");
		}
		System.out.println("");
		
	}
	public static void insertionsort (int array[])
	{
		int n=array.length; 
		for (int i=1;i<n;i++)
		{
			int key=array[i];
			int j=i-1;
			while ((j>-1)&& (array[j]>key))
			{
				array[j+1]=array[j]; 
				j=j-1; 
			}
			array[j+1]=key; 
			printarray(array); 
		}	
		
	}

}
