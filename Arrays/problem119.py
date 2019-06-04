# Problem-119: Pascal's Triangle II
# Link - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(1,rowIndex+1):
            l = [1]
            for j in range(0,i-1):
                l.append(ret[j]+ret[j+1])
            l.append(1)
            ret = l
        return ret