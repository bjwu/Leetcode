class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start ,leng, dict= 0, 0, {}
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] >= start:
                    start = dict[s[i]]+1
            dict[s[i]] = i
            leng = max(leng, i-start+1)
        return leng


# string的题目通常只要返回长度数字，不要返回具体的字符串，这样的话可以采用dict方式记录index很方便。同时采用几个pointers进行遍历也是常用的方法。
# 用dict的key记录str的char，value记录对应的index简直是神器