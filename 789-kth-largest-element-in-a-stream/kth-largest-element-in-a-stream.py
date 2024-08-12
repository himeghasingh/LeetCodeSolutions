class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
       

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums
    #     for i in range(0, len(self.nums)):
    #         self.nums[i] = -1 * self.nums[i]
    #     heapq.heapify(self.nums)
        

    # def add(self, val: int) -> int:
    #     heapq.heappush(self.nums, (-1*val))
    #     c = 0
    #     temp = []
    #     while (c < self.k-1):
    #         temp.append(heapq.heappop(self.nums))
    #         c += 1
    #     res = heapq.heappop(self.nums)
    #     heapq.heappush(self.nums, res)
    #     for t in temp:
    #         heapq.heappush(self.nums, t)
    #     return (res*-1)


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)