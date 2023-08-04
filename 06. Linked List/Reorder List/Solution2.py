# Time complexity: O(n) - actually O(2n)
# Space complexity: O(n) - need a dequeue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Using a dequeue so we can pop from the right and the left
        lst = deque()
        # Nodes for when we start dequeing
        current_node = None

        # Takes the first node
        next_node = head

        # While the next node is not None (meaning we have reached the
        # end of the linked list)
        while next_node != None:
            # Append to the queue the node of the list
            lst.append(next_node)
            # Get the next node in the list (may be None if it's the end
            # of the list)
            next_node = next_node.next
            
        # Iterate over the queue taking the nodes from the left and right1
        while lst:
            # If it's the first node in the list, we update current node with
            # it
            if not current_node:
                current_node = lst.popleft()
            # If it's a node in the middle, we update the next node from the
            # current, by taking the left node in the queue, and updating the
            # current node with the popped node
            else:
                current_node.next = lst.popleft()
                current_node = current_node.next
            
            # Set the next node as None in case the loop ends here, meaning it
            # was the last node in the list
            current_node.next = None
            
            # If the list still has elements, we are now going to pop from the
            # right
            if lst:
                # Pop the right most node
                current_node.next = lst.pop()
                # Update the current node with the popped node
                current_node = current_node.next
                # Set the next node as None in case the loop ends here
                current_node.next = None