def characterReplacement(s, k):
    l, r = 0, 0
    firstDiff = 0
    res = 0
    diffCounter = 0

    while r < len(s):
        if s[l] == s[r] and r == len(s)-1 and diffCounter <= k:
            res = max(res, r - l + 1)
        elif r == len(s)-1 and diffCounter < k:
            res = max(res, r - l + 1)
        # If the current char is the same
        # as the char in the left, just
        # move the right pointer once
        elif s[l] == s[r] and diffCounter <= k:
            r += 1
            continue
        # If the chars are not the same
        else:
            # Increase the count of differences
            diffCounter += 1 

            # If it's the first difference found
            if firstDiff == 0:
                firstDiff = r

            # Check if diffcounter is greater
            # than k
            if diffCounter > k:
                res = max(res, r - l)
                diffCounter = 0
                l = firstDiff
                r = l
                firstDiff = 0
        r += 1
        
    return res

print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABABBA", 1)) # 4

# PRODUCES WRONG ANSWER
# It returns 3, while it should have replaced the
# A with a B and return 4
print(characterReplacement("ABBB", 2)) 