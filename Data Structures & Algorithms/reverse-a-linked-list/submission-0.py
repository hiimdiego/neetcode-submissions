# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Assign head and previous pointers of linked list
        prev, curr = None, head
        #Traverse linked list
        while curr:
            #Create temp
            temp = curr.next
            #Reassign current next node
            curr.next = prev
            #Reassign previous node
            prev = curr
            #Update current node
            curr = temp
        return prev