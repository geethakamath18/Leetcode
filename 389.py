#LeetCode problem 389: Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return i
            elif i in s and s.count(i)<t.count(i):
                return i
            else:
                continue
                
            