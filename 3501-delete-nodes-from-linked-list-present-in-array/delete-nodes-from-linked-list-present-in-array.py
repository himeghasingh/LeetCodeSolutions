# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        numsSet = set(nums)
       
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        
        while head:
            if head.val in numsSet:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
             


        