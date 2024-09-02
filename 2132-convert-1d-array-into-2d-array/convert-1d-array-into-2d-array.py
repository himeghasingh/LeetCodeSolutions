class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        # newarr = []*m for i in range(m)
        newarr = []
        for i in range(0, len(original), n):
            newarr.append(original[i:i+n])
        # print(newarr)
        return newarr



        