# DOES NOT WORK

# Time complexity: 
# Space complexity: 

def lengthOfLongestSubstring(s):
	l, r = 0, 0
	maxLen = 0

	for c in s:
		if c not in s[l:r+1]:
			r += 1
		else:
			maxLen = max(maxLen, r - l + 1)
			l += 1

	return maxLen


print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("pwwkew")) # 3