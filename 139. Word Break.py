class Solution:
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 这是一个自上而下的DP，超时了
        # results = []
        # for i in range(len(s)):
        #     if s[:i+1] in wordDict:
        #         if s[i+1:] == '':
        #             return True
        #         else:
        #             results.append(self.wordBreak(s[i+1:], wordDict))
        # return (True in results)
        memo = {}
        def helper(s, loc):
            if loc in memo:
                return memo[loc]
            results = []
            for i in range(len(s)):
                if loc+i+1 in memo:
                    results.append(memo[loc+i+1])
                    continue
                if s[:i+1] in wordDict:
                    if s[i+1:] == '':
                        return True
                    else:
                        results.append(helper(s[i+1:], loc+i+1))
            memo[loc] = (True in results)
            return (True in results)
        return helper(s, 0)

# ```py
#         def can_decode(i):
#             if i == len(s):
#                 return True
#             for w in wordDict:
#                 if s.startswith(w, i) and can_decode(i + len(w)):
#                     return True
#             return False

#         return can_decode(0)
# ```
# 又是这个startwith()， 要记住听到没