#include <stdio.h>
#include <stdbool.h>
#include <string.h>

_Bool isValid(char* s);
//_Bool STACK_EMTPY(int *S);
void PUSH(int *S,int x,int *S_top);
int POP(int* S,int *S_top);



int main(){
    char* str={"{}{}{}()"};
    if(isValid(str))
        printf("1");
    else
        printf("0");
}

_Bool isValid(char* s){
    int S_top=-1;			
    int len=strlen(s);	
    int ST[len];		//Create stack  //这里可以使用char
    int temp;			
    int i=0;
    if (len%2!=0) return 0;	
    while(i<len)
    {
        if(S_top==-1)		//如果stack为空，则直接push
        {
            temp=s[i];
            PUSH(ST,s[i],&S_top);
        }
        else
        {
            temp=s[i]-ST[S_top];	//计算下一个元素和stack的top元素是否match
            if ((temp==1)||(temp==2))  // if s[i]&s[i+1] match
                POP(ST,&S_top);
            else
                PUSH(ST,s[i],&S_top);
        }
        i++;
    }
    if (S_top==-1) return true;		//如果全部遍历完后，stack为空
    else    return false;
}

//_Bool STACK_EMTPY(int *S){		//这里好像没有必要用到这个函数，直接查看S_top即可
//    if (S_top==-1) return true;
//    else return false;
//}

void PUSH(int *S,int x,int *S_top){
    (*S_top)++;			//这里应该要有括号
    S[*S_top]=x;
}

int POP(int* S,int *S_top){
    if(*S_top==-1)
    {
        //printf("error: underflow");	//在leetcode里，不要出现printf
        return 0;
    }
    else
    {
        (*S_top)--;
        return S[*S_top];
    }
}
