# Time complexity: O(n) - iterate once over the string and converting chars
#                         into lowercase
# Space complexity: O(1) - no need to save anything extra

def isPalindrome(s):
	# Converts the string's characters into lowercase
	# Time complexity of O(n) where n is the length of the string
	s = s.lower()
	# Pointers (indexes)
	left = 0
	right = len(s)-1

	# Iterate over the characters in the string
	# If the left is greater than the right, it means you already checked
	# both halves, so you don't need to continue 
	while left < right:
		# While the char in the left/right index is not alphanumeric, you
		# move the pointer to the right/left accordingly
		while left < right and not s[left].isalnum():
			left += 1
		while left < right and not s[right].isalnum():
			right -= 1

		# If the characters in the indexes are not the same, it means it's
		# not a palindrome
		if s[left] != s[right]:
			return False
		# If they are the same, just update the indexes to continue checking
		else:
			left += 1
			right -= 1

	# If you didn't find a pair of chars that was different, it's a palindrome
	return True

		
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome(".,"))