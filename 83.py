#LeetCode problem 83: Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev=None
        curr=head
        a=[]
        while(curr is not None):
            if(curr.val in a):
                curr=curr.next
                prev.next=curr
            else:  
                a.append(curr.val)
                prev=curr
                curr=curr.next
        return head