#LeetCode problem 1123: Lowest Common Ancestor of Deepest Leaves 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        h,subtree= self.getHeight(root,0)
        return subtree
    
    def getHeight(self, root: TreeNode, h: int):
        if root is None:
            return
        if root is not None:
            return h, root
        
        h+=1
        l,l_node=self.getHeight(root.left,h)
        r,r_node=self.getHeight(root.right,h)
        
        if(l==r):
            return l, node
        elif(l>=r):
            return l,l_node
        else:
            return r,r_node

