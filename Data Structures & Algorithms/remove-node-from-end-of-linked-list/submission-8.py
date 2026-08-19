# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Find length of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        #Find index of node to remove (0-indexed)
        node_idx = length - n

        #Check if node is the head of the list
        if node_idx == 0:
            head = head.next
            return head

        #Find and remove node
        curr = head
        prev = None
        idx = 0
        while curr:
            if idx == node_idx:
                prev.next = curr.next
                curr.next = None
                break
            prev = curr
            curr = curr.next
            idx += 1
        return head