#LeetCode problem 688: Knight Probability in Chessboard
class Solution:      
        
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def helper(r, c, moves, p):
            if not ((0 <= r < N) and (0 <= c < N)): return 0                                          
            if moves == 0: return p                                                                     
            return sum(helper(i, j, moves-1, p/8) for i,j in ((r+2,c+1),(r+1,c+2),(r-1,c+2),(r-2,c+1), 
                                                              (r-2,c-1),(r-1,c-2),(r+1,c-2),(r+2,c-1)))
        return helper(r, c, K, 1)