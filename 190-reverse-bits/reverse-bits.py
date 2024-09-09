class Solution:
    def reverseBits(self, n: int) -> int:

        binstr = "{:032b}".format(n)
        return int(binstr[::-1], 2)

    