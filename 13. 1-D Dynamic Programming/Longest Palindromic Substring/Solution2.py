# Time complexity: O(n^2) as for every center element we search all the
#                  other elements in the array (going from the center to the
#                  edges). If instead of storing the indexes of res_l and res_r
#                  we stored the substring as "res=s[l:r+1]", the time complexity
#                  would have been O(n^3) as slicing is done in O(n)
# Space complexity: O(1) as we are only storing the indexes and length

# This is a brute force solution where we check from every character the chars in
# the vecinity until they are no longer a valid palindrome. We store the starting
# and ending indexes, as well as the length of the palindrome so we can continue
# searching for the longest one. We do this twice for odd and even palindromes. For
# the even palindromes, the last iteration won't happen as when the function extend
# is called with a right index out of bounds it won't enter the while loop.
#
# An optimization, but that is harder to implement, is usign the Manacher algorithm
# With this algorithm, you could solve it in linear time.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Indixes of the answer so we only need to slice once at the end
        res_l, res_r = 0, 0
        res_len = 0

        # Time complexity: O(n^2)
        def extend(l, r, res_l, res_r, res_len):
            # While the two pointers are in bound and they are equal (they are
            # palindromes)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the size of the current palindrome (given by the difference
                # of the two pointers) is bigger than the size of the previous
                # palindrome, then we have found a bigger one
                if (r - l + 1) > res_len:
                    # Update the palindrome and size of it
                    res_l = l
                    res_r = r + 1
                    res_len = r - l + 1
                # Shift the pointers
                l -= 1
                r += 1

            return res_l, res_r, res_len

        # Time complexity: O(n) as we iterate over all the elements in the string
        for i in range(len(s)):
            # Optimization by @victorvelmakin9907 in neetcode's youtube video
            # Basically if half the length of the longest palindrome is already
            # greater than the remaining characters in the string s, we stop
            # checking
            if res_len > 0 and len(s) - i - 1 < res_len // 2:
                break

            # odd length
            res_l, res_r, res_len = extend(i, i, res_l, res_r, res_len)

            # Handle even length palindromes
            res_l, res_r, res_len = extend(i, i + 1, res_l, res_r, res_len)

        # Slice the string with the longest palindrome
        return s[res_l:res_r]


s = Solution()

print(s.longestPalindrome("babad"))  # aba or bab
print(s.longestPalindrome("cbbd"))  # bb
