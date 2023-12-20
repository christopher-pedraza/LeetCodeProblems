# Neetcode.io solution

# Time complexity: O(n^2) where n is the length of the string s. This is because
#                  we will check for every character in the string, the palindromes
#                  that can be formed with that character as the center. This
#                  produces a time complexity of O(n^2), however, we need to do
#                  this process twice as we need to check for even-sized
#                  palindromes, as well as odd-sized, thus having a O(2n^2), which
#                  overall is O(n^2)
# Space complexity: O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        def extend(l, r, res):
            # While both pointers are inbound and equal...
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # It means we found a palindrome, so we increase the counter
                res += 1
                # Shift the pointers
                l -= 1
                r += 1
            return res

        # Store the amount of palindromic substrings
        res = 0
        # Iterate over all the chars in the string to check from each one the
        # amount of palindromic substrings
        for i in range(len(s)):
            # Count odd and even palindromes
            res = extend(i, i, res)
            res = extend(i, i + 1, res)
        # Return the count of the palindromes found
        return res


s = Solution()

print(s.countSubstrings("abc"))  # 3
print(s.countSubstrings("aaa"))  # 6
