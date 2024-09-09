class Solution:
    def reverse(self, x: int) -> int:
        strr = str(abs(x))
        strr = strr[::-1]
        if x < 0:
            strr = '-' + strr
        newint = int(strr)
        if -1 * ((2**31) - 1) <= newint <= (2**31) + 1:
            return newint
        return 0

        