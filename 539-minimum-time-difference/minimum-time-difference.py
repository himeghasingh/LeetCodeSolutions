class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        minPoints = [0] * n
        for i in range(0, n):
            hr, mins = timePoints[i].split(":")
            hr = int(hr)
            mins = int(mins)
            minPoints[i] = (hr*60) + mins
        minDiff = float("inf")
        minPoints.sort()

        for i in range(0, n-1):
            diff = abs(minPoints[i+1]-minPoints[i])
            currDiff = min(diff, 1440-diff)
            minDiff = min(minDiff, currDiff)
        minDiff = min(minDiff, minPoints[-1]-minPoints[0], 1440- (minPoints[-1]-minPoints[0]))
        return minDiff

    


        