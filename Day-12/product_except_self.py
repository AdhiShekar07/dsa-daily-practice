"""
Problem: Product of Array Except Self
Platform: LeetCode
Difficulty: Medium
Approach: Prefix & Suffix Product
Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
"""

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result
