"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        queue = deque()
        stack = []
        stack.append(root)
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            for c in node.children:
                stack.append(c)
        return res[::-1]
        

        


















        #####Recursive#####
        # ll = []
        
        # def traverse(node):
        #     if not node:
        #         return
        #     for nc in node.children:
        #         traverse(nc)
        #     ll.append(node.val)

        # traverse(root)
        # return ll
        