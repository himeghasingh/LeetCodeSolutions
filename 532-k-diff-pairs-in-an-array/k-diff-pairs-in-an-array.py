class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # nums.sort()
        n = len(nums)
        # i = 0
        # j = 1
        count = 0
        print(nums)
        seen = set()
        # while (i < j and j < n):
        #     diff = abs(nums[j] - nums[i])
        #     if diff == k:
        #         count += 1
        #         j += 1
        #     elif diff < k:
        #         j +=1
        #     else:
        #         i +=1
        #     if i == j:
        #         j += 1
        # # print(count)
        # return count

        for i in range(0, n):
            for j in range(i+1, n):
                diff = abs(nums[i] - nums[j])
                if diff == k and (nums[i],nums[j]) not in seen:
                    print("i =", i, " j =",j)
                    count +=1
                    seen.add((nums[i],nums[j]))
                    seen.add((nums[j],nums[i]))
                    
        return count


        