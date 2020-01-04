class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        demo = set()
        for i in nums:
            if i in demo:
                demo.remove(i)
            else:
                demo.add(i)
        return demo.pop()

# 1. python中的^ 运算符代表按位异或，所以如果对nums中的所有元素进行异或，那么有两个的元素都会被抵消，剩下的就是single number了。
# 2. 求和相减也是一种方法
# 下面每个函数都是个不同的方法
def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)


