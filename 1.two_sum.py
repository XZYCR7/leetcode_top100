'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums)<=1:

            return None
        else:
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    if target==nums[i]+nums[j]:
                        print(i,j)
                        return i,j
            #print (None)
            return None
s=Solution()
n = [3,3]
s.twoSum(n,6)