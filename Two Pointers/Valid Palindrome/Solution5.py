# Time complexity: O(n) - iterate once over the string
# Space complexity: O(n) - need to save the cleaned string 

def isPalindrome(s):
	# Used to stored the only-alphanum-string
	newStr = ""

	#
	# Getting the string with only alphanumeric characters
	#
	# Iterate over the chars of the input string
	for c in s:
		# Check if the char is alphanumeric
		if c.isalnum():
			# If so, add it into the new string as a lowercase
			# character
			newStr += c.lower()

	#
	# Checking if the string is the same as its reverse version
	#
	return newStr == newStr[::-1]


		
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome(".,"))