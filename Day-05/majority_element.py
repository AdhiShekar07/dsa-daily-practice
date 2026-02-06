"""
Problem: Majority Element
Platform: LeetCode / GeeksforGeeks
Difficulty: Easy
Approach: Boyer-Moore Voting Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
