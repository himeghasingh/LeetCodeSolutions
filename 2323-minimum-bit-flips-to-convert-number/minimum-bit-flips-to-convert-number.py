class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def toBin(num):
            res = ""
            while(num > 0):
                res = str((num % 2)) + res
                num = num // 2
            return res
        num1 = toBin(start)
        num2 = toBin(goal)
        len1 = len(num1)
        len2 = len(num2)
        diff = abs(len1 - len2)
        if len1 > len2:
            num2 = ('0' * diff) + num2
        elif len2 > len1:
            num1 = ('0' * diff) + num1
        lenn = len(num1)
        c = 0
        for i in range(0, lenn):
            if num1[i] != num2[i]:
                c += 1
        print(c)
        return c


        