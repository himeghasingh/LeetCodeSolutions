class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        dist = -float("inf")
        # for i in range (0, len(arrays)):
        #     minn1 = min(arrays[i])
        #     maxn1 = max(arrays[i])
        #     for j in range (i+1, len(arrays)):
        #         minn2 = min(arrays[j])
        #         maxn2 = max(arrays[j])
        #         dist1 = abs(minn1-maxn2)
        #         dist2 = abs(minn2-maxn1)
        #         dist = max(dist1, dist2)
        #         if dist > maxdist:
        #             maxdist = dist
        # return maxdist

        # maxdist = -float("inf")
        # minn1 = float ("inf")
        # minn2 = float ("inf")
        # maxn1 = -float("inf")
        # maxn2 = -float("inf")
        # minindex = -1
        # maxindex = -1
        # n1 = 
        # for i in range (0, len(arrays)-1):
        #     d = (max(abs(max(arrays[i])-min(arrays[i+1])), abs(max(arrays[i+1])-min(arrays[i]))
        #     if d > dist:
        #         dist = d



        # minval = arrays[0][0]
        # maxval = arrays[0][-1]

        # for arr in arrays:

        #     dist1 = abs(maxval - arr[0])
        #     dist2 = abs(arr[-1] - minval)
        #     dist = max(dist, dist1, dist2)
        #     if(arr[0] < minval):
        #         minval = arr[0]
        #     if(arr[-1] > maxval):
        #         maxval = arr[-1]
        # return dist
            

        #     d = (max(abs(max(arrays[i])-min(arrays[i+1])), abs(max(arrays[i+1])-min(arrays[i]))))
        #     if d > dist:
        #         dist = d
        #     dist1 = abs(max(arrays[i])-min(arrays[i+1]))
        #     dist2 = abs(max(arrays[i+1])-min(arrays[i]))
        #     if dist1 >= dist2:
        #         n1 = max(arrays[i])
        #         n2 = min(arrays[i+1])
        #         index1 = i
        #         index2 = i+1
        #     else:
        #         n1 = max(arrays[i+1])
        #         n2 = min(arrays[i])
        #         index1 = i+1
        #         index2 = i

        # return dist

        #     if min(arrays[i]) < minn1 and i != maxindex:
        #         minn1 = min(arrays[i])
        #         minindex = i
        #     if min(arrays[i+1]) < minn2 and i != maxindex:
        #         minn2 = min(arrays[i+1])
        #         minindex = i+1
        #     if max(arrays[i]) > maxn1 and i != minindex:
        #         maxn1 = max(arrays[i])
        #         maxindex = i
        #     if max(arrays[i+1]) > maxn2 and i != minindex:
        #         maxn2 = max(arrays[i+1])
        #         maxindex = i+1
        #     dist1 = abs(minn1-maxn2)
        #     dist2 = abs(minn2-maxn1)
        #     dist = max(dist1, dist2)
        #     print("minn1: ", minn1, "minn2: ", minn2, "maxn1: ", maxn1, "maxn2: ", maxn2, "dist1: ", dist1, "dist2: ", dist2, "dist: ", dist)
        #     if dist > maxdist:
        #         maxdist = dist
        # return maxdist
        min_val, max_val = arrays[0][0], arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            current_min, current_max = arrays[i][0], arrays[i][-1]

            max_distance = max(
                max_distance,
                abs(max_val - current_min),
                abs(current_max - min_val)
            )

            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance
                
            