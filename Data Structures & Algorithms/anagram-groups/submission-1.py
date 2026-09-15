class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs = {}
        for i, n in enumerate(strs):
            key = ''.join(sorted(n))
            if key not in hash_strs:
                hash_strs[key] = [n]
            else:
                hash_strs[key].append(n)
        return list(hash_strs.values())