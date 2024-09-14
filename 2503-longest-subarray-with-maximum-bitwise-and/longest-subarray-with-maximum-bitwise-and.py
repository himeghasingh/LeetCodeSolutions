class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxnum = max(nums)
        c = 0
        maxlen = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] == maxnum:
                c += 1
                maxlen = max(maxlen, c)
            else:
                c = 0
                

            
        return maxlen
        