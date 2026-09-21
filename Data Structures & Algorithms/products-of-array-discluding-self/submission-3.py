class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        return_list = []
        for i, n in enumerate(nums):
            if i == 0:
                prefix.append(n)
            else:
                prefix.append(n * prefix[i-1])
        
        for i, n in enumerate(reversed((nums))):
            if i == 0:
                suffix.append(n)
            else:
                suffix.append(n* suffix[i-1])
        suffix = list(reversed(suffix))

        for i in range(len(nums)):
            if i == 0:
                return_list.append(suffix[i + 1])
            elif i == len(nums) - 1:
                return_list.append(prefix[i - 1])
            else:
                return_list.append(prefix[i - 1] * suffix[i + 1])
        return return_list