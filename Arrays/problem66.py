# Problem-66: Plus One
# Link - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while i>=0 and digits[i]==9:
            digits[i] = 0
            i -= 1
        if i<0:
            #newList =
            return  [1] + digits[:]
        digits[i] = digits[i]+1
        return digits