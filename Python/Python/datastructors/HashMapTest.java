// A class file to demonstrate the use of hashmap

import java.util.HashMap;

public class HashMapTest
{
	public static void main(String args[])
	{
		HashMap<Integer,Integer> map=new HashMap<Integer,Integer>(); 

		for (int i=0; i<50; i++)
		{
			i=i*2; 
			map.put(i,0); 
			map.put(null,0); 
		}

		for (int j=0; j<=100;j++)
		{
			if (map.containsKey(j)){
			System.out.println("Map contains "+j); 
			}
			else {
				System.out.println("Map doesn't contain "+j); 
			}


		}


	}
}