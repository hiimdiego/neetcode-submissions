# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Perform in order traveral
        curr = root
        stack = []
        num = 0
        #check curr and stack
        while curr or stack:
            #check curr and append vals
            while curr:
                stack.append(curr)
                curr = curr.left
            #pop and check value of num
            curr = stack.pop()
            num += 1
            if num == k:
                return curr.val
            #check right subtree
            curr = curr.right
        

            