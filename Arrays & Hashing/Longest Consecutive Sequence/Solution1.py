# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(n)

def longestConsecutive(nums):
    numberSet = set(nums)
    maxLength = 0

    for n in numberSet:
        # Check if the current number is the start of a sequence
        # For it to be the start of a sequence, there shouldn't
        # be a left neighbor
        # To check for left neighbor, check if n-1 exists in set
        # If n-1 doesn't exist in number set, n is the start
        if (n-1) not in numberSet:
            currentLength = 1

            # Check if the sequence has other consecutive numbers
            # So from current number, I will iterate foward checking
            # if the numbers are in the set
            # If the next number is in the set increase count of
            # current sequence length
            while (n + currentLength) in numberSet:
                currentLength += 1

            # Get the max length from the current and previous max length
            maxLength = max(currentLength, maxLength)

    return maxLength


print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([]))
print(longestConsecutive([-1, -2, -3, -4]))