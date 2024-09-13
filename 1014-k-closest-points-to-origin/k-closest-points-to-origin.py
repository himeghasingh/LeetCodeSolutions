class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)
        # res = []

        # dist = defaultdict(int)
        # for i in range(0, n):
        #     x, y = points[i]
        #     dist[i] = (x * x) + (y * y)

        # sortedDist = dict(sorted(dist.items(), key=lambda item: item[1]))
        # indexes = list(sortedDist.keys())[0:k]

        # i = 0
        # while(k > 0):
        #     res.append(points[indexes[i]])
        #     k -= 1
        #     i += 1

        # return res

        heap = []
        for i in range(0, k):
            x, y = points[i]
            distance =  -1 * ((x * x) + (y * y))
            heap.append((distance, points[i]))
        heapq.heapify(heap)

        for i in range(k, n):
            x, y = points[i]
            distance =  -1 * ((x * x) + (y * y))
            if distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (distance, points[i]))

        res = []
        for i in range(0, len(heap)):
            res.append(heap[i][1])
        return res




        
    #     heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
    #     heapq.heapify(heap)
    #     for i in range(k, len(points)):
    #         dist = -self.squared_distance(points[i])
    #         heapq.heappop()
    #         heapq.heappush()
        
    #     # Return all points stored in the max heap
    #     return [points[i] for (_, i) in heap]
    
    # def squared_distance(self, point: List[int]) -> int:
    #     """Calculate and return the squared Euclidean distance."""
    #     return point[0] ** 2 + point[1] ** 2

    