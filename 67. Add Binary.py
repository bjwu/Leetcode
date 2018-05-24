class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import numpy as np
        if len(a)<=len(b):
            minstr=a
            maxstr=b
        else:
            minstr=b
            maxstr=a
        carry = [0]*(len(maxstr)+1)
        output = [0]*(len(maxstr))
        for i in range(len(minstr)):
            output[-(i+1)] = (int(minstr[-(i+1)])+int(maxstr[-(i+1)])+carry[-(i+1)])%2
            carry[-(i+2)] = (int(minstr[-(i+1)])+int(maxstr[-(i+1)])+carry[-(i+1)])//2
        for i in range(len(minstr),len(maxstr)):
            output[-(i+1)] = (int(maxstr[-(i+1)])+carry[-(i+1)])%2
            carry[-(i+2)] = (int(maxstr[-(i+1)])+carry[-(i+1)])//2
        if carry[0] == 1:
            output.insert(0,1)
        output =  [str(x) for x in output]
        return ''.join(output)
        
        
############ More powerful ##############

#add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
   class Solution:
        def addBinary(self, a, b):
            if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'


########## More simple ##################
# 
class Solution:
    def addBinary(self, a, b):
        return str(bin(int(a,2)+int(b,2)))[2:]         
            
            
