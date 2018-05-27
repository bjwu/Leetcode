#include <stdio.h>
#include <limits.h>

typedef struct {
	  int *key;		//堆数组
	  int top;		
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack* s=(MinStack*)malloc(sizeof(MinStack));
	s->key=(int*)malloc(maxSize*sizeof(int));
	s->top=-1;
	return s;
}

void minStackPush(MinStack* obj, int x) {
	(obj->top)++;
	*((obj->key)+(obj->top))=x;
}

void minStackPop(MinStack* obj) {
    (obj->top)--;
}

int minStackTop(MinStack* obj) {
    return *((obj->key)+(obj->top));
}

int minStackGetMin(MinStack* obj) {
    int MIN=INT_MAX;
	int i=obj->top;
	while(i>-1){
		if(*((obj->key)+i)<MIN)
			MIN=*((obj->key)+i);
		i--;
	}
	return MIN;
}

void minStackFree(MinStack* obj) {
    free(obj->key);
	free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */
