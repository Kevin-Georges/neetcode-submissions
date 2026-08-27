class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed_nums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashed_nums:
                return [hashed_nums[complement], i]
            else:
                hashed_nums[nums[i]] = i