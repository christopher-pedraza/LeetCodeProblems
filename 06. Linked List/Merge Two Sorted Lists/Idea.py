# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        # While at least one of the lists are not empty
        while list1 or list2:
            # If only list1 is empty
            if not list1:
                # If it's the first node of resulting list, add
                # to head the node
                if not head:
                    head = list2
                # If it isn't the first node
                else:
                    head.next = list2
                    head = head.next
                # Remove the first node of list2
                list2 = list2.next
            # If only list2 is empty
            elif not list2:
                # If it's the first node of resulting list, add
                # to head the node
                if not head:
                    head = list1
                # If it isn't the first node
                else:
                    head.next = list1
                    head = head.next
                # Remove the first node of list1
                list1 = list1.next
            # If none of the lists are empy
            else:
                # If the head value of list1 is less than the head
                # value of list2, add to the resulting list the
                # node of list1
                if list1.val < list2.val:
                    # If it's the first node of resulting list, add
                    # to head the node
                    if not head:
                        head = list1
                    # If it isn't the first node
                    else:
                        head.next = list1
                        head = head.next
                    # Remove the first node of list1
                    list1 = list1.next
                # If the head value of list2 is greater or equals than
                # the head value of list1, add to the resulting list the
                # node of list2
                else:
                    # If it's the first node of resulting list, add
                    # to head the node
                    if not head:
                        head = list2
                    # If it isn't the first node
                    else:
                        head.next = list2
                        head = head.next
                    # Remove the first node of list1
                    list2 = list2.next
        return head