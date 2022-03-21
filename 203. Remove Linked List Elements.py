# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        cur = head
        prv = None
        while(cur != None):            
            if head.val == val:
                head = head.next
                cur= head
            elif cur.val == val:
                prv.next = cur.next
                cur = cur.next                
            else:
                prv = cur
                cur = cur.next           
        return head