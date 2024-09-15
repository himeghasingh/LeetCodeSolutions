class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda points:points[1])
        arrows = 1
        lastPos = points[0][1]
        for i in range(1, n):
            if points[i][0] > lastPos:
                arrows += 1
                lastPos = points[i][1]
        return arrows
            
        # points.sort(key=lambda points: points[1]-points[0], reverse=True)
        # print(points)

        # count = 0
        # n = len(points)
        # visited = set()
        # i = 0
        # arrows = 0
        # while count < n:
        #     start, end = points[i]
        #     print("\n", visited)
        #     if (start, end, i) not in visited:
        #         arrows += 1
        #         print("arrows = ", arrows)
        #         visited.add((start, end, i))
        #         count += 1
        #         for j in range(0, n):
        #             s, e = points[j]
        #             if (s, e, j) not in visited:
        #                 print("s = ", s, "e = ", e, "start = ", start, "end = ", end)
        #                 if start <= s <= end or start <= e <= end:
        #                     print("adding to visited")
        #                     visited.add((s, e, j))
        #                     count += 1
        #     i += 1
        # print(arrows)
        # return arrows



        