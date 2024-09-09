class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def toBin(num):
            strr = ""
            while (num > 0):
                strr = str(num%2) + strr
                num = num // 2
            return strr
       
        def toDec(num):
            summ = 0
            c = 0
            for i in range(len(num)-1, -1, -1):
                summ += int(num[i]) * (2 ** c)
                c += 1
            return summ
        resnum = toDec(a) + toDec(b)
        if resnum == 0:
            return "0"
        return toBin(resnum)
