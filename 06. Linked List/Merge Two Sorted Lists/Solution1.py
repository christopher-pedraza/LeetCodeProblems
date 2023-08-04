# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # This dummy helps remove the edge case of inserting into an empty
        # list
        dummy = ListNode()
        # Tail is the last element of the list, in the first instance, it
        # will be the dummy 
        tail = dummy

        # If both of them are not empty
        while list1 and list2:
            # If the value of list 1 is less than the value of list 2
            if list1.val < list2.val:
                # Insert into our tail the value of the list 1
                tail.next = list1
                # Update the list 1 pointer
                list1 = list1.next
            # If list 2 is less than or equals than the value in list 1
            else:
            	# Insert into our tail the value of the list 2
                tail.next = list2
                # Update the list 2 pointer
                list2 = list2.next
            # Update the tail pointer
            tail = tail.next

        # If only list 1 is not empty
        if list1:
        	# Insert into tail the remaining portion of list 1
            tail.next = list1
        # If only list 2 is not empty
        elif list2:
        	# Insert into tail the remaining portion of list 2
            tail.next = list2

        # Return the list after the dummy to not include it
        return dummy.next