# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        #Traverse list 1
        while l1:
            #Convert values to strings and append them to num1 and num2
            num1 = str(l1.val) + num1
            l1 = l1.next
        #Traverse list 2
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        #Convert strings back to int and sum together
        num1 = int(num1)
        num2 = int(num2)
        total = num1 + num2
        #Convert sum back into string and traverse backwards
        total = str(total)
        tmp = curr = ListNode()
        for char in reversed(total):
            curr.next = ListNode(int(char))
            curr = curr.next
        return tmp.next

