class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        seen = sorted(set(nums))
        count = 0
        temp = 1
        if not seen:
            return count

        for num in seen:
            if num - 1 in lookup:
                temp += 1
            else:
                count = max(count, temp)
                temp = 1
        count = max(count, temp)
        return count