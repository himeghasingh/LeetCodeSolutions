# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def findInTree(value, root, positions):
            if not root:
                return 
            if root.val == value:
                positions.append(root)
            findInTree(value, root.left, positions)
            findInTree(value, root.right, positions)
            return positions

        headPos = findInTree(head.val, root, [])
        head = head.next
        while head:
            nodePos = []
            for pos in headPos:
                if pos.left and pos.left.val == head.val:
                    nodePos.append(pos.left)
                if pos.right and pos.right.val == head.val:
                    nodePos.append(pos.right)
            if nodePos == []:
                return False
                
            headPos = nodePos
            head = head.next
                
     
        return True
            




        



        