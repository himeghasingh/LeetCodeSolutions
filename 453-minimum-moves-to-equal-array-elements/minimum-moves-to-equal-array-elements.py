class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        nums.sort()
        for i in range(1, n):
            steps += nums[i] - nums[0]
        return steps

        #####TLE#####
        # while True:
        #     nums.sort()
        #     maxnum = max(nums)
        #     count = Counter(nums)

        #     if count[maxnum] == n:
        #         break

        #     for i in range(0, n-1):
        #         nums[i] += 1
        #     steps += 1
           
                
        # return steps


        