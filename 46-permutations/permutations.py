class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def makeComb(path):
            if len(path) == n and path not in res:
                res.append(list(path))
                return
            for j in range(0, n):
                if nums[j] not in path:
                    makeComb(path+[nums[j]])
        
        
        makeComb([])
        return res
            
        