# Neetcode.io solution

# The brute force solution would be to have a list and each
# time we add a new number, we go through the list checking
# where should we insert the number, and if it's before other
# numbers, we move the next numbers 1 position so we can insert
# it. This operation of adding a number will be in the worst
# case O(n) as we would have to move all the numbers in the
# list every time if we always insert smaller numbers. The
# operation of calculating the median will just be O(1) as we
# just have to access the middle element(s).

# A better solution would be to use 2 heaps/priority queues
# We will have a small heap and a big heap. The small heap
# will have only numbers that are smaller or equals to all
# the numbers in the big heap. These two heaps should be
# approximately balanced in terms of size. They can only have
# a difference of 1 element (for example, one with 3 and the
# other with 2). If the difference increases, we have to balance
# them again. Inserting into a heap always has a time complexity
# of O(logn), the same goes to removing an element.
# The small heap will be a maxHeap, and the big heap will be
# a min heap. This way, we can access the max element in the
# small heap in O(1), and the min element in the big heap in
# also O(1). However, it's important to consider that heap
# operations (removing and adding) are O(logn). The reason of
# this arrangement is because when we calculate the median, we
# want the max from the smaller heap and the min from the
# bigger heap:
# [1, 2, 3] <= [4, 5, 6]
#   max -^      ^- min
# The median would need the 3 and the 4
# If the size of the heaps is different (by 1), we know we have
# an odd number of elements, thus we just take the element from
# the heap that has the extra element:
# [1, 2, 3] [3, 5]
#        ^- median

# Procedure when adding numbers (from the video, the solution
# in the website is slightly more optimized):
# Each time we add or remove, the time complexity is O(logn)
# as that's the cost of the heap operations. Just consulting
# the min value of the min heap or max value of the max heap
# is O(1)
# 1. Add the numbers first in the small heap (doesn't matter to
# which one we add them, but we will use the min)
# 2. If the size of the heaps differs by more than 1, we get
# the max from the small heap (which is a maxHeap) and add it
# to the big heap, or the min from the big heap (which is the
# minHeap) adn add it to the small heap.
# 3. If the min element of the big heap is smaller than the
# max element in the small heap we get the max from the small 
# heap and add it to the big heap
# 4. Repeat steps 2 and 3 until we have both heaps of roughly
# the same size and with the smaller elements in the small heap
# and the greater elements in the big heap.

# Procedure when calculating the median:
# The time complexity will be O(1) as we will only need to 
# consult the min number of the min heap (The heap with the
# bigger numbers) and the max number from the max heap (the
# heap with the smallest numbers), sum them and divide them by
# 2 (in case the quantity of numbers is even, if not, just get
# 1 number from the heap that has the extra element)
# 1. Check if the size of both heaps is the same
# 1.1 If YES, get the min from the heap of bigger numbers and
#     max from the heap of smaller numbers, sum them and divide
#     them by 2
# 1.2 If NOT, get the min/max from the heap that has the extra
#     element

# Follow up:
# 1) If all integer numbers from the stream are in the range
#    [0, 100], how would you optimize your solution?
# 2) If 99% of all integer numbers from the stream are in the
#    range [0, 100], how would you optimize your solution?
# Ans:
# 1) Maybe initialise an array of size 100, where the key is
#    the number and the value is the frequency. You can then
#    get the answer in constant time by iterating through
#    until you reach the halfway point.
# 2) If 99% of the numbers are in the range you could do the
#    same thing but have two extra variables for "over 100"
#    and "under 100" and this would work as long as the median
#    number was in the range 0-100

class MedianFinder:
    def __init__(self):
        # two heaps: large (minheap), small (maxheap)
        # Heaps should be roughly the same size
        # maxHeap, minHeap (python default)
        self.small, self.large = [], []  

    # Time complexity: O(2logn) -> O(logn)
    # This is because the lookup in the heaps is O(1), but
    # in the worst case, we will have to remove a number from
    # one of the heaps O(logn) and add it to the other one
    # O(logn)
    def addNum(self, num: int) -> None:
        # If there's elements in the large heap and
        # the number is bigger than the first element
        # in it, it means it will be bigger than any
        # other number in the small heap, thus, we add
        # it to the big heap
        if self.large and num > self.large[0]:
            # Add to the large heap the number
            heapq.heappush(self.large, num)
        # But if large doesn't have anything or the number is
        # smaller than the smallest number in the large heap
        # (as it's a minHeap), we add it to the small heap
        else:
            # Python only implements min heaps, thus it
            # prioritizes smaller numbers. As the small heap
            # need to be a maxHeap, we can multiply the value
            # by -1 so the bigger values will now be the
            # smallest ones
            heapq.heappush(self.small, -1 * num)

        # If the small heap has more than 1 element more than
        # the large heap, we need to move the biggest element
        # in the small heap to the large heap to keep them
        # balanced
        if len(self.small) > len(self.large) + 1:
            # As when we added the number to the maxHeap we
            # multiplied it by -1 to make it a maxHeap, we
            # multiply it once again to reverse it to the 
            # original value. We are taking out the extra
            # number that the small heap has to move it to
            # the large heap
            val = -1 * heapq.heappop(self.small)
            # Add to the large heap the biggest number we took
            # from the small heap
            heapq.heappush(self.large, val)
        # If the large heap has more than 1 element more than
        # the small heap, we need to move the smallest element
        # in the large heap to the small heap to keep them
        # balanced
        if len(self.large) > len(self.small) + 1:
            # Take from the minHeap of the large heap the
            # smallest value to move it to the small heap
            val = heapq.heappop(self.large)
            # Add to the small heap the value (remembering to
            # multiply it by -1 so it works as a maxHeap)
            heapq.heappush(self.small, -1 * val)
        
    # Time complexity: O(1)
    # Because the lookup in a heap is done in constant time
    def findMedian(self) -> float:
        # If we have an odd quantity of numbers and the small
        # heap has the extra element
        if len(self.small) > len(self.large):
            # Take the biggest number from the small heap
            # (as it is a maxHeap). Remember that as by default
            # the heaps are minHeaps, we need to revert the
            # value by multiplying by -1
            return -1 * self.small[0]
        # If we have an odd quantity of numbers and the large
        # heap has the extra element
        elif len(self.large) > len(self.small):
            # Take the smallest number from the large heap
            # (as it is a minHeap).
            return self.large[0]
        # If both heaps have the same quantity of numbers, we
        # take the biggest number from the small heap (maxHeap)
        # and the smallest number from the large heap (minHeap)
        # add them together, and divide them by 2. Remember
        # that we need to rever the the value of the small
        # heap. Also, divide by a float number so we can get
        # a float value (I don't know if this is necessary) 
        return (-1 * self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()