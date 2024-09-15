class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = dict(sorted(count.items(), key = lambda item:item[1], reverse=True))
        res = list(count.keys())[0:k]
        return res
        