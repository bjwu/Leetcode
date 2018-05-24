class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countdict = {}
        for num in nums:
            if num not in countdict:
                countdict[num] = 1
            else:
                countdict[num] += 1
        return max(countdict.items(),key=lambda x:x[1])[0]


# 这是一种方法，因为排序后那个数肯定会在中间位置
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        return a[int(len(a)/2)]

# 这也是个好办法（Boyer-Moore Voting Algorithm），但是这两种办法都局限于这个数的数量大于>n/2	
	public class Solution {
    public int majorityElement(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;
            
        }
        return major;
    }

# 这个跟我的方法一样，也是hashmap，原来有一个collections.Counter()可以自动计数的啊
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

