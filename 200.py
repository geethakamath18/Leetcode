#LeetCode problem 200: Number of Islands
class Solution:
    def check(self,grid,nodesVisited,row,col,m,n):
        return (row>=0 and row<m and col>=0 and col<n and grid[row][col]=="1" and nodesVisited[row][col]==0)
    
    def dfs(self,grid,nodesVisited,row,col,m,n):
        a=[-1,1,0,0]
        b=[0,0,1,-1]
        nodesVisited[row][col]=1
        for k in range(4):
            if self.check(grid,nodesVisited,row+a[k],col+b[k],m,n):
                self.dfs(grid,nodesVisited,row+a[k],col+b[k],m,n)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        nodesVisited=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0":
                    continue
                elif grid[i][j]=="1" and nodesVisited[i][j]==0:
                    count+=1
                    self.dfs(grid,nodesVisited,i,j,len(grid),len(grid[0])) 
        return count