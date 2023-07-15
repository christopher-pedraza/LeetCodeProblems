# Time complexity: O(n) - actually O(3n) as you need to iterate over nums
#                         twice to get the left and right products, and once
#                         to store the answer
# Space complexity: O(n) - arrays of size n are needed to store the products
#                          and answer

def productExceptSelf(nums):
    # Create lists filled with 0s of length nums for the
    # product of the left side, right side, and to store
    # the answers of multiplying the left product by the 
    # right one on each index
    left = [0 for i in range(len(nums))]
    right = [0 for i in range(len(nums))]
    ans = [0 for i in range(len(nums))]

    # left side products
    currentProduct = 1
    # Iterate from 0->length of nums
    # In each index i you save the product of the numbers on the left
    # side from the index.
    #   ex. [2, 4, 6]
    #    left[0] = 1
    #    left[1] = 2
    #    left[2] = 8
    for i in range(0, len(nums), 1):
        left[i] = currentProduct
        currentProduct *= nums[i]

    # right side products
    currentProduct = 1
    # Iterate from (length of nums-1) -> -1 (0 inclusive)
    # In each index i you save the product of the numbers on the right
    # side from the index.
    #   ex. [2, 4, 6]
    #    right[0] = 24
    #    right[1] = 6
    #    right[2] = 1   
    for i in range(len(nums)-1, -1, -1):
        right[i] = currentProduct
        currentProduct *= nums[i]
    
    # Save the product of left*right in each index of ans
    #   ex. input: [2, 4, 6]   left: [1, 2, 8]   right: [24, 6, 1]
    #    ans[0] = 1*24 = 24
    #    ans[1] = 2*6  = 12
    #    ans[2] = 8*1  = 8
    for i in range(len(nums)):
        ans[i] = left[i]*right[i]

    return ans

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))