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
		while left < right and not isAlphaNum(s[left]):
			left += 1
		while left < right and not isAlphaNum(s[right]):
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

# Function to check if a char is alphanumeric
# It converts the chars into integers using ord and check if the received
# char is between the range
def isAlphaNum(c):
	if ord(c) >= ord('a') and ord(c) <= ord('z'):
		return True
	elif ord(c) >= ord('0') and ord(c) <= ord('9'):
		return True
	else:
		return False

		

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome(".,"))