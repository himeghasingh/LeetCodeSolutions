class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        n = len(nums)

        for i in range(0, n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # if n == 1 or k == 0:
        #     return False
        # i = 0
        # j = 1
        # while j < n and i < n:
        #     # print("i = ",i, " j = ", j)
        #     if nums[i] == nums[j]:
        #         return True
        #     j += 1
        #     if j - i > k or (j == n and i < n - 1):
        #         print("\nBefore")
        #         print("i = ", i)
        #         print("j = ", j)
        #         i += 1
        #         j = i + 1
        #         print("\nAfter")
        #         print("i = ", i)
        #         print("j = ", j)
               

                
            
        # return False


        