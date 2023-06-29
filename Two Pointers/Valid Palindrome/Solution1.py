# Neetcode.io solution

# Time complexity: O(n) - iterate once over the string and converting
#                         chars into lowercase
# Space complexity: O(1) - no need to save anything extra

def isPalindrome(s):
    # Pointers (indexes)
    l, r = 0, len(s) - 1

    # Iterate over the characters in the string
    # If the left is greater than the right, it means you already
    # checked both halves, so you don't need to continue 
    while l < r:
        # While the char in the left/right index is not alphanumeric,
        # you move the pointer to the right/left accordingly
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum(s[r]):
            r -= 1

        # If the characters in the indexes are not the same, it means it's
        # not a palindrome
        if s[l].lower() != s[r].lower():
            return False

        # Update the indexes to continue checking
        l += 1
        r -= 1

    # If you didn't find a pair of chars that was different, it's a palindrome
    return True

# Function to check if a char is alphanumeric
# It converts the chars into integers using ord and check if the received
# char is between the range
def alphanum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )

        
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome(".,"))