#LeetCode problem 414: Third Maximum Number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)>=3:
            return sorted(nums)[::-1][2]
        return sorted(nums)[::-1][0]