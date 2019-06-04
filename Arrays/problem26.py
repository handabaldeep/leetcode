# Problem-26: Remove Duplicates from Sorted Array
# Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastIndex,ctr,i = 0,1,1
        while i<len(nums):
            while i<len(nums) and nums[i]==nums[lastIndex]:
                i = i+1
            if(i>=len(nums)):
                break
            lastIndex = lastIndex+1
            nums[lastIndex] = nums[i]
            ctr = ctr+1
            i = i+1
        nums = nums[:ctr]
        return ctr