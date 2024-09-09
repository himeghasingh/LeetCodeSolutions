class Solution:
    def validPalindrome(self, s: str) -> bool:
        # count = Counter(s)
        # print(count)
        # c = 0
        # for ch, freq in count.items():
        #     if freq == 1:
        #         c += 1
        #     if c > 2:
        #         return False
        # return True
                
        n = len(s)
        start = 0
        end = n-1
        c = 0
        if s == s[::-1]:
            return True
        while(start <= end):
            if s[start] != s[end]:
                c += 1
                newstr1 = s[0:start+1] + s[start+1:end] + s[end+1:]
                newstr2 = s[0:start] + s[start+1:end] + s[end:]
                print(newstr1, newstr2)
                if newstr1 == newstr1[::-1] or newstr2 == newstr2[::-1]:
                    return True
                else:
                    return False
            
            start += 1
            end -= 1

        