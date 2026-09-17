class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "empty"
        encoded_str = "  _ ".join(strs)
        return encoded_str
        
    def decode(self, s: str) -> List[str]: 
        if s == "empty":
            return []
        return s.split("  _ ")