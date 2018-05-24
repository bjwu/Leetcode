#include <stdio.h>

typedef struct {
	int *key;
	int top;
} MyStack;

/** Initialize your data structure here. */
MyStack* myStackCreate(int maxSize) {
    MyStack *s=(MyStack*)malloc(sizeof(MyStack));
	s->key=(int*)malloc(maxSize*sizeof(int));
	s->top=-1;
	return s;
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    (obj->top)++;
	(obj->key)[obj->top]=x;
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack* obj) {
	return (obj->key)[(obj->top)--];
}

/** Get the top element. */
int myStackTop(MyStack* obj) {
	return (obj->key)[obj->top];
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack* obj) {
	return ((obj->top)==-1);   
}

void myStackFree(MyStack* obj) {
   free(obj); 
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * struct MyStack* obj = myStackCreate(maxSize);
 * myStackPush(obj, x);
 * int param_2 = myStackPop(obj);
 * int param_3 = myStackTop(obj);
 * bool param_4 = myStackEmpty(obj);
 * myStackFree(obj);
 */

