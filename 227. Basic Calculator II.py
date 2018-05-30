class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        slist = ['0']
        operator = {'*','/','+','-'}
        nums = '0123456789'
        for i in range(len(s)):
            if s[i] in operator:
                slist.append(s[i])
            else:
                if slist[-1].isdigit():
                    slist[-1] += s[i] 
                else:
                    slist.append(s[i])
        t = 0
        stack = []
        while t < len(slist):
            if slist[t] not in operator:
                stack.append(int(slist[t]))
                t += 1
            else:
                if slist[t] in {'+', '-'}:
                    stack.append(slist[t])
                    t += 1
                elif slist[t] == '*':
                    stack.append(stack.pop() * int(slist[t+1]))
                    t += 2
                elif slist[t] == '/':
                    stack.append(stack.pop() // int(slist[t+1]))
                    t += 2
        t, output= 1, stack[0]
        while t < len(stack):
            if stack[t] == '+':
                output += stack[t+1]
            else:
                output -= stack[t+1]
            t += 2
        return output
        
        