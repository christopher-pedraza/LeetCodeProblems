# Neetcode.io solution

# Time complexity: O(n) - actually O(2n) as you need to iterate over nums
#                         twice to get the left and right products
# Space complexity: O(1) - other than the answer list, no other list is needed

def productExceptSelf(nums):
    # Create lists filled with 0s of length nums
    # Also: `ans = [0 for i in range(len(nums))]`
    ans = [0]*len(nums)
    
    # left side products
    currentProduct = 1
    # Iterate from left to right storing the product of all numbers before the
    # current index
    for i in range(0, len(nums), 1):
        ans[i] = currentProduct
        currentProduct *= nums[i]

    # right side products 
    currentProduct = 1
    # Iterate from right to left multiplying the stored values (left products) by
    # the product of all the numbers at the right of the current index. 
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= currentProduct
        currentProduct *= nums[i]

    return ans

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))