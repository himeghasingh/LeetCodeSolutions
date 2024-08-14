class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 1:
            return 1

        maxLen = 0
        l = 0
        r = 0
        substr = ""
        ch = ''

        while(l <= r  and r < n):
            ch = s[r]
            if ch in substr:
                maxLen = max(maxLen, len(substr))
                dupIndex = substr.index(ch)
                # if dupIndex < 0:
                #     dupIndex = 0
                l += dupIndex+1
                r = l
                substr = s[l:r+1]
            else:
                substr += ch
            r += 1

        maxLen = max(maxLen, len(substr))
        return maxLen
            









# while(l <= r  and r < n):
        #     print("\n")
        #     print(substr, "substr")
        #     if s[r] in substr:
        #         maxLen = max(maxLen, len(substr))
        #         dupIndex = substr.index(s[r])
        #         print("duplicate ind = ", dupIndex)
        #         if dupIndex < 0:
        #             dupIndex = 0
        #         l += dupIndex+1
        #         substr = s[l:r+1]
        #         r += dupIndex
        #     else:
        #         substr += s[r]
        #     r += 1
        # print(substr)
        # maxLen = max(maxLen, len(substr))
        # print(maxLen)
        # return maxLen
        