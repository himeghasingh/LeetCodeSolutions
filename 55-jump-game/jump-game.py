class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n-2, -1, -1):
            print("current number ",nums[i])
            if nums[i] >= goal - i :
                goal = i
        if goal == 0:
            return True
        return False

        