

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # helper function to get kth node
        def get_kth_node(node):
            for _ in range(k):
                if not node:
                    return None 
                node = node.next 
            return node
        
        dummy = ListNode(0, head)
        group_prev = dummy 

        while True:
            kth = get_kth_node(group_prev)
            if not kth:
                break 
            group_next = kth.next 

            # reverse the group 
            prev, cur = group_next, group_prev.next 
            while cur != group_next:
                nxt = cur.next 
                cur.next = prev 
                prev = cur 
                cur = nxt 
            # reconnect to next group 
            tmp = group_prev.next 
            group_prev.next = kth 
            group_prev = tmp 
        return dummy.next 
        


        