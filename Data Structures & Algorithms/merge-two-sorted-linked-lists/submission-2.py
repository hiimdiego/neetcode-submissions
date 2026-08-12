# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Initialize output and head pointers
        temp = node = ListNode()
        #Traverse both lists at the same time
        while list1 and list2:
            #Check if value of first list is less than second list
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            #Increment node pointer
            node = node.next
        #Set value of next node to whichever list is non empty
        node.next = list1 or list2
        #Return temp next pointer
        return temp.next