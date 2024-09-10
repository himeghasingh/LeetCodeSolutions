class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        len1 = len(slots1)
        len2 = len(slots2)
        slots1.sort()
        slots2.sort()
        i = 0
        j = 0
        while (i < len1 and j < len2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            if min(e1, e2) - max(s1, s2) >= duration:
                return [max(s1, s2), (max(s1, s2) + duration)]
            if e1 >= e2:
                j += 1
            else:
                i += 1
        return []























        # def checkOverlap(a1, b1, a2, b2):
        #     if a1 >= a2 and b1 <= b2 and b1 - a1 >= duration:
        #         slots.append([a1, a1+duration])
        #         return True
        #     if a2 >= a1 and b2 >= b1 and a2 < b1 and b1 - a2 >= duration:
        #         slots.append([a2, a2+duration])
        #         return True

        # len1 = len(slots1)
        # len2 = len(slots2)
        # slots1.sort()
        # slots2.sort()
        # i = 0
        # j = 0
        # slots = []
        # for i in range(0, len1):
        #     for j in range(0, len2):
        #         a1, b1 = slots1[i]
        #         a2, b2 = slots2[j]
        #         if checkOverlap(a1, b1, a2, b2):
        #             return slots[0]
        #         if checkOverlap(a2, b2, a1, b1):
        #             return slots[0]
        # if slots:
        #     return slots[0]
        # return []

        
        



        