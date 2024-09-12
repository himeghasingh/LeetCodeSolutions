class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            flag = 0
            for ch in word:
                if ch not in allowed:
                    flag = 1
                    break
            if flag == 0:
                c += 1
        return c

        