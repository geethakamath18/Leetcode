#LeetCode problem 872: Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1=[]
        s2=[]
        self.getSequence(root1,s1)
        self.getSequence(root2,s2)
        if s1==s2: return True
        return False
        
    def getSequence(self, root:TreeNode,l:List):
        if root is None:
            return
        if root.left is None and root.right is None:
            l.append(root.val)
        self.getSequence(root.left,l)
        self.getSequence(root.right,l)