class Solution:
    def isPalindrome(self, s: str) -> bool:
        if isinstance(s, str):
            s = list(s.lower())
        else:
            s = list(str(s))

        new_s = []

        for i in range(len(s)):
            if s[i].isalnum():
                new_s.append(s[i])
        
        head = 0
        tail = len(new_s) - 1

        for i in range(len(new_s)):
            if new_s[head] == new_s[tail]:
                head += 1
                tail -= 1
                pass 
            else:
                return False
        return True