# Problem-118: Pascal's Triangle
# Link - https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        ret = [[1]]
        for i in range(2,numRows+1):
            l = [1]
            for j in range(0,i-2):
                l.append(ret[i-2][j]+ret[i-2][j+1])
            l.append(1)
            ret.append(l)
        return ret