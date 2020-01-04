class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)

### 这很明显不是我写的code

#     ```c
# 		// c++  code
#     vector<string> restoreIpAddresses(string s) {
#         vector<string> ret;
#         string ans;
        
#         for (int a=1; a<=3; a++)
#         for (int b=1; b<=3; b++)
#         for (int c=1; c<=3; c++)
#         for (int d=1; d<=3; d++)
#             if (a+b+c+d == s.length()) {
#                 int A = stoi(s.substr(0, a));
#                 int B = stoi(s.substr(a, b));
#                 int C = stoi(s.substr(a+b, c));
#                 int D = stoi(s.substr(a+b+c, d));
#                 if (A<=255 && B<=255 && C<=255 && D<=255)
#                     if ( (ans=to_string(A)+"."+to_string(B)+"."+to_string(C)+"."+to_string(D)).length() == s.length()+3)
#                         ret.push_back(ans);
#             }    
        
#         return ret;
# ````				
# 我喜欢这个方法，但是这个貌似只能对应特定题目。遍历所有的可能的方式，然后选择正确的方式，非常好理解

# 另外，找所有解的问题可以要知道一个backtracking(回溯法)，其实也可以理解成DFS方法。这个方法通常采用递归，递归函数的参数可以包括（待处理s， 处理的次数index，处理后结果sol，打印后结果res），用这种套路求解这样的问题实在是太棒了。