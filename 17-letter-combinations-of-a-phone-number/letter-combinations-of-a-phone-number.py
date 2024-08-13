class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        letterNumMap = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        res = []

        def makeComb(index, pattern):
            if index == n:
                res.append(pattern)
                return
            currNum = digits[index]
            currLetters = letterNumMap[currNum]
            for letter in currLetters:
                makeComb(index + 1, pattern + letter)

        makeComb(0, "")
        return res

            


        