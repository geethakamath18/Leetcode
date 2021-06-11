#LeetCode problem 53: Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = current_sum = nums[0]
        for i in nums[1:]:
            current_sum = max(i, current_sum+i)
            print(current_sum)
            m = max(m, current_sum)     
        return m