from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in nums_idx_dict:
                nums_idx_dict[nums[i]] = i
            else:
                return [nums_idx_dict[target - nums[i]], i]
