class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def makeComb(startInd, path):
            if len(path) == n and path not in res:
                res.append(list(path))
                return
            for j in range(0, n):
                if nums[j] not in path:
                    makeComb(j+1, path+[nums[j]])
        
        for i in range(0, n):
            makeComb(i, [])
        return res
            
        