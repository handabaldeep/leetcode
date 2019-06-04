# Problem-35: Search Insert Position
# Link - https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        m = 0
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r = m-1
            else:
                l = m+1
        #print(m)
        if nums[m]>target:
            return m
        else:
            return m+1