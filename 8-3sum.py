from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            j = i + 1
            target_set = set()
            pairs = []
            while j < len(nums):
                if target - nums[j] not in target_set:
                    target_set.add(nums[j])
                else:
                    pairs.append((nums[i], target - nums[j], nums[j]))
                j += 1
            if len(pairs):
                res.extend(pairs)
        res_set = set(res)
        res = [list(i) for i in res_set]
        return res
