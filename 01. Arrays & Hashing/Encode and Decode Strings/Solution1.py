# Neetcode.io solution

# Time complexity: O(n) as you need to iterate over all the words in the list
# Space complexity: O(n) as you store a string containing all the words in the list
def encode(strs):
	res = ""
	# Iterate over the words in the list
	for s in strs:
		# Concatenate each word with the length of it preceeding it followed by a #
		res += str(len(s)) + "#" + s
	return res

# Time complexity: O(n) as you need to iterate once over all the chars in the string
# Space complexity: O(n) as you save a list with the words in the string
def decode(str):
	# Resulting list with the words
	res = []
	# Index for the loop
	i = 0

	# Using a while-loop so I can change the value of i inside the loop
	while i < len(str):
		j = i

		# Search for the delimiter. All numbers before are the length
		while str[j] != "#":
			j += 1

		# Once j is in the pos of #, you can slice the string from the i index up to
		# j (pos of #), where j is not included
		length = int(str[i:j])

		# Get the word from the char after the delimiter (in index j) up to the length
		# of the word (not included) and append it into the list
		res.append(str[j+1: j+1+length])

		# Each iterationg, set the end of the word (which is actually the next char as it's 
		# 0-based) as the next index of i
		i = j+1+length
	# Return the resulting list with the words
	return res

print(encode(["lintisacodingsite","code","love","you"]))
print(decode(encode(["lintisacodingsite","code","love","you"])))