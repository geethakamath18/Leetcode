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


# class Solution:
#     def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:


#         def dfs(node, depth):  
#             # monitor which sub tree has a deeper path
#             # if both has the same depth (balanced), return the current node
#             # otherwise, abandon the shorter sub-tree, and return the recursive result of the other
#             if not node:
#                 return depth, node

#             depth += 1

#             left_depth, left_root = dfs(node.left, depth)
#             right_depth, right_root = dfs(node.right, depth)

#             if left_depth == right_depth:
#                 return left_depth, node
#             if left_depth > right_depth:
#                 return left_depth, left_root
#             else:
#                 return right_depth, right_root

#         # return both depth and the root

#         depth, node = dfs(root, 0)

#         return node 
