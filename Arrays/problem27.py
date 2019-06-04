# Problem-27: Remove Element
# Link - https://leetcode.com/problems/remove-element/ 

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ctr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ctr] = nums[i]
                ctr += 1
        return ctr