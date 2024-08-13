class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        results = []

        def makeSum(target, startInd, path):
            if target == 0:
                if path not in results:
                    results.append(path)
                    return
            for i in range(startInd, n):
                if i > startInd and candidates[i] == candidates[i - 1]:
                    continue 
                if candidates[i] > target:
                    return
                makeSum(target-candidates[i], i+1, path+[candidates[i]]) 

        for i in range(0, n):
            makeSum(target, i, [])
        return results

        
        
