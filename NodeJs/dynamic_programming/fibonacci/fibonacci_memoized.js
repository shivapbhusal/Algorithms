/*
 A recursive implementation of Fibonacci
 */ 

const memo = new Map ();

function fibonacci(N){
	if (memo.has(N)){
		return memo.get(N);
	}
	else if (N<=2){
		return N;
	}
	else {
		memo.set(N,fibonacci(N-1)+fibonacci(N-2));
		return fibonacci(N-1)+fibonacci(N-2);
	}
}

if (memo.has(1)){
console.log("Worked");
}

N = process.argv[2];

console.log(fibonacci(N));


