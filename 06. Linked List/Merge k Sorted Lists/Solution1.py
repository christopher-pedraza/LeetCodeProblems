# Neetcode.io solution

# Time complexity: O(nlogk) where n is the size of the list and k the
#                           quantity of lists
# Space complexity: O(1) no extra memory needed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    	# Handle edge cases in which the list is null or empty
        if not lists or len(lists) == 0:
        	# Return empty linked list
            return None

        # Take pairs of linked lists and merge them until we have only
        # 1 linked list remaining, which is our output
        while len(lists) > 1:
        	# Merged lists will be stored here
            mergedLists = []
            # Iterate over the lists in pairs, that's why the increment
            # is 2
            for i in range(0, len(lists), 2):
            	# Get the two lists
                l1 = lists[i]
                # If we have an odd number of lists, and are incrementing
                # by 2, the next list could be None. We check if i+1 is
                # out of bounds, if it is, we set it as None, which can
                # still be merged as an empty list
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the two lists and add it to the list of merged
                # lists
                mergedLists.append(self.mergeList(l1, l2))

            # Update list variable with the merged lists
            lists = mergedLists

        # When we only have 1 list left, we can return the head
        return lists[0]

    # Merge 2 linked lists
    def mergeList(self, list1, list2):
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
        # If both lists are empty, this will return None (empty list)
        # as that is the default value for the next in a node
        return dummy.next