class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        i = 0
        seen = set()
        
        res = 0
        while i+3 <= n:
            if len(set(s[i:i+3])) == 3:
                res += 1
            i += 1
        return res



            

        