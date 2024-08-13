class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_p = sorted(p)
        n_p = len(p)
        n = len(s)
        res = []
        for i in range(0, n - n_p + 1):
            if sorted(s[i:i+n_p]) == sorted_p:
                res.append(i)
        print(res)
        return res

        