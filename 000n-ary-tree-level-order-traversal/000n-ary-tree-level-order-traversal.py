"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, 0])
        prev = None
        traversal = [[root.val]]
        while queue:
            node, level = queue.popleft()
            if node.children:
                for c in node.children:
                    if c:
                        if len(traversal) != level + 2:
                            traversal.append([])
                        traversal[level+1].append(c.val)
                        queue.append([c, level+1])
        return traversal


            

            

            
            

        