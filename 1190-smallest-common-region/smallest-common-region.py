class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        rows = len(regions)
        lastInd1 = lastInd2 = len(regions)
        
        while region1 != region2:
            if lastInd1 > lastInd2:
                region1, lastInd1 = self.whoContains(regions, region1, lastInd1) 
            elif lastInd2 > lastInd1:
                region2, lastInd2 = self.whoContains(regions, region2, lastInd2)
            else:
                region1, lastInd1 = self.whoContains(regions, region1, lastInd1) 
                region2, lastInd2 = self.whoContains(regions, region2, lastInd2)

        return region1


    def whoContains(self, regions, region, lastInd):
        for r in range(lastInd-1, -1, -1):
            if region in regions[r]:
                return regions[r][0], r
