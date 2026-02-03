"""
Problem: Find the Largest Element in an Array
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Linear Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def largest(self, arr):
        mx = arr[0]  # assume first element is the largest

        for i in range(1, len(arr)):
            if arr[i] > mx:
                mx = arr[i]

        return mx
