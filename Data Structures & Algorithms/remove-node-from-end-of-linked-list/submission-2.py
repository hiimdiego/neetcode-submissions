# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Create dummy, fast, and slow pointers
        dummy = ListNode(0, head)
        left = right = dummy
        #Increment right pointer to where you want to remove the node
        while n >= 0:
            right = right.next
            n -= 1
        #Increment left pointer to just before where you want to remove the node
        while right:
            left = left.next
            right = right.next
        #remove node
        left.next = left.next.next
        #return where dummy node points to 
        return dummy.next