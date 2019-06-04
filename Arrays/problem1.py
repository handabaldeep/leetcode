# Problem-1: Two Sum
# Link - https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[target-nums[i]],i]