#LeetCode problem 94: Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a=[]
        self.returnOrder(root,a)
        return a
    
    def returnOrder(self, root: TreeNode, a:List):       
        if root is None:
            return
        if root:
            self.returnOrder(root.left,a)
            a.append(root.val)
            self.returnOrder(root.right,a)