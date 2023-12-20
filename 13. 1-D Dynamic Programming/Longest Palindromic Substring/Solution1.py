# Solutions from (He has other viable solutions in the link):
# https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/

# Time complexity: O(n) where n is the length of the input string. This is because
#                  the algorithm scans the input string linearly.
# Space complexity: O(n) where n is the length of the input string. This is
#                   because a new string is created with '#' inserted between each
#                   character and at both ends, and a list dp of the same length
#                   is created to store the length of the palindrome with the
#                   center at each character.


class Solution:
    # Define a method to find the longest palindrome in a string
    def longestPalindrome(self, s: str) -> str:
        # If the string is empty or only contains one character, return the
        # string itself
        if len(s) <= 1:
            return s

        # Initialize the maximum length of palindrome and the palindrome string
        Max_Len = 1
        Max_Str = s[0]

        # Add '#' between each character in the string and at both ends
        s = "#" + "#".join(s) + "#"

        # Initialize a list to store the length of the palindrome with the center
        # at each character
        dp = [0 for _ in range(len(s))]

        # Initialize the center and the right boundary of the palindrome
        center = 0
        right = 0

        # Iterate through each character in the string
        for i in range(len(s)):
            # If the character is within the right boundary of the current
            # palindrome
            if i < right:
                # The length of the palindrome with the center at the character
                # is either the distance to the right boundary or the length of
                # the palindrome symmetric to the center
                dp[i] = min(right - i, dp[2 * center - i])

            # Expand the palindrome centered at the character as much as possible
            while (
                i - dp[i] - 1 >= 0
                and i + dp[i] + 1 < len(s)
                and s[i - dp[i] - 1] == s[i + dp[i] + 1]
            ):
                dp[i] += 1

            # If the right boundary of the palindrome centered at the character
            # is beyond the current right boundary, update the center and the
            # right boundary
            if i + dp[i] > right:
                center = i
                right = i + dp[i]

            # If the length of the palindrome centered at the character is greater
            # than the current maximum length, update the maximum length and the
            # palindrome string
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i - dp[i] : i + dp[i] + 1].replace("#", "")

        # Return the longest palindrome string
        return Max_Str


s = Solution()

print(s.longestPalindrome("babad"))  # aba or bab
print(s.longestPalindrome("cbbd"))  # bb
