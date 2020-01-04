#include <stdio.h>

typedef struct {
	int *key;       //队列的元素
	int top;
	int rear;
	int maxSize;
} MyQueue;

/** Initialize your data structure here. */
MyQueue* myQueueCreate(int maxSize) {
    MyQueue *q=(MyQueue*)malloc(sizeof(MyQueue));
	q->key=(int*)malloc(maxSize*sizeof(int));
	q->top=maxSize-1;
	q->rear=maxSize-1;
	q->maxSize=maxSize;
	return q;
}

/** Push element x to the back of queue. */
void myQueuePush(MyQueue* obj, int x) {		//这里没有考虑队列满的情况
	(obj->key)[obj->rear]=x;
	if (obj->rear==0)
		obj->rear=obj->maxSize-1;
	else
		obj->rear--;
}

/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue* obj) {      //对于top的underflow的情况做了更新
    if (obj->top==0) {
        obj->top=obj->maxSize-1;
        return (obj->key)[obj->top];
    }
    else
        return (obj->key)[(obj->top)--];
}

/** Get the front element. */
int myQueuePeek(MyQueue* obj) {
	return (obj->key)[obj->top];  
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue* obj) {
   return (obj->rear==obj->top); 
}

void myQueueFree(MyQueue* obj) {
   free(obj); 
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * struct MyQueue* obj = myQueueCreate(maxSize);
 * myQueuePush(obj, x);
 * int param_2 = myQueuePop(obj);
 * int param_3 = myQueuePeek(obj);
 * bool param_4 = myQueueEmpty(obj);
 * myQueueFree(obj);
 */
//

