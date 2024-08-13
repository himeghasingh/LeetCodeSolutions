class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def makeComb(start, curr):
            if len(curr) == k:
                res.append(curr)
                return
            for i in range(start, n+1):
                makeComb(i+1, curr + [i])
        makeComb(1, [])
        return res