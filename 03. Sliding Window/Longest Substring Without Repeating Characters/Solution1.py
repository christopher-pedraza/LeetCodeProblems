# Neetcode.io solution

# Time complexity: O(n) go through the entire
#				   list once
# Space complexity: O(n) potentially all chars
#					are unique and have to add
#					them to the set

def lengthOfLongestSubstring(s):
	# Use a set to check if we have duplicate
	# characters in constant time. This could
	# also be done with a list, however, in a
	# list, usually contains() is run in linear
	# time.
	charSet = set()
	# Left pointer
	# We also have a right pointer, but this
	# one will change while we visit the chars
	# in the string, so it's going to be in the
	# for loop
	l = 0
	# Stores the longest substring that has been
	# found
	longestSubstring = 0

	# Move the right pointer through the string
	# Each time you move it, you are going to check
	# if the new character that's been added to the
	# substring was already in the set. If so, we
	# have to shrink the substring until it doesn't
	# include that character. In order to shrink it
	# we are going to move the left pointer, removing
	# the characters that are no longer included from
	# the set. After adjusting the left pointer so
	# the substring doesn't include duplicates, add
	# the new character (in the right pointer position)
	# to the set and calculate again the length of the
	# substring. We're only going to store the max
	# value from the previous and new one. After that
	# keep moving the right pointer and repeating the
	# steps until you go through the entire string
	for r in range(len(s)):
		# If the current character is already in the
		# set, remove it and check for the next char
		while s[r] in charSet:
			# Remove the character in the left pointer
			# from the set and move the pointer 1 pos
			# to the right.
			# Time complexity of removing: O(1)
			charSet.remove(s[l])
			l += 1
		# After removing the duplicate, add the char to
		# the set
		# Time complexity of adding: O(1)
		charSet.add(s[r])
		# And calculate the new max length
		# Time complexity of max: O(n)
		longestSubstring = max(longestSubstring, r - l + 1)
	return longestSubstring

print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("pwwkew")) # 3