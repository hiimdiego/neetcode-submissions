# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        idx = -1
        visited = set()
        curr = head
        while curr:
            if curr.next and curr.next.val in visited:
                idx = curr.next.val
                break
            visited.add(curr.val)
            curr = curr.next
        return idx != -1
        