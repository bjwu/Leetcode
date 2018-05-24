class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if s[i] in sdict and t[i] in tdict and sdict[s[i]] == tdict[t[i]]:
                continue                
            elif s[i] not in sdict and t[i] not in tdict:
                sdict[s[i]] = tdict[t[i]] = i
            else:
                return False
        return True

# 了解几个方法：
# 1、

def isIsomorphic2(self, s, t):
    return list(map(s.find, s)) == list(map(t.find, t))
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

# 2、
def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# 3、
# 其实用一个dict也可以搞定
def isIsomorphic4(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    found = {}
		## 这个dict的key是s[i]，value值是t[i]
    
    for i in range(len(s)):
        if s[i] in found:
            if not found[s[i]] == t[i]:
                return False
        else:
            if t[i] in found.values():
                return False
            found[s[i]] = t[i]
    return True

