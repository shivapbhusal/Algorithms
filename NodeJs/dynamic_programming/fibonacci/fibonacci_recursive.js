/*
 A recursive implementation of Fibonacci
 */ 

function fibonacci(N){
	if (N<=2){
		return N;
	}
	else {
		return  fibonacci(N-1)+fibonacci(N-2);
	}
}

N = process.argv[2];

console.log(fibonacci(N));


