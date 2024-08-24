class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        is_odd = length % 2 != 0
        first_half = n[:(length + 1) // 2] if is_odd else n[:length // 2]
        
        candidates = set()
        
        # Candidate by modifying the first half
        middle = int(first_half)
        for i in [-1, 0, 1]:
            modified_first_half = str(middle + i)
            if is_odd:
                candidate = modified_first_half + modified_first_half[:-1][::-1]
            else:
                candidate = modified_first_half + modified_first_half[::-1]
            candidates.add(candidate)
        
        # Edge cases
        candidates.add('9' * (length - 1))
        candidates.add('1' + '0' * (length - 1) + '1')
        
        # Remove the original number from candidates
        candidates.discard(n)
        
        # Filter out any empty strings (just in case)
        candidates = {c for c in candidates if c}
        
        # Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        return closest_palindrome





        # lenn = len(n)
        # print(lenn)
        # num = int(n)
        # if n == '10' or n == '11':
        #     return '9'
        # if lenn == 1 or n != n[::-1]:
        #     print("entered if")
            
        #     if lenn == 1:
        #         return str(int(n) - 1)
        #     if lenn % 2 != 0:
        #         firsthalf = n[0 : lenn//2]
        #         return firsthalf + n[lenn//2] + firsthalf[::-1]
        #     if lenn % 2 == 0:
        #         firsthalf = n[0 : lenn//2]
        #         return firsthalf + firsthalf[::-1]
        # else:
        #     print("entered else")
        #     num1 = -1
        #     num2 = -1
        #     if lenn % 2 == 0:
        #         first1 = str(int(n[0 : lenn//2]) - 1)
        #         num1 = first1 + first1[::-1]
        #         first2 = str(int(n[0 : lenn//2]) + 1)
        #         num2 = first2 + first2[::-1]
        #     else:
        #         first1 = str(int(n[0 : ((lenn//2)+1)]) - 1)
        #         num1 = first1 + first1[0:len(first1)-1][::-1]
        #         first2 = str(int(n[0 : ((lenn//2)+1)]) + 1)
        #         num2 = first2 + first2[0:len(first2)-1][::-1]
        #     dist1 = num - int(num1)
        #     dist2 = int(num2) - num
        #     if dist1 < dist2:
        #         return num1
        #     elif dist2 > dist1:
        #         return num2
        #     else:
        #         return num1



            
            
            
            
            
            
            
            
            
            
            
            # print("entered else")
            
            # smallnum = str(num - 1)
            # lens = len(smallnum)
            # bignum = str(num + 1)
            # lenb = len(bignum)
            # sfinal = ""
            # bfinal = ""

            # if lens % 2 != 0:
            #     sfirst = smallnum[0 : lens//2]
            #     sfinal =  sfirst + smallnum[lens//2] + sfirst[::-1]
            # if lens % 2 == 0:
            #     sfirst = smallnum[0 : lens//2]
            #     sfinal =  sfirst + sfirst[::-1]
            
            # if lenb % 2 != 0:
            #     bfirst = bignum[0 : lenb//2]
            #     bfinal =  bfirst + bignum[lenb//2] + bfirst[::-1]
            # if lens % 2 == 0:
            #     bfirst = bignum[0 : lenb//2]
            #     bfinal =  bfirst + bfirst[::-1]

            # sfinalnum = int(sfinal)
            # bfinalnum = int(bfinal)
            # print("sfinal", sfinal)
            # print("bfinal", bfinal)
            # sdist = num - sfinalnum
            # bdist = bfinalnum - num
            # if sdist < bdist:
            #     return sfinal
            # elif bdist < sdist:
            #     return bfinal
            # else:
            #     return sfinal
            

            









        # i = 1
        # num = int(n)
        # while True:
        #     bigflag = False
        #     smallflag = False
        #     bignum = str(num + i)
        #     smallnum = str(num - i)
        #     if int(smallnum) >= 0:
        #         if smallnum == smallnum[::-1]:
        #             smallflag = True
        #     if bignum == bignum[::-1]:
        #         bigflag = True
        #     if (bigflag and smallflag):
        #         return smallnum
        #     elif bigflag:
        #         return bignum
        #     elif smallflag:
        #         return smallnum
        #     i += 1



        