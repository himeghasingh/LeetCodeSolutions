class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = re.split(r'(\+|\-)', expression)
        n = len(result)
        numerator = []
        denominator = []
        if result[0] == '':
            result = result[1:]
        else:
            result.insert(0, '+')
        n = len(result)
        for i in range(0, n):
            ch = result[i]
            if ch == '+' or ch == '-':
                number = result[i+1]
                index = number.index('/')
                numr = number[0:index]
                denr = number[index+1:]
                denominator.append(int(denr))
                if ch == '-':
                    numerator.append(-(int(numr)))
                else:
                    numerator.append(int(numr))

        flen = len(numerator)
        bigden = 1
        bignum = 0
        for d in denominator:
            bigden = bigden * d
        for i in range(0, flen):
            den = denominator[i]
            num = numerator[i]
            mul = bigden // den
            bignum += (num*mul)
        print(bigden, "denominator")
        print(bignum, "numerator")
        def hcf(a, b):
            while b:
                a, b = b, a % b
            return a
        if bignum == 0:
            return '0/1'
        elif abs(bignum) == 1 or abs(bigden) == 1:
            return str(bignum)+"/"+str(bigden)
        else:
            f = hcf(bignum, bigden)
            bignum = bignum // f
            bigden = bigden // f
            return str(bignum)+"/"+str(bigden)
        




        



       
        