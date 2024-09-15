class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # count = dict(sorted(count.items(), key = lambda item:item[1], reverse=True))
        # res = list(count.keys())[0:k]
        # return res
        # return heapq.nlargest(k, count.keys(), count.get)
        heap = []
        heapq.heapify(heap)
        i = 0

        for key,val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, [val, key])
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [val, key])
        res = []
        print(heap)
        for val, key in heap:
            res.append(key)
        return res



        