# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Will store the first node after reversing the list (the previous
        # last node)
        self.firstNode = None

        # Auxiliary function to to reverse the list
        def reverseAux(node):
            # If the next node is None, it means we have reached the end
            # of the list
            if not node.next:
                # We set this node as the firstNode (as it was previously
                # the last node but will now be the head of the list)
                self.firstNode = node
                # Return the node so we can start reversing it
                return node
            # If the current node is NOT the last one in the list
            else:
                # Call the recursive function passing the next node
                # after the recursive call returns with the next node
                # we set the next of that node to the current node.
                # This way we can get all the way to the last node, and
                # then start setting up the `next` node from the last
                # node up to the first
                reverseAux(node.next).next = node
                # Set the next value of the current node to None. If
                # the current node is not the last one (or previously
                # the first one, this `next` value will get replaced
                # in the previous recursive call, however, if it's
                # the last one, then it will remain as None as there
                # shouldn't be any more nodes after it)
                node.next = None
                # Return the current node so we can reverse in the
                # previous recursive call its `next` value
                return node

        # If the head is not None, meaning the list is not empty, start
        # the recursive calls passing the head as the first node.
        # However, if it's None, we won't call the function and just
        # return None as it's the default value of firstNode at it will
        # never change
        if head:
            reverseAux(head)

        # Return the previously last node which is now the head
        return(self.firstNode)