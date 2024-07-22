class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for e in edges:
            addedge = uf.union(e[0], e[1])
            if not addedge:
                return False
        root = uf.root[0]
        for i in range (1, len(uf.root)):
            target = uf.root[i]
            if root != uf.find(target):
                return False
        return True



class UnionFind:
    def __init__(self, n):
        self.root = [0] * n
        self.rank = [1] * n
        for i in range(0,n):
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
                for r in self.root:
                    self.root[yroot] = xroot
            elif yrank > xrank:
                for r in self.root:
                    self.root[xroot] = yroot
            elif xrank == yrank:
                for r in self.root:
                    self.root[yroot] = xroot
                self.rank[xroot] += 1
            return True
        else:
            return False

                