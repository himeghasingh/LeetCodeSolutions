# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        maxwidth = 0

        queue = deque()
        queue.append([root,0])
        
        while queue:
            levelLen = len(queue)
            levelHeadNode, levelHeadIndex = queue[0] 
            for i in range(levelLen):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append([node.left,  2 * index])
                if node.right:
                    queue.append([node.right, 2 * index + 1])
            
            currWidth = index - levelHeadIndex + 1
            maxwidth = max(maxwidth, currWidth)
        
        return maxwidth
























        # nodemap = defaultdict(list)
        # print("root : ", root)

        # def findDepth(node):
        #     if not node:
        #         return 0
        #     return 1 + max(findDepth(node.left), findDepth(node.right))
        # depth = findDepth(root)
        # print("depth = ", depth)

        # def make_tree_complete(root):
        #     if not root:
        #         return []
            
        #     queue = deque([root])
        #     complete_tree = []

        #     while queue:
        #         node = queue.popleft()
        #         complete_tree.append(node.val if node else None)
                
        #         if node:
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     print(complete_tree)
    
        #     return complete_tree

        # def findWidth(node, level):
        #     if not node:
        #         if level <= depth:
        #             nodemap[level].append(None)
        #             return
        #         else:
        #             print("why here, level is", level)
        #             return
        #     nodemap[level].append(node.val)
        #     findWidth(node.left, level+1)
        #     findWidth(node.right, level+1)

        # newroot = make_tree_complete(root)[0]
        # print("\n",newroot)
        # # findWidth(newroot, 1)
        # # print(nodemap)
        # return depth
        
        

        