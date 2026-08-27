class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for i in range(len(nums)):
            if nums[i] in encountered:
                return True
            else:
                encountered.add(nums[i])
        return False

