class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # oddPrefix = [0] * (n+1)
        # for i in range(0, n):
        #     if nums[i] % 2 != 0:
        #         oddPrefix[i+1] = 1 + oddPrefix[i]
        #     else:
        #          oddPrefix[i+1] = oddPrefix[i]
        # # print (oddPrefix)
        # c = 0

        # for i in range(0, n-k+1):
        #     for j in range(i+k, n+1):
        #         if oddPrefix[j] - oddPrefix[i] == k:
        #             c += 1
        #         elif oddPrefix[j] - oddPrefix[i] > k or ((oddPrefix[j] - oddPrefix[i] < k) and (n - j < k - (oddPrefix[j] - oddPrefix[i]))):
        #             break
        # # print(c)
        # return c
        n = len(nums)
        oddPrefix = [0] * (n + 1)

        for i in range(0, n):
            if nums[i] % 2 != 0:
                oddPrefix[i+1] = 1 + oddPrefix[i]
            else:
                 oddPrefix[i+1] = oddPrefix[i]

        prefixCount = defaultdict(int)
        count = 0

        for j in range(0, n + 1):
            if oddPrefix[j] - k in prefixCount:
                count += prefixCount[oddPrefix[j] - k]
            prefixCount[oddPrefix[j]] += 1

        return count