#
#   DOESN'T WORK AS YOU COULD HAVE NEGATIVE NUMBERS AS ONE OF THE NUMBERS
#

# Time complexity: O(n)
# Space complexity: O(n)

def longestConsecutive(nums):
    # List to store each number as an index
    # In each index there will be a 0, except if the numbers exists
    vals = [0 for i in range((max(nums)+1 if nums else 0))]
    # Stores the longest consecutive sequence that has been found
    longestConsecutive = 0
    
    # For each num (which will be the index), set 1
    for n in nums:
        vals[n] = 1

    # Iterate over the new list
    currentCons = 0
    for i in range(len(vals)):
        # if it finds 1, add 1 to current
        if vals[i]==1:
            currentCons += 1
        # If it's a 0, get the max from the previous longest and the current
        else:
            longestConsecutive = max(longestConsecutive, currentCons)
            currentCons = 0

    # Get the longest again in case all numbers where consecutive (never arrived at the else)
    longestConsecutive = max(longestConsecutive, currentCons)
    return longestConsecutive

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([]))