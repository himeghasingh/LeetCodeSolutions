class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        res = []
        strMap = defaultdict(int)
        seen = set()

        if n <= 10:
            return []
        for i in range(0, n - 10 + 1):
            substr = s[i:i+10]
            strMap[substr] += 1
            
            if strMap[substr] > 1:
                if substr not in seen:
                    res.append(substr)
                    seen.add(substr)
            
        return res


            

        