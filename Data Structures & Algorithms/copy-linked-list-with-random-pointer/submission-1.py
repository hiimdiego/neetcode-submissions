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
        #Create map of old nodes to new nodes
        oldToCurr = {None : None}
        #Iterate through linked list and map nodes
        curr = head
        while curr:
            newNode = Node(curr.val)
            oldToCurr[curr] = newNode
            curr = curr.next
        #Iterate through linked list again and copy next and random pointers
        curr = head
        while curr:
            copy = oldToCurr[curr]
            copy.next = oldToCurr[curr.next]
            copy.random = oldToCurr[curr.random]
            curr = curr.next

        return oldToCurr[head]
        