class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if '0' in digits or '1' in digits or not digits:
            return []
        else:
            output = [i for i in dict[digits[0]]]
            for i in range(1, len(digits)):
                new = []
                for s in output:
                    for j in dict[digits[i]]:
                        new.append(s+j)
                output = new
        return output


# 这种反复迭代却只知道要迭代len次数的时候，reduce()就是干这个用的，所以一句话就可以搞定
# `return reduce(lambda acc, digit: [x + y for x in acc for y in dict[digit]], digits, [''])`

# 只不过在python3中，使用reduce需要
# from functools import reduce