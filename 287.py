#LeetCode problem 287: Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                return i
        