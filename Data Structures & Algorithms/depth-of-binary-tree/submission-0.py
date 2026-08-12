# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Check if root is NULL
        if not root:
            return 0
        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0
        return 1 + max(left,right)
        