#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* temp=NULL;
    struct ListNode* head=(struct ListNode*)malloc(sizeof(struct ListNode));
    int cnt=0;
    if(l1==NULL)
        return l2;
    else if(l2==NULL)
        return l1;
    //如果一个list为空，则返回另一个
    while((l1!=NULL)&&(l2!=NULL)){
        struct ListNode* LinkedNode=(struct ListNode*)malloc(sizeof(struct ListNode));
        if((l1->val)>(l2->val))
        {
            if (cnt==0)
            {
                head->val=l2->val;
                temp=head;
            }
            else
            {
                LinkedNode->val=l2->val;    //把其中较小的值赋给linkedNode
                temp->next=LinkedNode;              //上一个temp指向新的LinkedNode
            }
            l2=l2->next;                    //l2更新
            cnt++;
        }
        else
        {
            if (cnt==0)
            {
                head->val=l1->val;
                temp=head;
            }
            else
            {
                LinkedNode->val=l1->val;    //把其中较小的值赋给linkedNode
                temp->next=LinkedNode;      //上一个temp指向新的LinkedNode
            }
            l1=l1->next;
            cnt++;
        }
        if(cnt!=1)
            temp=LinkedNode;                    //linkedNode把自己的地址赋给temp
    }
    //将一个剩余的list链接到之前到tail上
    if (l1==NULL)
        temp->next=l2;
    else
        temp->next=l1;
    
    return head;
}


