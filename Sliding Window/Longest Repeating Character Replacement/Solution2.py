# Neetcode.io solution

# Time complexity: O(26*n)
# Space complexity: O(n)

def characterReplacement(s, k):
	# We're going to count the frequency of
	# the chars in the substring in order to
	# replace the chars with the char that
	# repeats the most as k is limited
	# To know the chars that need to be
	# replaced, we can do:
	# `windowLen-Count[MostFreqChar]`
	# Then we can check if the result of the
	# operation is <= to k. If so, the current
	# window is valid as we have enough
	# replacements to have equal chars
	count = {} # char -> count of ocurrences
	res = 0
	l = 0

	for r in range(len(s)):
		# Add 1 to the count of each char
		count[s[r]] = 1 + count.get(s[r], 0)

		# If the lenght of the window minus the max
		# frequency of chars (max number of chars that
		# are the same) is greater than k, it means
		# we need to slide the window as it already
		# surpases the maximum replacements allowed
		# We do this operation because, consider this:
		# s="AABAB", k=1
		# window="AAB", len=3, maxF[A]=2
		#   3-2 = 1 is less than k
		# window="AABB", len=4, maxF[A]=2 / maxF[B]=2
		#   4-2 = 2 is NOT less than k
		while(r-l+1) - max(count.values()) > k:
			# Decrease the count of the char in the left
			# pointer as it's going to move to the right
			# one position
			count[s[l]] -= 1
			l += 1

		# Get the maximum lenght of the substring from the
		# current and previous
		res = max(res, r-l+1)

	return res
	
print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABABBA", 1)) # 4
print(characterReplacement("ABBB", 2)) # 4