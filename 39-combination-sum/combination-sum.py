class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        results = []

        def makeSum(target, startInd, path):
            if target == 0:
                if sorted(path) not in results:
                    results.append(sorted(path))
                    return
            for i in range(0, n):
                if candidates[i] > target:
                    return
                makeSum(target-candidates[i], i+1, path+[candidates[i]]) 

        for i in range(0, n):
            makeSum(target, i, [])
        return results
