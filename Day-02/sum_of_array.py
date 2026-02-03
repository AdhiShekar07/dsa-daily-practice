"""
Problem: Sum of Elements in an Array
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Simple Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
