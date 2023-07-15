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
	# Stores the length of each word
	length = ""
	# Stores the chars of a word
	word = ""
	# Resulting list with the words
	res = []
	# Index for the loop
	i = 0

	# Using a while-loop so I can change the value of i inside the loop
	while i < len(str):
		# If the char is a #, it means I already have all the numbers representing
		# the length of the next word
		if (str[i] == "#"):
			# Transform the string length into an int (it's a string so I can concatenate
			# the numbers while reading the chars)
			length = int(length)
			# Iterate over the next characters from current pos using the length of the word
			for j in range(i+1, i+1+length):
				# Concatenating each char into word
				word += str[j]
			# When the word is finished, append it into the resulting list
			res.append(word)
			# Update the index adding the length of the word that has been added to the list
			i += length
			# Reset the values of length and word as I concatenate chars into them
			length = ""
			word = ""
		# If it's not a #, its the numbers representing the length of the word
		else:
			# Concatenate them into length as a string (keep it as a string so I can continue
			# concatenating chars, when I find a #, I change it into an int as it means I already
			# have all the numbers)
			length += str[i]
		# Each iterationg, add 1 to the index
		i += 1	
	# Return the resulting list with the words
	return res

print(encode(["lintisacodingsite","code","love","you"]))
print(decode(encode(["lintisacodingsite","code","love","you"])))