// LeetCode problem 1480: Running Sum of 1d Array

class Solution {
    public int[] runningSum(int[] nums) {
        int[] total = new int[nums.length];
        for(int i=0;i<total.length;i++){
            total[i]=0;
        }
        total[0]=nums[0];
        for(int i=1;i<nums.length;i++){
            total[i]= total[i-1]+nums[i];
        }
        return total;
    }
}