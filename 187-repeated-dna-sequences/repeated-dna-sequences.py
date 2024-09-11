class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        print(n)
        strMap = defaultdict(int)
        if n <= 10:
            return []
        for i in range(0, n-9):
            substr = s[i:i+10]
            strMap[substr] += 1
        res = []
        for k, v in strMap.items():
            if v > 1:
                res.append(k)
        # print(res)
        return res


            

        