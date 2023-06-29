# Time complexity: O(n) - iterating twice over the string
# Space complexity: O(n) - saving the string in another cleaned string 

# Not needed in leetcode:
from string import ascii_lowercase

def isPalindrome(s):
	phrase = ""

	# Convert the input string into lowercase and remove any character
	# other than alphanumeric
	s = s.lower()
	for t in s:
		if t in ascii_lowercase or t in [str(x) for x in range(10)]:
			phrase += t

	# Iterate over the cleaned string and check if the left pointer
	# is the same as the right one. If once they are not the same, 
	# it's not a valid palindrome
	for i in range(len(phrase)):
		left = phrase[i]
		right = phrase[-1*(i+1)]
		if left != right:
			return False

	# If iterating from the left is the same as doing it from the right
	# it's a valid palindrome
	return True
		

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))