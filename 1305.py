#LeetCode problem 1305: All Elements in Two Binary Search Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if root1 is None:
            tree2=self.returnInorder(root2) 
            return sorted(tree2)
        elif root2 is None:
            tree1=self.returnInorder(root1)
            return sorted(tree1)
        tree1=self.returnInorder(root1)
        tree2=self.returnInorder(root2) 
        return sorted(tree1+tree2)
    
    def returnInorder(self, root: TreeNode)->List[int]:
        res=[]
        current = root  
        stack=[]
        while True: 
            if current is not None: 
                stack.append(current) 
                current = current.left  
            elif(stack): 
                current = stack.pop() 
                res.append(current.val)
                current = current.right  
            else: 
                break
        return res