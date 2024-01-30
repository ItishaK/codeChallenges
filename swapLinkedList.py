from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        if self.head is None:
            self.head = new_node
            print('self.head: ',self.head)
        else:
            last = self.head
            while(last.next):
                last = last.next
            print('last element: ',last)

        last.next = new_node

        self.swapPairs([1, 2, 3, 4])
