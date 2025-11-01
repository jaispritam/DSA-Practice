from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list using a min-heap (priority queue).

        Args:
        lists (List[Optional[ListNode]]): A list of k linked lists.

        Returns:
        Optional[ListNode]: The head of the merged sorted linked list.
        """

        # Step 1: Initialize a min-heap
        heap = []

        # Push the head of each non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                # We push a tuple: (node value, list index, node)
                # list index ensures the tuple is unique if values are the same
                heapq.heappush(heap, (node.val, i, node))

        # Step 2: Initialize a dummy node to build the result list
        dummy = ListNode(0)
        tail = dummy  # tail points to the last node in the merged list

        # Step 3: Process the heap until it's empty
        while heap:
            # Pop the smallest value node from the heap
            val, i, node = heapq.heappop(heap)
            # Append this node to the merged list
            tail.next = node
            tail = tail.next

            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Step 4: Return the merged linked list (skipping dummy)
        return dummy.next
