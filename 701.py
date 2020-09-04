#LeetCode problem 701: Insert into a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root=TreeNode(val)
        if val<root.val and root.left is None:
            root.left=TreeNode(val)
            return root
        elif val>root.val and root.right is None:
            root.right=TreeNode(val)
            return root
        elif val<root.val:
            self.insertIntoBST(root.left,val)
        elif val>root.val:
            self.insertIntoBST(root.right,val)
        return root