#LeetCode problem 1443: Minimum Time to Collect All Apples in a Tree
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Creating adjacency list
        aList=[[] for i in range(n)]
        for i,j in edges:
            aList[i]. append(j)
            aList[j]. append(i)
        nodesVisited=set()
        return max(self.dfs(nodesVisited,aList, hasApple,0) - 2, 0)
    
    def dfs(self,nodesVisited,aList,hasApple,node):
        if node in nodesVisited:
            return 0
        nodesVisited.add(node)
        time=0
        for child in aList[node]:
            time+=self.dfs(nodesVisited, aList, hasApple, child)
        if time > 0:
            return time + 2
        return 2 if hasApple[node] else 0
        