"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Create a map from old to new nodes
        oldToCopy = {None:None}
        curr = head
        #Traverse list and map old to new
        while curr: 
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        #Traverse list again and adjust next and random pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]