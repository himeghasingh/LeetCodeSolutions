class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        nums.sort()

        def twoSum(i, res):
            seen = set()
            j = i+1
            while j < n:
                complement = -nums[i]-nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    while j+1 < n and nums[j] == nums[j+1]:
                        j += 1
                seen.add(nums[j])
                j += 1




        for i in range(0, n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                twoSum(i, res)
        print(res)
        return res























        # n = len(nums)
        # numCounter = Counter(nums)
        # nums.sort()
        # ll = []


        # def twoSum(target, index, ll, firstNum):
        #     for i in range(index+1, n):
        #         if target-nums[i] in numCounter:
        #             if nums[i] != target-nums[i] or (nums[i] == target-nums[i] and numCounter[nums[i]] > 1):
        #                 ll.append([firstNum]+[nums[i], target-nums[i]])
        #     return ll
        
        # for i in range(0, n):

        #     firstNum = nums[i]
        #     if firstNum >= 0 and numCounter[0] < 3:
        #         break
        #     if i > 0 and nums[i] == nums[i-1] and nums[i]!=0:
        #         continue 
        #     ll = twoSum(0-firstNum, i, ll, firstNum)
            
        # print(ll)
        # return ll

                            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums) < 3:
        #     return []
        # # nums.sort()
        # n = len(nums)
        # sums = defaultdict(list)
        # res = set()

        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         currSum = nums[i] + nums[j]
        #         sums[currSum].append([i,j])



        # for i in range(0, n):
        #     firstNum = nums[i]
        #     remSum = 0 - firstNum
        #     if remSum in sums:
        #         sumComb = sums[remSum]
        #         for j,k in sumComb:
        #             if i != j and i != k:
        #                 res.add((i,j,k))
        # # print(res)
        # ll = []
        # for i,j,k in res:
        #     temp = sorted([nums[i], nums[j], nums[k]])
        #     if temp not in ll:
        #         ll.append(temp)
        # # print(ll)
        # return ll


        


























        ##### Backtracking, gives TLE for last 6 TCs #####
        # n = len(nums)
        # if len(nums) < 3:
        #     return []
        # res = []
        # nums.sort()

        # def findTriplet(start, target, path):
            
        #     if target == 0 and len(path) == 3:
        #         res.append(path)
        #         return
        #     if len(path) == 3:
        #         return
        #     if path and path[0] > 0:
        #         return
        #     for i in range(start, n):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         findTriplet(i+1, target-nums[i], path+[nums[i]])
        
        # findTriplet(0, 0, [])
        # return res

        
            