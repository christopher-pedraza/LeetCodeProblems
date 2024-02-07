# Neetcode.io solution

# THE JAVA SOLUTION IS SIMPLER AS YOU DON'T NEED TO HANDLE NEGATIVE NUMBERS

# Time complexity: O(1) as the problem won't grow linearly as we have an integer
# constraint of -1000 <= a, b <= 1000.
# Space complexity: O(1) as we are not using any extra space to solve the problem.

# To add two bits, we can use the XOR operation. If both bits are 0 or 1, as they are
# same, the result will be 0, with the difference that when there's two 1s, we should
# have a carry of 1. When the two bits are not the same, we will have a 1 as a result
# as exepcted of the operation:
#  0 ^ 1 = 1
#  1 ^ 0 = 1
#  0 ^ 0 = 0
#  1 ^ 1 = 0 with carry 1

# To know when we should have a 1 as a carry, we can use the AND operation. If both
# bits are 1, the result will be 1, otherwise, it will be 0. This is the carry we
# should add to the next bit. This carry will be added to the next bit by shifting it
# one position to the left.

# We will be performing the operation on the whole integer, however, in order to
# consider the carries, we will have a loop so we can do the operation again if we
# ended up with a carry, if not, we will end up the loop. We will have a loop where we
# will be passing the two nums to the add function. We will always pass the result of
# the XOR operation as the first parameter and the result of the AND operation shifted
# to the left as the second parameter in case we have a carry. We will keep doing this
# until any of the values is 0. Example:
#
#   1 0 0 1 (9)
# ^
#   1 0 1 1 (11)
# ----------
#   0 0 1 0 (2)
#   ^     ^
#   \------\-- carry 1 as the AND operator would result in 1001, then we shift it to
#              the left to get 10010, which is 18
#
# 1 0 0 1 0
# This integer will be added (XOR) to the result we had from the XOR operation:
#  0 0 0 1 0 (2)            0 0 0 1 0 (2)
# ^                     AND
#  1 0 0 1 0 (18)           1 0 0 1 0 (18)
# -----------              -----------
#  1 0 0 0 0 (16)           0 0 0 1 0 (2)  <- Shift to left: 00100 (4)
#
# We will keep doing this until we don't have any carry.
#
#  0 0 1 0 0 (4)            0 0 1 0 0 (4)
# ^                     AND
#  1 0 0 0 0 (16)           1 0 0 0 0 (16)
# -----------              -----------
#  1 0 1 0 0 (20)           0 0 0 0 0 (0)  <- Shift to left: 00000 (0)
#
# As we don't have any carry, we will end up the loop and return the result of the XOR
# operation, which is 20.


class Solution:
    # Define a method getSum that takes two integers a and b as input and returns an
    # integer
    def getSum(self, a: int, b: int) -> int:
        # Define a helper function add that takes two integers a and b as input
        def add(a, b):
            # If either a or b is zero, return the other number
            # This is because adding zero to a number does not change the number
            if not a or not b:
                return a or b
            # If neither a nor b is zero, recursively call the add function
            # The first argument is the XOR of a and b, which gives the sum without
            # carrying
            # The second argument is the AND of a and b left shifted by one, which
            # gives the carry
            # The recursion continues until there is no carry, at which point the sum
            # is returned
            return add(a ^ b, (a & b) << 1)

        # ALL OF THIS NEEDS TO BE ADDED BECAUSE IN PYTHON NEGATIVE NUMBERS ARE STORED
        # IN TWO'S COMPLEMENT FORM, OTHER LANGUAGES SUCH AS JAVA AND C++ STORE NEGATIVE
        # NUMBERS IN TWO'S COMPLEMENT FORM AS WELL BUT THEY USE A DIFFERENT NUMBER OF
        # BITS TO REPRESENT INTEGERS, SO YOU DON'T NEED TO WORRY ABOUT THIS IN THOSE
        # LANGUAGES
        # If a and b have different signs (i.e., one is positive and the other is
        # negative)
        if a * b < 0:
            # If a is positive, swap a and b and recursively call the getSum function
            # This is done to ensure that a is negative and b is positive
            if a > 0:
                return self.getSum(b, a)
            # If the absolute value of a is equal to b (i.e., -a == b), return 0
            # This is because a number plus its negation equals zero
            """ Explanation of the tilde operator in Python
            The tilde ~ is a unary operator in Python that is used for bitwise
            negation. It takes a number x and inverts all the bits in its binary
            representation.
            
			In other words, for every 1 in the binary representation of x, it changes
            it to 0, and for every 0, it changes it to 1.
            
			However, in Python, the result of ~x is computed as -(x+1). This is
            because Python uses a form of binary representation known as two's
            complement, which allows it to represent negative numbers in a way that
            is convenient for binary arithmetic.
            
			For example, ~5 in Python would give -6 because it inverts the bits in
            the binary representation of 5 (which is 101), resulting in 010 (which
            is 2), but then applies the two's complement rule to give -6.
            
            The expression add(~a, 1) in Python is essentially calculating the absolute
            value of a. Here's why:
            
			The ~a is a bitwise negation of a, which flips all the bits in the binary
            representation of a. In Python, this is equivalent to -(a+1) due to
            Python's use of two's complement binary representation.

			So, ~a is -(a+1). When you add 1 to ~a, you get -(a+1) + 1, which simplifies
            to -a.

			Therefore, add(~a, 1) is equivalent to -a, which is the absolute value of a
            if a is negative. If a is positive, add(~a, 1) will return a negative value.

			In the context of the code you provided, add(~a, 1) is used to get the
            absolute value of a when a is negative.
            """
            if add(~a, 1) == b:
                return 0
            # If the absolute value of a is less than b (i.e., -a < b)
            if add(~a, 1) < b:
                # Return the negation of the sum of the absolute values of a and b
                # This is done by taking the bitwise complement of a and b, adding
                # them, and then taking the bitwise complement of the result
                # The bitwise complement of a number is the same as negating the number
                # and subtracting 1
                return add(~add(add(~a, 1), add(~b, 1)), 1)

        # If a and b have the same sign or the absolute value of a is greater than b
        # Return the sum of a and b using the add helper function
        return add(a, b)


s = Solution()

print(s.getSum(1, 2))  # 3
print(s.getSum(-2, 3))  # 1
print(s.getSum(-2, -3))  # -5
print(s.getSum(2, 3))  # 5
