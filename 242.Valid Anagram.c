//
//  isAnagram.c
//  Leetcode
//
//  Created by 吴必佳 on 2018/1/28.
//  Copyright © 2018年 BiJia Wu. All rights reserved.
//

#include "isAnagram.h"

_Bool isAnagram(char *s,char *t){
    int s_num[26]={0};
    int t_num[26]={0};
    int s_len=strlen(s);
    if (s_len!=strlen(t))
        return false;
    for (int i=0;i<s_len;i++){
        s_num[*(s+i)-'a']++;
        t_num[*(t+i)-'a']++;
    }
    for(int i=0;i<26;i++){
        if (s_num[i]!=t_num[i])
            return false;
    }
    return true;
}

