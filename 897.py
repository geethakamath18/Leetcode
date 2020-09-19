#LeetCode problem 897: Increasing Order Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        if root.left is None and root.right is None:
            return TreeNode(root.val)
        res=self.getPreOrder(root)
        a=newNode=TreeNode(res[0])
        for i in range(1,len(res)):
            newNode.right=TreeNode(res[i])
            newNode.left=None
            newNode=newNode.right
        return a
    
    def getPreOrder(self, root: TreeNode,res=[])->List[int]:
        if root is None:
            return
        self.getPreOrder(root.left,res)
        res.append(root.val)
        self.getPreOrder(root.right,res)
        return res