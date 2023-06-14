from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_prod, min_prod = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                max_prod, min_prod = 1, 1
                continue
            tmp = max_prod * nums[i]
            max_prod = max(max_prod * nums[i], nums[i] * min_prod, nums[i])
            min_prod = min(tmp, nums[i] * min_prod, nums[i])
            res = max(res, max_prod)
        return res
