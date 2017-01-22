package com.algo.practice;

public class MergeSort {

	public static void main(String[] args) {
		int [] input ={2,3,4,5,7}; 
		int p=0; 
		int r=input.length-1; 
		int [] output =mergesort(input,p,r); 
		for (int x=0;x<output.length-1;x++)
		{
			System.out.println(x+",");
		}

	}
	public static int [] mergesort (int[] inputarray, int p, int r)
	{
		int []sorted = null; 
		if ( p<r)
		{
			int q=(p+r)/2; 
			
			mergesort(inputarray,p,q); 
			mergesort(inputarray,q+1,r); 
			sorted=mergeprocedure(inputarray,p,q,r); 
		}
		return sorted; 
		
	}
	public static int [] mergeprocedure (int [] inputarray, int p, int q, int r)
	{
		int n1=q-p+1; 
		int n2=r-q; 
		int [] L={0}; 
		int [] R={0}; 
		
		for (int i=0;i<n1;i++)
		{
			L[i]=inputarray[p+i]; 
		}
		for (int j=0;j<n2;j++)
		{
			R[j]=inputarray[q+j]; 	
		}
		L[n1-1]=(int) Double.POSITIVE_INFINITY; 
		R[n2-1]=(int) Double.POSITIVE_INFINITY; 
		int i=1; 
		int j=1; 
		
		for (int k=p;k<=r;k++)
		{
			if (L[i]<=R[j])
			{
				inputarray[k]=L[i]; 
				i=i+1; 
			}
			else 
			{
				inputarray[k]=R[j];
				j=j+1; 	
			}
					
		}
		return inputarray; 	
		
		
	}
	

}
