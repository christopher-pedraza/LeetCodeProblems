# Time complexity: O(n*m)? - iterate once over the
#                            string t of length n
#                            and once over the string
#                            s of length m. However
#                            also iterate each time
#                            over the dict of length
#                            n for each cycle of s
# Space complexity: O(n*m)? - dicts with chars from
#                             the strings s and t

def minWindow(s, t):
    # Dict that contains the length of a
    # substring that contains the required
    # chars as a key, and the starting index
    # as the value
    lengths = {} # len -> StartIndex
    # Left pointer
    l = 0
    # Dicts with the frequency of the chars in the
    # strings
    charsT = {}
    charsS = {}

    # Get the frequency of each char in t
    # Time complexity: O(n)
    for c in t:
        charsT[c] = 1 + charsT.get(c, 0)

    # Iterate over s, moving the right pointer
    # Time complexity: O(m)
    for r in range(len(s)):
        # Add 1 to the frequency of the current char
        charsS[s[r]] = 1 + charsS.get(s[r], 0)

        isComplete = True
        # If the substring contains the chars in T
        while isComplete:
            # Checks if the substring contains the required
            # frequency of each char in T
            # Time complexity: O(n)
            for item in charsT:
                isComplete = (isComplete and
                                item in charsS and
                                charsS.get(item) >= charsT.get(item))

            if isComplete:
                # Add the length of the substring as well as the
                # starting index to the dict
                lengths[r-l+1] = l
                # Remove 1 from the frequency of the char that will
                # no longer be included after moving the left pointer
                # to the right once
                charsS[s[l]] -= 1
                # Move left pointer
                l += 1

    # If nothing was added to lengths, it means no substring of s
    # contains the chars of t in the same frequency. Thus, we return
    # an empty string
    if not lengths:
        return ""
    # However, if lengths is not empty
    else:
        # Get the minimum length of a substring from the dict
        minLen = min(lengths)
        # And slice the string to get the substring
        return s[lengths[minLen]:lengths[minLen]+minLen]

print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("a", "a")) # "a"
print(minWindow("a", "aa")) # ""