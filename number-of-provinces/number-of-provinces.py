class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        provinces = n

        for i in range (0, n):
            for j in range(i+1, n):
                if (isConnected[i][j] == 1):
                    if (uf.find(i) != uf.find(j)):
                        provinces -= 1
                        uf.union(i, j)
        return provinces

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, target):
        if(self.parent[target] != target):
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

    def union(self, i, j):
        ipar = self.find(i)
        jpar = self.find(j)
        if (ipar == jpar):
            return
        elif (self.rank[ipar] > self.rank[jpar]):
            self.parent[jpar] = ipar
        elif (self.rank[jpar] > self.rank[ipar]):
            self.parent[ipar] = jpar
        else:
            self.parent[ipar] = jpar
            self.rank[jpar] += 1


        