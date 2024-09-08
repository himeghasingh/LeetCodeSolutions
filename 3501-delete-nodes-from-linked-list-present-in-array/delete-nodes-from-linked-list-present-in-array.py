# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        numsSet = set(nums)
       
        prev = ListNode(None)
        prev.next = head
        dummy = prev
        
        flag = 0

        while head:
            if head.val in numsSet:
                prev.next = head.next
                flag = 1
            else:
                flag = 0
            if flag == 0:
                prev = head
            head = head.next
        return dummy.next
             


        