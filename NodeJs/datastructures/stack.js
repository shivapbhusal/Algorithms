/*
 Stack Implementation in NodeJs.

 Author : Shiva Bhusal.
 */

class Stack {
	constructor(){
		this.stack = [];
	}

	isEmpty(){
		return this.stack.length == 0;
	}

	push(x){
		this.stack.push(x);
	}

	pop(x){
		this.stack.pop();
	}

	getSize(){
		return this.stack.length;
	}

	getItemOnTop(){
		if (this.stack.length){
			return this.stack[this.stack.length -1];
		}
	}
}

myStack = new Stack();

console.log("Order in which items are pushed");
for (let i=0; i<=10; i++){
	myStack.push(i);
	console.log(i);
}

console.log("\n"+"Order in which items are popped");
for (let i =0; i<=10; i++){
	console.log(myStack.getItemOnTop())
	myStack.pop();
}
