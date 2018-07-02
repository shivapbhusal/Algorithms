/*
 Queue Implementation in NodeJs.

 Author : Shiva Bhusal.
 */

class Queue {
	constructor(){
		this.queue = [];
	}

	isEmpty(){
		return this.queue.length == 0;
	}

	enqueue(x){
		this.queue.push(x);
	}

	dequeue(){
		this.queue.splice(0,1);
	}

	getSize(){
		return this.queue.length;
	}

	getItemAtFront(){
		if (this.queue.length){
			return this.queue[0];
		}
		else {
			console.log("The queue is empty");
		}
	}
}

myQueue = new Queue();

console.log("Order in which items are enqueued");
for (let i=0; i<=10; i++){
	myQueue.enqueue(i);
	console.log(i);
}

console.log("\n"+"Order in which items are dequeued");
for (let i =0; i<=10; i++){
	console.log(myQueue.getItemAtFront())
	myQueue.dequeue();
}
