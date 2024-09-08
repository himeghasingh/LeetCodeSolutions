class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        actualtotal = (m + n) * mean
        currtotal = sum(rolls)
        diff = actualtotal - currtotal
        res = []
        # print(diff)
        if diff > n*6 or diff < n:
            return []
        part = diff // n
        extra = diff % n
        print("part", part)
        print("extra =", extra)
        for i in range(0, n-extra):
            res.append(part)
        for i in range(0, extra):
            res.append(part+1)

        # print(res)
        return res




        