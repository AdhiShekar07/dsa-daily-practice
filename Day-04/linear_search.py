"""
Problem: Linear Search
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Sequential Search
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
