# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recTree(start, end, root):
            if start > end:
                return None
            else:
                maxnum = max(nums[start:end+1])
                maxindex = nums.index(maxnum)
                root = TreeNode(maxnum)
                root.left = recTree(start, maxindex-1, root)       
                root.right = recTree(maxindex+1, end, root)   

            return root
        
        n = len(nums)
        tree = recTree(0, n-1, TreeNode())
        return tree


        