# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # if not head:
        #     return []
        # res = []
        # curr = head
        # n = 0
        # while curr:
        #     curr = curr.next
        #     n += 1

        # count = 0
        # flag = 0
        # if n > k:
        #     flag = 1
        #     count = n // k
        # else:
        #     count = 1
        
        # i = 0



        # while head:
        #     if count == 1:
        #         res.append(ListNode(head.val))
        #         head = head.next
        #         i += 1
        #         continue
                
            
        #     newhead = head
        #     dupnewhead = newhead
        #     cnt = 1
        #     print(res)
        #     print("i = ", i)
            
        #     while (cnt < count+1 and i == 0 and flag == 1) or (cnt < count and flag == 0) or (cnt < count and i > 0 and flag == 1) :
        #         print("iterating cnt = ", cnt)
        #         head = head.next
        #         newhead = ListNode(head.val)
        #         newhead = newhead.next
                
        #         cnt += 1

        #     print("cnt = ", cnt)
        #     print("dupnewhead = ", dupnewhead)
            
        #     res[i] = dupnewhead
        #     i += 1
            
        # print(res)

        # # for i in range (0,len(res)):

        # #     if res[i] == []:
        # #         res[i] = None
            
        
        # return res

        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        partSize = n // k
        extra = n % k

        res = []
        curr = head

        for i in range(k):
            partLength = partSize + (1 if i < extra else 0)
            if partLength == 0:
                res.append(None)
            else:
                partHead = curr
                for j in range(partLength - 1):
                    if curr:
                        curr = curr.next
                if curr:
                    nextPart = curr.next
                    curr.next = None
                    curr = nextPart
                res.append(partHead)

        return res