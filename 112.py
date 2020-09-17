#LeetCode problem 112: Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return(root.val==sum)
        res=[]
        self.isTrue(root,sum,res)
        print(res)
        if res.count(1)>=1:
            return True
        return False
    
    def isTrue(self, root: TreeNode, s: int, res) -> bool:    
        if root is not None:
            if not root.left and not root.right and root.val == s:
                 res.append(1)
            if root.left is not None:
                self.isTrue(root.left,s-root.val,res)
            if root.right is not None:
                self.isTrue(root.right,s-root.val,res)