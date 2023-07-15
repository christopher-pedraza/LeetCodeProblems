# Neetcode.io solution

# Time complexity: O(n) - iterate through the string
#                         once. Difference with
#                         solution 2 is that you don't
#                         need to find the max freq if
#                         isn't bigger
# Space complexity: O(n)

def characterReplacement(s, k):
    count = {}
    l = 0
    maxf = 0

    # Iterate over the whole word moving the right
    # pointer
    for r in range(len(s)):
        # Add 1 to the count of each char
        count[s[r]] = 1 + count.get(s[r], 0)

        # We only update the max frequency if we find
        # a frequency that is greater than the previous
        # max. This is because we want to minimize the 
        # replacements needed, thus maximizing the 
        # amount of chars that are repeated (which is
        # described by maxFrequency). If the count of
        # a certain character decreases, and we would
        # have to decrease the maxFrequency, then it
        # means that the previous solution maximized
        # the chars better. Remember we want to maximize
        # the lenght of our window, and in order to do
        # it and still be less than or equal than k, we
        # need maxF to be as big as possible. We could
        # also check each time for the max frequency
        # inside the count dict, however, this would
        # make the time complexity as O(26*N), which is
        # still linear, but slower and is not needed
        # This is a O(1) operation as we are not scanning
        # any list
        maxf = max(maxf, count[s[r]])

        # If the lenght of the window minus the max
        # frequency of chars (max number of chars that
        # are the same) is greater than k, it means
        # we need to slide the window as it already
        # surpases the maximum replacements allowed
        # We do this operation because, consider this:
        # s="AABAB", k=1
        # window="AAB", len=3, maxF[A]=2
        #   3-2 = 1 is less than k
        # window="AABB", len=4, maxF[A]=2 / maxF[B]=2
        #   4-2 = 2 is NOT less than k
        if (r - l + 1) - maxf > k:
            # Decrease the count of the char in the left
            # pointer as it's going to move to the right
            # one position
            count[s[l]] -= 1
            l += 1

    # To get the size of the window we do:
    # AAABC
    # ^  ^
    # |  |
    # 0  3
    #
    # 3 - 0 + 1 = 4
    return (r - l + 1)

print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABABBA", 1)) # 4
print(characterReplacement("ABBB", 2)) # 4