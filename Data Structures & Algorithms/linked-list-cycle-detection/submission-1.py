# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        idx = -1
        #Create for values visited
        visited = set()
        #Set current pointer to head
        curr = head
        #While loop
        while curr:
            if curr.next:
                if curr.next.val in visited:
                    idx = curr.next.val
                    break
                else:
                    visited.add(curr.next.val)
            curr = curr.next

        return idx != -1