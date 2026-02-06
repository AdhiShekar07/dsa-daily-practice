"""
Problem: Move Zeros to End
Platform: LeetCode
Difficulty: Easy
Approach: Two Pointer / In-place modification
Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeros(nums):
    pos = 0

    # Step 1: Move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    # Step 2: Fill remaining positions with zeros
    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums
