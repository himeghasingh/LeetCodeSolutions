class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        def makeComb(start, target, path):
            if target == 0 and len(path) == k:
                res.append(path)
                return
            if target < 0 or len(path) == k:
                return
            for i in range(start, 10):
                makeComb(i+1, target-i, path+[i])
        makeComb(1, n, [])
        return res

        