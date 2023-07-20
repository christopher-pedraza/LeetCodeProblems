# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(n)

def checkInclusion(s1: str, s2: str) -> bool:
    # If s1 is longer than s2, then it's impossible to
    # get a permutation of s1 in s2, so we return false
    if len(s1) > len(s2):
        return False

    # Lists storing the frequency of the letters, in which 
    # index of the list refers to the letter as an int
    # For each char in s1, we are adding 1 to the frequency
    # of it in the lists. This can also be done using 
    # hashmaps 
    s1Count, s2Count = [0] * 26, [0] * 26
    # s1 should be smaller than s2, so this helps initialize
    # the beginning window of s2 at the same time as we get
    # the needed frequency of the characters in s1
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    # This helps use to reduce the need to compare the whole
    # hash map everytime, which in the worst case would be
    # 26 comparisons (26 letters in the alphabet). Basically
    # for each letter we check if the quantity matches in
    # both hashmaps. If so, we add 1 to `matches`, which can
    # go from 0 (no letters match the quantity) up to 26 (all
    # letters in the window match). I'm talking about hashmaps
    # because I'm linking each letter with the frequency, but
    # in this case we are using a list, in which the index is
    # the value of the letter as an int. 
    matches = 0
    # We know there are only going to be 26 chars in the array
    for i in range(26):
        # If the count is the same (either you have the same
        # quantity of the letters or also, in both strings you
        # don't have a letter so you have a 0), we add 1 to
        # matches, otherwise, we add 0
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    # Left pointer at the begginning
    l = 0
    # Right pointer will iterate over all positions. It starts
    # from the length of s1 as we already added the frequency in
    # that chars, and up to the length of s2 where we are
    # looking for the permutation of s1
    for r in range(len(s1), len(s2)):
        # If `matches` is already 26, it means all letters in the
        # window match with the needed letters in s1
        if matches == 26:
            return True

        # This can be made easier using a hashmap in which the
        # character is the key. However, as we are using an array
        # we are getting the int value of the char, and substracting
        # the int value of a so they are normalized to 0
        index = ord(s2[r]) - ord("a")
        # Add 1 to the frequency of the character in the r pointer
        s2Count[index] += 1

        # If after incrementing the count of the letter it's exactly
        # the quantity we needed, we add to `matches` 1 
        if s1Count[index] == s2Count[index]:
            matches += 1
        # However, we could also have made it too large, in this case,
        # matches decreases as it's above the needed quantity, thus
        # it no longer matches. If this is the case (that we made it
        # exactly 1 more than the exact quantity that was needed) we
        # decrease matches as it previously match the quantity, but not
        # anymore
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # We now do the opposite for the left pointer
        # We get the index of the character in the left pointer
        index = ord(s2[l]) - ord("a")
        # Substract 1 to the count of it as we are moving the pointer
        # once to the right
        s2Count[index] -= 1
        # If with the movement the counts match, we add 1 to matches
        if s1Count[index] == s2Count[index]:
            matches += 1
        # If now we are exactly 1 short, it means it previously matched,
        # so we remove 1 from matches
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        # And we move the left pointer once to the right
        l += 1
    # If matches equals 26, it either means it never enter the loop
    # or we got the correct match count at the last iteration. Either
    # way, it means we're able to find a permutation of s1 in s2
    return matches == 26

print(checkInclusion("ab", "eidbaooo")) # True
print(checkInclusion("ab", "eidboaoo")) # False
print(checkInclusion("adc", "dcda")) # True