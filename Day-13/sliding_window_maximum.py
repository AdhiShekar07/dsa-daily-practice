"""
Problem: Sliding Window Maximum
Platform: LeetCode
Difficulty: Hard
Approach: Monotonic Deque
Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        
        # Remove elements outside window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Start adding result after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
