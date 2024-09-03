class Solution:
    def getLucky(self, s: str, k: int) -> int:
        currsum = ""
        for ch in s:
            currsum += str(ord(ch) - ord('a') + 1)
        currsum = int(currsum)
        while k>0:
            newsum = 0
            while currsum>0:
                newsum += currsum % 10
                currsum = currsum // 10
            currsum = newsum
            k -= 1
        return currsum
        