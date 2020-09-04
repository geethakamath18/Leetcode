#LeetCode problem 559: Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        m=1
        for child in root.children: 
            m=max(self.maxDepth(child)+1,m)
        return m