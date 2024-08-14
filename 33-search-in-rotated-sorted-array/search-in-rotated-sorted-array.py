class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n - 1

        while (l < r):
            mid = (l + r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        print("im here")
        
        minIndex = l
        print("minindex", minIndex)
        if nums[0] <= target <= nums[minIndex-1] and minIndex > 0:
            print("in first half")
            left = 0
            right = minIndex - 1
            while(left <= right):
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        
        elif nums[minIndex] <= target <= nums[n-1]:
            print("in second half")
            left = minIndex
            right = n - 1
            while(left <= right):
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

        
        return -1
        