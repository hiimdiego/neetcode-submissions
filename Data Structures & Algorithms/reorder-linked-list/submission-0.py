# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Initialize slow and fast pointers
        slow = fast = head
        #Traverse list using slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Traverse list using slow pointer and reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        #Interweave both lists
        while second:
            temp, temp2 = first.next, second.next
            first.next = second
            second.next = temp
            first, second = temp, temp2

        