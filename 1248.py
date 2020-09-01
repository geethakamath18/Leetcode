#LeetCode problem 1248: Count Number of Nice Subarrays
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(k, nums) - self.atMost(k-1, nums)
    
    def atMost(self, k: int, nums: List[int]):
        res = i = 0
        for j in range(len(nums)):
            k -= nums[j] % 2
            while k < 0:
                k += nums[i] % 2
                i += 1
            res += j - i + 1
        return res   
                
        