class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)
        res = []

        dist = defaultdict(int)
        for i in range(0, n):
            x, y = points[i]
            dist[i] = (x * x) + (y * y)

        sortedDist = dict(sorted(dist.items(), key=lambda item: item[1]))
        indexes = list(sortedDist.keys())[0:k]

        i = 0
        while(k > 0):
            res.append(points[indexes[i]])
            k -= 1
            i += 1

        return res

    