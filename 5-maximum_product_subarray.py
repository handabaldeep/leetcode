from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_prod = max_prod
        for i in range(1, len(nums)):
            curr_prod = max(curr_prod * nums[i], nums[i])
            max_prod = max(curr_prod, max_prod)

        return max_prod
