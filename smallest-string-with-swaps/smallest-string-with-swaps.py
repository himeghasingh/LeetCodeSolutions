class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for p in pairs:
            uf.union(p[0], p[1])
        for i in range (0, len(uf.root)):
            uf.root[i] = uf.find(uf.root[i])

        subs = defaultdict(list)
        for i in range (0, len(s)):
            k = uf.find(i)
            subs[k].append(s[i])
        for k,v in subs.items():
            v.sort()

        res = [""] * len(s)
        for i in range(0, len(s)):
            ele = subs[uf.root[i]][0]
            res[i] += ele
            subs[uf.root[i]].remove(ele)

        return "".join(res)

class UnionFind:
    def __init__(self, n):
        self.root = [0] * n
        self.rank = [1] * n
        for i in range(0, n):
            self.root[i] = i
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            xrank = self.rank[xroot]
            yrank = self.rank[yroot]
            if xrank > yrank:
                self.root[yroot] = xroot
            elif yrank > xrank:
                self.root[xroot] = yroot
            elif xrank == yrank:
                self.root[yroot] = xroot
                self.rank[xroot] += 1
        