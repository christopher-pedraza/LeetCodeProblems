# Neetcode.io's solution

# Time complexity: O(n^2*m) because we will iterate once over the string s looking for the
# words m and the looking operation will check for the n chars.
# Space complexity: O(n) where n is the length of the string s, as we need to store for
# every index of it True/False

# The brute force solution would be to check from every character in the string s, if we
# can form the words from the wordDict, this would end with a time complexity of O(n^2)
# where n is the size of the string s.
#
# A more efficient way to solve this would be to instead of checking from every character
# all the other words, just search every word and move a pointer if we find the word to
# after its length. This is a DP approach and would be O(n*m) where n is the size of s and
# m the number of words in the wordDict:
# s = "neetcode"
# wordDict = ["neet", "leet", "nee", "code"]
#
# i = 0
# |- neet
#    i = 4 / remaining chars: "code"
#    |- neet - x
#    |- leet - x
#    |- nee - x
#    |- code
#       i = 8 / remaining chars: ""
#       --------RETURN TRUE--------
# |- leet - x
# |- nee
#    i = 3 / remaining chars: "tcode"
#    |- neet - x
#    |- leet - x
#    |- nee - x
#    |- code - x
# |- code - x
#
# We will be storing if any solution evers returns false (for example the "nee" path) in
# case we ever return to the same index (in this case index 3) we can not repeat the
# validations all over again.
# For example: "dp[3] = False"
#
# Notice that when there's no more characters in s, it means we were able to break the word
# s using the words in the wordDict and return True.
#
#
# Now, the Dynamic Programming approach would be like this:
#
# s = "neetcode"
# wordDict = ["neet", "leet", "code"]
#
# We will start from the end/top knowing that it would be true if we ever get to that point
# because its outside of the word. This is the base case
# dp[8] = True
#
# Now, for the other values, we will check if there's any word that matches the remaining
# length and if so, if it matches the characters in that space:
# "e"
# dp[7] = False
# "de"
# dp[6] = False
# "ode"
# dp[5] = False
# As there's no word of 3 chars, all these dp's are false
#
# "code"
# dp[4] = dp[4+len("code")]
# dp[4] = dp[8]
# dp[4] = True
# But this dp is True as the word "code" exists in the wordDict
#
# "tcode"
# dp[3] = False
# "etcode"
# dp[2] = False
# "eetcode"
# dp[1] = False
#
# "neetcode"
# dp[0] = dp[0+len("neet")]
# dp[0] = dp[4]
# dp[0] = true
# dp[0] is true as the word neet exists, and as it's of 4 letters and in the fourth
# position of the dp it's true, then dp[0] is also true


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # At the beginning, we will store in every index of the string s + 1 (for the
        # base case outside of the string) False
        dp = [False] * (len(s) + 1)
        # The base case starts with True as it would mean it was possible to break the
        # word
        dp[len(s)] = True

        # Iterate top-down for every position in the string s (O(n))
        for i in range(len(s) - 1, -1, -1):
            # For each position in the string we will check whether we find the words
            # (O(m))
            for w in wordDict:
                # We check if the length from the current index is enough for the size of
                # the word w and if the sliced portion is equal to the word
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # dp[i] will be the dp of the current index + the size of the word
                    dp[i] = dp[i + len(w)]
                # If we have already calculated a True in the index i, we don't need to
                # process it again and can stop the loop
                if dp[i]:
                    break

        # If dp[0] is True, we managed to break the string s into the words of wordDict
        # because:
        # dp[0] = dp[0 + len("neet")]
        # dp[0] = dp[4]
        # dp[0] = dp[4 + len("code")]
        # dp[0] = dp[8]
        # dp[0] = True
        # If we managed to arrive at the base case, we successfully broke the word, if not
        # it's not possible to break it
        return dp[0]


s = Solution()

print(s.wordBreak("leetcode", ["leet", "code"]))  # True
print(s.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
