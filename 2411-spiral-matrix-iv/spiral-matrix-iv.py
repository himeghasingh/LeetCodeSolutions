# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix  = [[-1]*n for i in range (m)]
        rstart = 0
        cstart = 0
        rend  = m - 1
        cend = n - 1
        flag = 0
        turn = 1
        while head:
            if turn % 4 == 1:
                for j in range(cstart, cend+1):
                    matrix[rstart][j] = head.val
                    head = head.next
                    if not head:
                        flag = 1
                        break
                rstart += 1

            if turn % 4 == 2:
                for i in range(rstart, rend+1):
                    matrix[i][cend] = head.val
                    head = head.next
                    if not head:
                        flag = 1
                        break
                cend -= 1

            if turn % 4 == 3:
                for j in range(cend, cstart-1, -1):
                    matrix[rend][j] = head.val
                    head = head.next
                    if not head:
                        flag = 1
                        break
                rend -= 1
            if turn % 4 == 0:
                for i in range(rend, rstart-1, -1):
                    matrix[i][cstart] = head.val
                    head = head.next
                    if not head:
                        flag = 1
                        break
                cstart += 1
            if flag == 1:
                break
            turn += 1

        return matrix
        