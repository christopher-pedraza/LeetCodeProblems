# Time complexity: O(n)
# Space complexity: O(n)

# Add the nodes of the linked list into a set after checking if the
# node is not already in the set. If it is, we found a cycle, if it
# isn't, we continue adding the nodes to the set. If we find a
# `next` that returns None, it means we reached the end of the list
# and as we never found a cycle, we return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Store the nodes until we find a cycle
        # MC: O(n)
        hSet = set()
        # Used in the loop to take the next node in the list
        current_node = head

        # Iterate over the nodes in the list
        # TC: O(n)
        while current_node:
            # If the node isn't in the hash set, it hasn't return to a
            # previous node (cycle)
            # TC: O(1)
            if current_node not in hSet:
                # Add to the hashset the current node
                # TC: O(1)
                hSet.add(current_node)
                # Take the next node in the list
                current_node = current_node.next
            # If it's already in the hSet, we found a cycle
            else:
                return True

        # If we end the loop without finding a cycle
        return False