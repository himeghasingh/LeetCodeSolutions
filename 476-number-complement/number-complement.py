class Solution:
    def findComplement(self, num: int) -> int:

        if num == 0:
            return 0

        def toBin(num):
            s = ""
            while (num > 0):
                rem = num % 2
                s = str(rem) + s
                num = num // 2
            return s

        def toDec(comp):
            n = len(comp)
            res = 0
            for i in range(0, n):
                ch = comp[n-i-1]
                print("ch:", ch)
                if ch == '1':
                    res += math.pow(2, i)
            return int(res)
        
        binNum = toBin(num)
        binComp = ""
        for ch in binNum:
            if ch == '0':
                binComp += '1'
            else:
                binComp += '0'
        decComp = toDec(binComp)
        
        return decComp





        