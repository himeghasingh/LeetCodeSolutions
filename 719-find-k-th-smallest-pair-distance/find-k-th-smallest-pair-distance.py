class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums.sort()

        def findPairs(target):
            left = 0
            res = 0
            for right in range(0, len(nums)):
                while nums[right] - nums[left] > target:
                    left += 1
                res += right - left 
            return res

        l = 0
        r = max(nums)
        while (l < r):
            mid  = l + ((r - l) // 2)
            pairs = findPairs(mid)
            if pairs >= k:
                r = mid
            else:
                l = mid + 1
        return r  

        # n = len(nums)
        # maxNum = max(nums)
        # distanceBucket = [0] * (maxNum + 1)

        # for i in range(0, n):
        #     for j in range(i + 1, n):
        #         distance = abs(nums[i] - nums[j])
        #         distanceBucket[distance] += 1

        # for dist in range(0, maxNum + 1):
        #     k -= distanceBucket[dist]
        #     if k <= 0:
        #         return dist

        # return -1  
       
       
       
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #####BRUTE FORCE TLE#####
        # diffArray = []
        # minDist = []
        # n = len(nums)
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         diff = abs(nums[i]- nums[j])
        #         heapq.heappush(minDist, diff)
        # c = 0
        # while (c < k-1):
        #     heapq.heappop(minDist)
        #     c += 1
        # res = heapq.heappop(minDist)
        # return res
       