# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize pointers
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #Find position of node to remove by subtracting from n
        while n > 0:
            right = right.next
            n -= 1
        
        #Shift pointers to where left is just before node to remove
        while right:
            left = left.next
            right = right.next
        
        #Remove node and return head
        left.next = left.next.next
        return dummy.next
        