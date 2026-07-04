# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        length = 0
        while curr: 
            length += 1
            curr = curr.next 
        
        if (length - n) == 0: 
            return head.next 
        stop = (length - n) - 1
        curr_new = head
        index = 0 
        
        while curr_new and curr_new.next: 
            if index == stop: 
                curr_new.next = curr_new.next.next 
                break
            else: 
                index += 1
                curr_new = curr_new.next 
        
        return head

            



