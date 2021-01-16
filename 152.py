#LeetCode problem 152: Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maximum = nums[0]
        minimum = nums[0]
        result = maximum
        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, maximum * curr, minimum * curr)
            minimum = min(curr, maximum * curr, minimum * curr)
            maximum = temp
            result = max(maximum, result)
        return result
            