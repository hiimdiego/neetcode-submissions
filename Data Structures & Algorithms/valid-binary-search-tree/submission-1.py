# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #helper function
        def valid(node, left, right):
            #Check if node is null
            if not node:
                return True
            #Check BST properties
            if not(node.val > left and node.val < right):
                return False
            #recurse
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        #return
        return valid(root, float('-inf'), float('inf'))
            

