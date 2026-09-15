class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = {}
        return_list = []
        for i, n in enumerate(nums):
            if n not in hash_nums:
                hash_nums[n] = 1
            else:
                hash_nums[n] = hash_nums[n] + 1

        for i in range(k):
            x = max(hash_nums, key=hash_nums.get)
            return_list.append(x)
            hash_nums.pop(x)
        
        return return_list