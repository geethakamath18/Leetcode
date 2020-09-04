#LeetCode problem 938: Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        s=[]
        self.returnSum(root, L, R, s)
        return(sum(s))
    
    def returnSum(self, root: TreeNode, L: int, R: int, s:List):   
        if root is None:
            return 
        if root.val<=R and root.val>=L:
            s.append(root.val)
        self.returnSum(root.left, L, R, s)
        self.returnSum(root.right, L, R, s)