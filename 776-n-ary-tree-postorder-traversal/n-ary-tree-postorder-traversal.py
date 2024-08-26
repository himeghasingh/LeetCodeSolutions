"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ll = []
        
        def traverse(node):
            if not node:
                return
            for nc in node.children:
                traverse(nc)
            ll.append(node.val)

        traverse(root)
        return ll
        