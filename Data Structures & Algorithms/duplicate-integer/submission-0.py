class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = []
        for i in range(len(nums)):
            if nums[i] in encountered:
                return True
            else:
                encountered.append(nums[i])
        return False