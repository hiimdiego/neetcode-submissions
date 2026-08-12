# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Traverse list to find length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        #Find index of node to remove (0-indexed)
        idx = length - n
        #Traverse list again and remove node
        i = 0
        curr = head
        prev = ListNode()
        output = None
        while curr:
            if i == idx:
                prev.next = curr.next
                curr.next = None
                if i == 0:
                    output = prev.next
                break
            if i == 0:
                output = curr
            prev = curr
            curr = curr.next
            i += 1
        return output