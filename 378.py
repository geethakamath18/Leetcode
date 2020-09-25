#LeetCode problem 378: Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
        return(sorted(res)[k-1])