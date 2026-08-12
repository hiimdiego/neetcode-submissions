# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Initialize left and right pointers
        dummy = ListNode(0, head)
        left = right = dummy
        #Increment right pointer to where we want to remove node
        while n >= 0:
            right = right.next
            n -= 1
        #Increment left pointer to just before node to remove
        while right:
            left = left.next
            right = right.next
        #remove node and return
        left.next = left.next.next

        return dummy.next
        
        