# Neetcode.io solution

# The explanation was really confusing, so it may be better if you
# rewatch the solution: https://youtu.be/q6IEA26hvXc

# Time complexity: O(log(min(n, m))) - running binary search on the smallest
#                                   of the two lists
# Space complexity: O(1)

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # We are assigning the lists into other variables so it's easier
    # to refer to them. A is going to be the list with the least length
    # If it isn't, we are going to swap them later on 
    A, B = nums1, nums2
    # Total length of all the numbers combined
    total = len(nums1) + len(nums2)
    # Half the length
    half = total // 2

    # If B is smaller than A, we swap A and B
    if len(B) < len(A):
        A, B = B, A

    # Left and right pointers. We are going to do binary search
    # on the smallest array and get the rest of the left numbers
    # from other array. In order to know how many more numbers we
    # need from the other array, we substract the quantity of
    # numbers from A from `half`
    l, r = 0, len(A) - 1

    # There's a guaranteed median, so we can just iterate until
    # we find the solution and return it
    while True:
        # Middle index in array A
        i = (l + r) // 2  # A
        # Index of the mid point in array B
        # We substract half which is the total quantity of numbers
        # from both arrays divided by 2. We then substract the size
        # of the window of A (as it is 0 based, and i is the index,
        # we add 1) and -1 (as it is 0 based and this should be the
        # index for B)
        j = half - (i+1) - 1  # B

        # Left of the partition A
        # If i is out of bounds (negative, meaning it has gone too
        # far to the left), we set -inf to Aleft
        Aleft = A[i] if i >= 0 else float("-infinity")
        # Right of the partition A
        # If i is out of bounds (more than the length-1 [remember
        # it's a 0-based index], meaning it has gone too far to the
        # right), we set +inf to Aright
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        # Left of the partition B
        # If j is out of bounds (negative, meaning it has gone too
        # far to the left), we set -inf to Bleft
        Bleft = B[j] if j >= 0 else float("-infinity")
        # Right of the partition B
        # If j is out of bounds (more than the length-1 [remember
        # it's a 0-based index], meaning it has gone too far to the
        # right), we set +inf to Bright
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # Partition is correct
        # We cross-check that the last (right) value from the right
        # partition of A is less than or equals the first (left) value
        # from the right partition of B. Also that the last (right)
        # value from the right partition of B is less than or equals to
        # the first (left) value in the right partion of A
        if Aleft <= Bright and Bleft <= Aright:
            # If it's odd, the mod2 of total would yield a positive
            # result, if it's even, it would result in 0
            if total % 2:
                # Return the least value from the right partitions of
                # A and B
                return min(Aright, Bright)
            # If it's even we get the greater value from the left
            # partitions and the least values from the right partitions
            # and get the mean from them
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        # If we don't find the median, it's possible that we have too
        # many numbers from A, so we reduce the size of the window by
        # shifting the right pointer and reducing the size of that
        # partition
        elif Aleft > Bright:
            r = i - 1
        # We need to incresease the size of the left partition of A
        else:
            l = i + 1

print(findMedianSortedArrays([1,3], [2])) # 2.00000
print(findMedianSortedArrays([1, 2], [3, 4])) # 2.50000
print(findMedianSortedArrays([], [1, 2, 3])) # 2.00000
print(findMedianSortedArrays([1, 2, 3], [])) # 2.00000
print(findMedianSortedArrays([10], [1, 2, 3, 4, 5, 6, 7, 8, 9])) # 5.50000
print(findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [10])) # 5.50000
print(findMedianSortedArrays([], [])) # 0.00000