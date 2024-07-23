class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        acqlist = defaultdict(set)

        for l in logs:
            first = l[1]
            second = l[2]
            acqlist[first].add(second)
            acqlist[second].add(first)
            acqfirst = acqlist[first]
            acqsecond = acqlist[second]
            
            if acqfirst is not acqsecond:
                union_set = acqfirst | acqsecond
                for node in union_set:
                    acqlist[node] = union_set

            if len(acqlist[0]) == n:
                return l[0]

        return -1
