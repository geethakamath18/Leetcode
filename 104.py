#LeetCode problem 104: Maximum Depth of Binary Tree 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
             return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        if l>r: return l+1  
        return r+1
        
