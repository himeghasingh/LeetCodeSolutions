class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = 'aeiou'
        res = 0
        mask = 0
        maskIndex = {0 :-1}

        for i, ch in enumerate(s):
            if ch in vowels:
                mask = mask ^ (1 + ord(ch) - ord('a'))
            if mask in maskIndex:
                length = i - maskIndex[mask]
                res = max(res, length)
            else:
                maskIndex[mask] = i
        return res


        ##### PREFIXSUM TLE #####
        # n = len(s)
        # evenVowel = [[0]*5 for i in range(n+1)]
        # vowel = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        # maxlen = float("-inf")


        # for i in range(0, n):
        #     ch = s[i]
        #     evenVowel[i+1] = evenVowel[i][:]
        #     if ch in vowel:
        #         evenVowel[i+1][vowel[ch]] += 1

        # def prefixDiff(start, end):
        #     for i in range(0, 5):
        #         diff = evenVowel[end][i] - evenVowel[start][i]
        #         if diff % 2 != 0:
        #             return False
        #     return True

        # for i in range(0, n):
        #     for j in range(0, n+1):
        #         substr = s[i:j]
        #         if prefixDiff(i, j):
        #             maxlen = max(maxlen, j-i)
        # return maxlen

        
        