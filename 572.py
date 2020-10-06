#LeetCode problem 572: Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res1=[]
        res2=[]
        res1=self.getInorder(s,res1)
        res2=self.getInorder(t,res2)
        s1=''
        for i in range(len(res1)):
            s1+=res1[i]
        s2=''
        for i in range(len(res2)):
            s2+=res2[i] 
        print(s1,s2)
        return s2 in s1
    
    def getInorder(self, root:TreeNode,res):
        if root is None:
            res.append("null")
            return
        if root.left is None:
            res.append("lnull")
        elif root.right is None:
            res.append("rnull")
        self.getInorder(root.left,res)
        res.append(str(root.val))
        self.getInorder(root.right,res)
        
        return res
        