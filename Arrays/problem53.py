# Problem-53: Maximum Subarray
# Link - https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = totMax = nums[0]
        for num in nums[1:]:
            currMax = max(num,currMax+num)
            totMax = max(totMax,currMax)
        return totMax