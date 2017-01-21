package com.algo.practice;

public class SecretNumberFinder {
	public static int secret=15; 

	public static void main(String[] args) {

		guessrange(1,50); 
		
	}
	
	public static void guessrange(int p, int q)
	{
		int midpoint=(p+q)/2; 
		if (secret==midpoint)
		{
			System.out.println(midpoint+"is correct");
		}
		else if (secret<midpoint)
		{
		System.out.println("Secret is less than"+midpoint); 
		q=midpoint; 
		guessrange(p,q); 
		}
		else if (secret>midpoint)
		{
			System.out.println("Secret is greater than"+midpoint); 
			p=midpoint; 
			guessrange(p,q); 
			
		}
		
	}

}
