# Time complexity: O(n) - iterate once over the list storing the nodes in a
#                         list and then access the index in constant time
# Space complexity: O(n) - need a list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # List to store the nodes of the linked list
        lst = []
        # Stores the current node in the loop. Starts with the head
        current_node = head
        # Add the list nodes to a list so we can later on access from behind
        while current_node:
            # Append the nodes to the list
            lst.append(current_node)
            # Update the current node with the next node
            current_node = current_node.next

        # Else, we get the index of the previous node of the target by
        # converting it to negative and substracting 1
        prev_index = -1*(n)-1
        # And the target index by converting it to negative
        target_index = -1*(n)

        # If the target node is the head, we just replace the head with the
        # next node in the list (could be None)
        if lst[target_index] == head:
            head = head.next
        else:
            # Update the `next` node of the previous node from the target with
            # the `next` node from the target
            lst[prev_index].next = lst[target_index].next

        # Return the head of the list
        return head