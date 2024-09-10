# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if not head or not head.next:
            return head
        dummy = head
        while head and head.next:
            a = head.val
            b = head.next.val
            c = gcd(a,b)
            temp = head.next
            head.next = ListNode(c)
            head.next.next = temp

            head = head.next.next
        return dummy

        