#LeetCode problem 167: Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            d[numbers[i]]=i
        for j in range(len(numbers)):
            if((target-numbers[j])) in d and d[target-numbers[j]]!=j:
                return[j+1,d[target-numbers[j]]+1]