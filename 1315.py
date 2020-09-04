#LeetCode problem 1315: Sum of Nodes with Even-Valued Grandparent
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        su=[]
        self.sumEverything(root,None,None,su)
        return sum(su)
    
    def sumEverything(self,root: TreeNode, parent:TreeNode, grandparent:TreeNode,s: List):
        if root is None:
            return 
        elif grandparent is not None and grandparent.val%2==0:
            s.append(root.val)
        self.sumEverything(root.left,root,parent,s)
        self.sumEverything(root.right,root,parent,s)