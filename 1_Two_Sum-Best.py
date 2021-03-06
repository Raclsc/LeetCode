# LeetCode
# Level: Easy
# Date: 2021.11.2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]] = i