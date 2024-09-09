class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        i = 1
        sq = i * i

        while (x >= sq):
            i += 1
            sq = i * i
        return i-1

        