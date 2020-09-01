#LeetCode problem 590: N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        a=[]
        self.returnOrder(root,a)
        return a
    
    def returnOrder(self, root: 'Node',l):
        if root is None:
            return 
        if root.children is not None:
            for child in root.children:
                self.returnOrder(child,l)
        l.append(root.val)