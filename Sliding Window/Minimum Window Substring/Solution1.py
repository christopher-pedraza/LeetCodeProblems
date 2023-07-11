# Neetcode.io solution

# Time complexity: O(n) - iterate once over the string s
#                         and each time do at most 2
#                         O(1) operations (add/remove
#                         from frequency HMap and update
#                         have/need values
# Space complexity: O(n)

def minWindow(s, t):
    # Edge case: if the substring we are looking for
    # is empty, return empty string
    if t == "":
        return ""

    # Frequency of the chars in string t
    countT = {}
    # Frequency of the chars we are looking from string t
    # in the window in string s
    countWindow = {}
    # Res contains the left and right pointers of the
    # substring in s that contains the needed chars
    # and resLen is the length of that substring
    # resLen could also be calculated with `r-l+1`
    # resLen starts with infinity because any len
    # would be smaller than infinity
    res, resLen = [-1, -1], float("infinity")
    # Left pointer
    l = 0

    # Get the frequency of each char in t
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    # `have` is how many conditions have been made, and
    # `need` is how many are needed. For conditions I
    # mean how many characters have met the required 
    # frequency
    have, need = 0, len(countT)

    # Iterate the right pointer through the string s
    # as well as get the current char
    for r, c in enumerate(s):
        # Add 1 to the frequency of the current char
        countWindow[c] = 1 + countWindow.get(c, 0)

        # If the char is in countT (is a required char
        # in the substring) and the count is the same
        # as the needed in countT (thus, the condition
        # has just been satisfied), add 1 to `have`
        # If you add anymore to the count of the char,
        # it won't update `have`, it only updates the
        # first time the condition is met, or when the
        # condition stops being met) 
        if c in countT and countWindow[c] == countT[c]:
            have += 1

        # While we have met the condition. In this case
        # we have to keep updating the answer if it's
        # smaller than the previous answer. Meanwhile,
        # while the condition is still met, we will move
        # as much as we can the left pointer to reduce
        # the size of the substring, while meeting the
        # required frequency
        while have == need:
            # If it's a new minimum result, we update it
            if (r - l + 1) < resLen:
                # Update the pointers of the substring
                # as well as the new length
                res = [l, r]
                resLen = r - l + 1
            
            # As we are trying to reduce the window to get the
            # minimum possible while meeting the conditions,
            # and in order to reduce it we move the left pointer
            # once to the right, we are going to reduce 1 to the
            # count of the char in the left index
            countWindow[s[l]] -= 1
            # Once you remove one from the count, you check if the
            # char that was removed is in countT (meaning, if it's
            # one of the characters that are required. If it's not
            # required, we don't care if we have a lot of it, or
            # none) and also if the new count of the char is less 
            # than the required count described by countT. If it is
            # less, we have to update `have` reducing its value by
            # one as one of the conditions that was needed is no
            # longer met.
            if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                have -= 1
            # After that, move the left pointer to the right once
            l += 1

    # As `res` is a list with 2 values: the left and right pointer
    # we can unpack it into two int variables.
    # Notice that if the conditions were never met while going
    # through s, res will still be [-1, -1]. However this is not
    # a proble thanks to the condition in the return
    l, r = res

    # Returns the spliced string from the left pointer from res
    # up to the right pointer + 1, if `resLen` isn't still the
    # default value. If it's the default value, it means the 
    # required conditions were never met and we return an empty
    # string
    return s[l:r+1] if resLen != float("infinity") else ""

print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("a", "a")) # "a"
print(minWindow("a", "aa")) # ""