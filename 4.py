#LeetCode problem 4: Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        s=[]
        if(len(nums1)==0):
            s=nums2
        elif(len(nums2)==0):
            s=nums1
        else:
            while(i<len(nums1) and j<len(nums2)):
                if(nums1[i]<nums2[j]):
                    s.append(nums1[i])
                    i+=1
                elif(nums1[i]>nums2[j]):
                    s.append(nums2[j])
                    j+=1
                else:
                    s.append(nums1[i])
                    i+=1
                    s.append(nums2[j])
                    j+=1
            if(i<len(nums1)):
                s=s+nums1[i:]
            elif(j<len(nums2)):
                s=s+nums2[j:]
        if(len(s)%2==0):
            mid=len(s)//2
            return float((s[mid]+s[mid-1])/2)
        else:
            mid=len(s)//2
            return float(s[mid])
         
                    
            
            